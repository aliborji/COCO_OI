# Object Detection with COCO_OI and ObjectNet_D

This repository provides an implementation for object detection using two complementary datasets to COCO: **COCO_OI** and **ObjectNet_D**. These datasets can help to improve object detection performance by overcoming the limitations of COCO dataset saturation.

## Getting Started

To get started with the environment and dependencies, follow these steps:

### 1. Create a Conda Environment

Create a new Conda environment with Python 3.7:

```bash
conda create -n objDet python=3.7
```

### 2. Activate the Conda Environment

Activate the newly created environment:

```bash
conda activate objDet
```

### 3. Install Dependencies

Install the necessary Python packages using pip:

```bash
pip install pycocotools numpy==1.16.0 opencv-python tqdm tensorboard tensorboardX pyyaml webcolors matplotlib torch==1.4.0 torchvision==0.5.0 boto3
```

## Citation

If you use this repository or datasets in your research, please cite the following paper:

```
@article{borji2022complementary,
  title={Complementary datasets to COCO for object detection},
  author={Borji, Ali},
  journal={arXiv preprint arXiv:2206.11473},
  year={2022}
}
```

## Datasets

### 1. **COCO_OI**

COCO_OI is a large dataset composed of images from **COCO** and **OpenImages**. It includes images from their 80 common classes, and it features:

- **1,418,978** training bounding boxes over **380,111** images.
- **41,893** validation bounding boxes over **18,299** images.

### 2. **ObjectNet_D**

ObjectNet_D consists of images depicting objects in daily life situations. It is originally created for object recognition tasks known as **ObjectNet**, and contains:

- 29 common categories with **COCO**.

This dataset is useful for testing the generalization ability of object detection models, especially when objects are placed in challenging and varied real-life settings.

## Evaluations

This repository includes an evaluation of object detection models on these datasets. Through this evaluation, we aim to pinpoint the sources of errors and help improve the accuracy and robustness of object detection systems.

## Usage

You can use this repository to train and test object detection models on **COCO_OI** and **ObjectNet_D** datasets. For more details on how to use these datasets, please refer to the code and data available at the following link:

[https://github.com/aliborji/COCO_OI](https://github.com/aliborji/COCO_OI)

---

Feel free to explore and contribute to the repository! If you have any questions or issues, don't hesitate to open an issue or reach out.


