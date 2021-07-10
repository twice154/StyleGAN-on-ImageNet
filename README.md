## StyleGAN-on-ImageNet

## Requirements

This repository starts from <a href="https://github.com/NVlabs/stylegan2-ada-pytorch">StyleGAN-ADA Official PyTorch Code</a>, and requirements are exactly same.

## Overview

## Preparing ImageNet-10-128x128

You can make **ImageNet-10-128x128**, by
* randomly select 10 classes from ImageNet.
* follow custom dataset creation guide from <a href="https://github.com/NVlabs/stylegan2-ada-pytorch">StyleGAN-ADA Official PyTorch Code</a> to make conditional image generation dataset of 128x128 images.

## Training on ImageNet-10-128x128

```.bash
# If you have GPU memory issue, please change evaluation metric to fid5k.
python train.py --outdir=./training-runs --data=/path/to/ImageNet-10-128x128 --gpus=#ofGPUs --cfg=auto --aug=ada --metrics=fid50k --kimg=100000 --cond=True
```

## Results on ImageNet-10-128x128

## License

Copyright &copy; 2021, NVIDIA Corporation. All rights reserved.

This work is made available under the [Nvidia Source Code License](https://nvlabs.github.io/stylegan2-ada-pytorch/license.html).

## Citation

```
@inproceedings{Karras2020ada,
  title     = {Training Generative Adversarial Networks with Limited Data},
  author    = {Tero Karras and Miika Aittala and Janne Hellsten and Samuli Laine and Jaakko Lehtinen and Timo Aila},
  booktitle = {Proc. NeurIPS},
  year      = {2020}
}
```
