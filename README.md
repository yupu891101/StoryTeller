# StoryTeller

This project has been tested with Python version 3.10.

## Installation

First, clone the repository and navigate to the project directory, then install the required dependencies:

```bash
git clone https://github.com/yupu891101/StoryTeller.git
cd StoryTeller
pip install -r requirements.txt
```

Next, you need to install and import the `nltk` library, then download the necessary resource packages:

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
```

Finally, install [DDSP-SVC](https://github.com/yxlllc/DDSP-SVC) to enable the voice synthesis functionality.

```bash
git clone https://github.com/yxlllc/DDSP-SVC.git
cd DDSP-SVC
pip install -r requirements.txt
```

> 1. Download the [model0.pt](https://github.com/yxlllc/DDSP-SVC/releases/download/5.0/model_0.pt) and place it into the `exp` folder within the DDSP-SVC directory.
> 2. Download the pre-trained [RMVPE](https://github.com/yxlllc/RMVPE/releases/download/230917/rmvpe.zip) extractor, unzip it, and place the contents into the `pretrain/rmvpe` folder within the DDSP-SVC directory.
> 3. Download the pre-trained [NSF-HiFiGAN](https://github.com/openvpi/vocoders/releases/download/nsf-hifigan-44.1k-hop512-128bin-2024.02/nsf_hifigan_44.1k_hop512_128bin_2024.02.zip) vocoder, unzip it, and place the contents into the `pretrain/nsf_hifigan` folder within the DDSP-SVC directory.
> 4. Download the pre-trained [ContentVec](https://ibm.ent.box.com/s/z1wgl1stco8ffooyatzdwsqn2psd9lrr) encoder and place it into the `pretrain/contentvec` folder within the DDSP-SVC directory.
> 5. Modify the configuration file in the `DDSP-SVC/configs` directory. The StoryTeller project uses `diffusion-fast.yaml` by default, so you need to update the `ckpt` path for the vocoder in this file to point to `pretrain/nsf_hifigan/model.ckpt`.

DDSP-SVC/     
├── configs/      
│   ├── diffusion-fast.yaml   
│   └── ...   
├── exp/      
│   └── model_0.pt    
├── pretrain/     
│   ├── rmvpe/    
│   │   └── model.pt      
│   ├── nsf_hifigan/      
│   │   ├── config.json   
│   │   ├── model.ckpt    
│   │   ├── NOTICE.txt    
│   │   └── NOTICE.zh-CN.txt      
│   └── contentvec/   
│       └── checkpoint_best_legacy_500.pt     
└── scripts/      
    ├── preprocess.py     
    └── train_diff.py     

