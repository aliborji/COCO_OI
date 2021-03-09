# reading the csv file and appending it to the COCO json train annotations

import json 
from coco_OI_objects import *
from PIL import Image
from os import path

# 1.  read the COCO train json file  
# 2.  read the train, test and validation csv files from the open images file
# 3.  merge the two in one big json file 
# 4.  update the COCO training json files (and copy the images to the destination manually)

#  I got the coco data from the ROBOFLow; make sure to fix the label name mismatch both in the validation and train json files first (and make it consistent with the COCO_OI_objects.py)


# 1.
with open('./COCO_OI/COCO_data/annotations/instances_train2017.json', 'r') as f:
	COCO_train_json = json.load(f)

print(COCO_train_json.keys())
print(COCO_train_json['categories'])


# last_img_id = COCO_train_json['images'][-1]['id']
# last_box_id = COCO_train_json['annotations'][-1]['id']

MAX_IMG_ID = -1
for x in COCO_train_json['images']: 
	if x['id'] > MAX_IMG_ID:
		MAX_IMG_ID = x['id']
last_img_id = MAX_IMG_ID

MAX_BOX_ID = -1
for x in COCO_train_json['annotations']: 
	if x['id'] > MAX_BOX_ID:
		MAX_BOX_ID = x['id']
last_box_id = MAX_BOX_ID
print(last_img_id, last_box_id)





# 2.
class_mapping = {}
with open('./COCO_OI/class-descriptions-boxable.csv', 'r') as f:
	cls = f.readlines()

for i in cls:
	a, b = i.strip().split(',')
	class_mapping[a] = b.lower()

# print(class_mapping)

OI_to_COCO_dict = {}
for k,v in COCO_to_OI_dict.items():
	if type(v) is not list:
		OI_to_COCO_dict[v.lower()] = k.lower()
	else:	
	    for x in v:
	    	OI_to_COCO_dict[x.lower()] = k.lower()

print(OI_to_COCO_dict)



# 3.
# 3.1 add images
imgs_to_add = []
IMG_FILES = ['train_images_to_download.csv', 'test_images_to_download.csv', 'validation_images_to_download.csv']
# IMG_FILES = ['validation_images_to_download.csv']
tmp_img_dict = {}
for IMG_FILE in IMG_FILES:
	with open(path.join('./COCO_OI/', IMG_FILE), 'r') as f:
		imgs = f.readlines()

	for img in imgs:
		last_img_id += 1
		im_path = path.join('./COCO_OI/train', img.strip().split('/')[-1]+'.jpg')
		im = Image.open(im_path)
		# resize the image while keeping the aspect ratio; change the width to 640 and adjust the height accordingly
		im.thumbnail((640,640), Image.ANTIALIAS)
		im.save(im_path)

		imgs_to_add.append({
	            "id": last_img_id,
	            "license": 1,
	            "file_name": img.strip().split('/')[-1]+'.jpg',
	            "height": im.height,
	            "width": im.width,
	            "date_captured": ""
	        })
		tmp_img_dict[img.strip().split('/')[-1]] = [last_img_id, im.width, im.height] 
		


print(len(imgs_to_add))



# 3.2 add boxes
# get the ids of the categories from the COCO json first
map_to_catID = {}
for cat in COCO_train_json['categories']:
	map_to_catID[cat['name']] = cat['id']


boxes_to_add = []
BOX_FILES = ['train_annotations_new.csv', 'test_annotations_new.csv', 'validation_annotations_new.csv']
# BOX_FILES = ['validation_annotations_new.csv']

for BOX_FILE in BOX_FILES:
	# print(BOX_FILE)
	with open(path.join('./COCO_OI/', BOX_FILE), 'r') as f:
		boxes = f.readlines()

	boxes = boxes[1:] # skip the first row in train csv

	for row in boxes:
		last_box_id += 1

		img_name, _, box_label, _, minX, maxX, minY, maxY, *_ = row.strip().split(',')
		img_id, im_width, im_height = tmp_img_dict[img_name]

		minX, maxX, minY, maxY = float(minX), float(maxX), float(minY), float(maxY)
		minX, maxX, minY, maxY = minX * im_width, maxX * im_width, minY * im_height, maxY * im_height

		boxes_to_add.append({
            "id": last_box_id,
            "image_id": img_id,
            "category_id": map_to_catID[OI_to_COCO_dict.get(class_mapping[box_label], -1)],
            "bbox": [
                minX ,  # top left x
                minY ,  # top left y
                (maxX - minX) ,	  # box width
                (maxY - minY) 	  # box height
            ],
            "area": (maxX - minX) * (maxY - minY),
            "segmentation": [],
            "iscrowd": 0
        })		


print(len(boxes_to_add))
# print(boxes_to_add[1:3])




# 4. 
COCO_train_json['images'].extend(imgs_to_add)
COCO_train_json['annotations'].extend(boxes_to_add)


print(len(COCO_train_json['images']))
print(len(COCO_train_json['annotations']))


filename = path.join('./COCO_OI/annotations', 'instances_train.json')
print('writing output to {}'.format(filename))
json.dump(COCO_train_json,  open(filename, "w"))
print('Done')

