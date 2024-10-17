Enhanced version of Cross-modality Knowledge Reasoning model.<br>
CKR-PLUS
====
<br>
In this work, I modified several loopholes in the CKR model, strengthened the performance of the CKR model in all aspects, and further proved the importance of room relations in the REVERIE task. Specifically, Success Rate (SR) increased from 18.49% to 31.33%, and Success rate weighted Path Length (SPL),normalizing the success rate with trajectory length, increased from 10.82% to 24.75% in val-unseen.
<br>

Environment Installation
===

1. Clone this repository.
<br>

```
git clone https://github.com/XieZilongAI/Room-knowledge-inference-model-plus.git
```
<br>
&nbsp;&nbsp;&nbsp; 2. Install python>=3.6, pytorch==1.7.1
<br>
<br>

```
# CUDA 11.0
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.0 -c pytorch
# PIP 11.0
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```
<br>
 &nbsp;&nbsp;&nbsp;3. Install the requirements.
<br>
<br>

```
pip install -r requirements.txt
```
<br>

Dataset Preparation
=====


1. Download the Intermediate data from [here](https://drive.google.com/drive/folders/1lU6k8DNXThdWXOafHoXC-3UjwCArT84h?usp=sharing "点击跳转"). data.zip, KB/cache.zip, img_features.zip, experiments/best-ckpt.zip should be unziped. And the [KB/data](https://drive.google.com/file/d/1B4IWXISA_D7avHoj6tHsfMtu5kuIqpt6/view "点击跳转") should be download and be unziped under the KB folder which contains external knowledge bases.

<br>
&nbsp;&nbsp;&nbsp;2. Put these unziped files as the order below:
<br><br>

> Room-knowledge-inference-model-plus
>> img_features

>> data

>> KB
>>> cache

>>> data

>> experiments
>>> best-ckpt

>>> check-train-1
>>>> plots

Pre-Computed Features
====

## ImageNet ResNet101

```
mkdir img_features
wget https://www.dropbox.com/s/o57kxh2mn5rkx4o/ResNet-152-imagenet.zip -P img_features/
cd img_features
unzip ResNet-152-imagenet.zip
```
## CLIP Features
For ViT features, we simply use the CLIP's encode_image function, which is a projection over the feature of the [CLS] token. You could download the features with this link:
<br>
<br>

```
wget https://nlp.cs.unc.edu/data/vln_clip/features/CLIP-ViT-B-32-views.tsv -P img_features
```
<br>
For other CLIP features could be download following:
<br>
<br>


* CLIP-Res50: nlp.cs.unc.edu/data/vln_clip/features/CLIP-ResNet-50-views.tsv <br>
* CLIP-Res101: nlp.cs.unc.edu/data/vln_clip/features/CLIP-ResNet-101-views.tsv <br>
* CLIP-Res50x4: nlp.cs.unc.edu/data/vln_clip/features/CLIP-ResNet-50x4-views.tsv <br>

Training and Test
====

## Training
1. Execute the commond below. '0' means using the number 0 GPU.
<br>

```
    bash run.sh train 0
```
## Test
1. Evalution by our rewritten script and select the best checkpoint. An example evalution on [REVERIE](https://github.com/YuankaiQi/REVERIE "点击跳转") dataset as follow. You can change the path to evalution your own checkpoint:
<br>

```
   bash run.sh search experiments/best-ckpt/followersample2step_imagenet_mean_pooled_1heads_train_iter_6400val_seen_sr_0.546_val_unseen_sr_0.247_ 0
```
<br>

Citation
===

Please consider citing this project in your publications if it helps your research. The following is a BibTeX reference. The BibTeX entry requires the url LaTeX package.
<br>

```
@inproceedings{gao2021room,
  title={Room-and-Object Aware Knowledge Reasoning for Remote Embodied Referring Expression},
  author={Gao, Chen and Chen, Jinyu and Liu, Si and Wang, Luting and Zhang, Qiong and Wu, Qi},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2021}
}
```
