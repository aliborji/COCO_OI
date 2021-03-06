# create the list of files from classes that we are interested in from the OpenImages dataset

from collections import  defaultdict
from coco_OI_objects import *
from os import path
import csv
import numpy as np


subsets = ['train', 'test', 'validation']

for subset in subsets:

	# set the dataset info you want to retrieve the images
	SET_NAME = f'{subset}/'
	if subset=='train':
		SET_DIR = 'oidv6-train-annotations-bbox.csv'
	else:
		SET_DIR = f'{subset}-annotations-bbox.csv'
	SET_WRITE_DIR = f'{subset}_images_to_download.csv'
	SET_ANNT_DIR = f'{subset}_annotations_new.csv'


	DISCARDED_CLASSES = ['person', 'car', 'chair'] #, 'tie'] #, 'boat', 'book', 'tie', 'cup', 'bottle', 'umbrella', 'bowl', 'traffic light', 'banana', 'handbag', 'truck', 'dining table', 'bench']
	#DISCARDED_CLASSES = list(set(COCO_to_OI_dict.keys()) - {'train', 'horse'}) # just for testing the code; remove!!!!!!!!!!!
	DISCARDED_CLASSES = [c.lower() for c in DISCARDED_CLASSES]
	MY_CLASSES = [c.lower() for c in COCO_to_OI_dict.keys() ]
	DESIRED_CLASSES = [c for c in MY_CLASSES if c not in DISCARDED_CLASSES] # to sample more




	# class mapping in OI
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

	# print(OI_to_COCO_dict)

	#  ----------------------------------------------------------------
	# read the annotation boxes
	box_freqs = defaultdict(int)
	# img_freqs = defaultdict(int)

	img_lst = defaultdict(list)
	with open(path.join('./COCO_OI', SET_DIR), 'r') as f:
		all_boxes = f.readlines()

	for idx, row in enumerate(all_boxes):
		if not idx: continue
		img_name, _, box_label, *_ = row.strip().split(',')
		img_lst[img_name].append(box_label)

	# print(img_lst)


	img_short_list = []
	for img_name, box_labels in img_lst.items():
		# if len(img_short_list) > NUM_IMAGES_TO_DOWNLOAD: break

		box_classes = []
		for x in box_labels:
			if class_mapping[x].lower() in OI_to_COCO_dict.keys():
				box_classes.append(OI_to_COCO_dict[class_mapping[x].lower()])


		if any([x in DESIRED_CLASSES for x in box_classes]) and \
			all([x not in DISCARDED_CLASSES for x in box_classes]): #DESIRED_CLASSES]): # and \
			# not any([True for x in box_labels if class_mapping[x].lower() in DISCARDED_CLASSES]):	# if any of the boxes fall in classes of interest	
			img_short_list.append(SET_NAME+img_name)
			for box in box_classes:
				box_freqs[box] += 1	 

			

	print(box_freqs)


	img_indices = {}#np.zeros(len(img_lst))
	for l in img_short_list:
		a,b = l.split('/')
		img_indices[b] = 1

	# ----------------------------------------
	# generate the new and smaller validation annotatios
	# csv_f = open(path.join('./OpenImages', SET_ANNT_DIR), 'w') 
	# csv_writer = csv.writer(csv_f, delimiter='')

	with open(path.join('./COCO_OI', SET_ANNT_DIR), 'w') as f:

		# already_added_imgs = []
		# annts = ''

		for idx, row in enumerate(all_boxes):
			# if not idx: continue
			im_name, _, x, *_ = row.strip().split(',')

			if idx == 0:
				f.write(row)
				continue

			if class_mapping[x].lower() not in OI_to_COCO_dict.keys(): continue
			if img_indices.get(im_name,False):
				f.write(row)

	# print(img_short_list)

	#  ----------------------------------------------------------------
	with open(path.join('./COCO_OI', SET_WRITE_DIR), 'w') as f:
		for im_name in img_short_list: # because we want the total to be 225K
			f.write(im_name+'\n')

	print(len(img_short_list))
