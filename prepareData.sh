
if [ ! -d COCO_OI ] 
then
	mkdir COCO_OI
	mkdir COCO_OI/train
	mkdir COCO_OI/val	
	mkdir COCO_OI/annotations
fi
cd COCO_OI


# get the coco data
if [ ! -d COCO_data ] 
then
	mkdir COCO_data
fi


wget http://images.cocodataset.org/zips/train2017.zip
wget http://images.cocodataset.org/zips/val2017.zip
wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip

unzip -d COCO_data train2017.zip
unzip -d COCO_data val2017.zip
unzip -d COCO_data annotations_trainval2017.zip

#rm train2017.zip val2017.zip annotations_trainval2017.zip



# get OpenImages data
wget https://storage.googleapis.com/openimages/v6/oidv6-train-annotations-bbox.csv
wget https://storage.googleapis.com/openimages/v5/validation-annotations-bbox.csv
wget https://storage.googleapis.com/openimages/v5/test-annotations-bbox.csv
wget https://storage.googleapis.com/openimages/v5/class-descriptions-boxable.csv



# merge the data and prepare the annotations
cd ..

python read_OI_data.py
python downloader.py 'COCO_OI/validation_images_to_download.csv' --download_folder='COCO_OI/train' --num_processes=5
python downloader.py 'COCO_OI/test_images_to_download.csv' --download_folder='COCO_OI/train' --num_processes=5
python downloader.py 'COCO_OI/train_images_to_download.csv' --download_folder='COCO_OI/train' --num_processes=5

python append_annotation_to_COCO.py

FILE=COCO_OI/annotations/instances_train.json
if [ -f "$FILE" ]; then

	mv COCO_OI/COCO_data/annotations/instances_val2017.json COCO_OI/annotations/instances_val.json

	ulimit -S -s unlimited

	mv COCO_OI/COCO_data/train2017/* COCO_OI/train
	mv COCO_OI/COCO_data/val2017/* COCO_OI/val

	# rm -rf COCO_OI/COCO_data/ 
	rm ./COCO_OI/*.csv
	#rm ./COCO_OI/*.zip
	rm -rf COCO_OI/COCO_data

	# get the detection code from here
	# git clone https://github.com/zylo117/Yet-Another-EfficientDet-Pytorch.git
	wget https://github.com/zylo117/Yet-Another-EfficientDet-Pytorch/archive/master.zip
	unzip master.zip
	rm master.zip
	mv Yet-Another-EfficientDet-Pytorch-master Yet-Another-EfficientDet-Pytorch

fi








