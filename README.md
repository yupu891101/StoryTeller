# StoryTeller

This project requires Python 3.10. Please ensure you have the correct version installed before proceeding.

## Installation

First, navigate to the project directory and install the required dependencies:

```bash
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

1. 下載[model0.pt](https://github.com/yxlllc/DDSP-SVC/releases/download/5.0/model_0.pt)並放在 DDSP-SVC 資料夾底下。
2. Download the pre-trained [RMVPE](https://github.com/yxlllc/RMVPE/releases/download/230917/rmvpe.zip) extractor and unzip it into pretrain/rmvpe folder.
3. Download and unzip the pre-trained [NSF-HiFiGAN](https://github.com/openvpi/vocoders/releases/download/nsf-hifigan-44.1k-hop512-128bin-2024.02/nsf_hifigan_44.1k_hop512_128bin_2024.02.zip) vocoder
4. Download the pre-trained [ContentVec](https://ibm.ent.box.com/s/z1wgl1stco8ffooyatzdwsqn2psd9lrr) encoder and put it under pretrain/contentvec folder.
