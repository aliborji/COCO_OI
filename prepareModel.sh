
cd Yet-Another-EfficientDet-Pytorch

# 1. ge the code
# pip install pycocotools numpy==1.16.0 opencv-python tqdm tensorboard tensorboardX pyyaml webcolors matplotlib


mkdir datasets
mv ../COCO_OI ./datasets/

mv ../COCO_OI.yml  ./projects



mkdir weights
wget https://github.com/zylo117/Yet-Another-EfficientDet-Pytorch/releases/download/1.0/efficientdet-d0.pth -O   ./weights/efficientdet-d0.pth





# 2. train the model  (c stands for compound [0...7X]
# pip install webcolors
# python train.py -c 0 -p birdview_vehicles --head_only True --lr 5e-3 --batch_size 32 --load_weights weights/efficientdet-d0.pth  --num_epochs 10 --save_interval 100

# to start
CUDA_VISIBLE_DEVICES=0 python train.py -c 0 -p COCO_OI --head_only False --lr 5e-3 --batch_size 32 --load_weights weights/efficientdet-d0.pth  --num_epochs 16 --save_interval 500

# to resume
#CUDA_VISIBLE_DEVICES=0 python train.py -c 0 -p COCO_OI --head_only False --lr 1e-3 --batch_size 32 --load_weights last  --num_epochs 16 --save_interval 100






# 3. evaluation
#get latest weight file
# %cd logs/birdview_vehicles
# weight_file = !ls -Art | grep efficientdet
# %cd ../..

#uncomment the next line to specify a weight file
#weight_file[-1] = 'efficientdet-d0_49_1400.pth'

# python coco_eval.py -c 0 -p birdview_vehicles -w "logs/birdview_vehicles/{weight_file[-1]}"

weight_file='last.pth'
python coco_eval.py -c 0 -p COCO_OI -w "logs/COCO_OI/$weight_file"
