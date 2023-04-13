Enhanced version of Cross-modality Knowledge Reasoning model.<br>
CKR-PLUS
====
<br>
In this work, I modified several loopholes in the CKR model, strengthened the performance of the CKR model in all aspects, and further proved the importance of room relations in the REVERIE task. Specifically, Success Rate (SR) increased from 18.49% to 31.33%, and Success rate weighted Path Length (SPL),normalizing the success rate with trajectory length, increased from 10.82% to 24.75% in val-unseen.
<br>

Environment Installation
===

<br>
1.Clone this repository.
<br>
<br>

```
git clone https://github.com/alloldman/CKR.git $CKR-root
```
<br>
2.Install pytorch==1.7.1
<br>
<br>

```
# CUDA 11.0
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.0 -c pytorch
# PIP 11.0
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```
<br>
3.Install the requirements.
<br>
<br>

```
pip install -r requirements.txt
```
<br>

Dataset Preparation
=====

<br>

1.Download the Intermediate data from [here](https://drive.google.com/drive/folders/1lU6k8DNXThdWXOafHoXC-3UjwCArT84h?usp=sharing "点击跳转"). data.zip, KB/cache.zip, img_features.zip, experiments/best-ckpt.zip should be unziped. And the [KB/data](https://drive.google.com/file/d/1B4IWXISA_D7avHoj6tHsfMtu5kuIqpt6/view "点击跳转") should be download and be unziped under the KB folder which contains external knowledge bases.

<br>
2.Put these unziped files as the order below:
<br>

> Room-knowledge-inference-model-plus
>> img_features

>> data

>> KB
>>> cache

>>> data

>> experiments
>>> best-ckpt
>>>> plots
