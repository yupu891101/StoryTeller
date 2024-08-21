# StoryTeller

This project has been tested with Python version 3.10.

## Installation

1. **Clone the Repository and Install Dependencies:**

    First, clone the repository and navigate to the project directory, then install the required dependencies:

    ```bash
    git clone https://github.com/yupu891101/StoryTeller.git
    cd StoryTeller
    pip install -r requirements.txt
    ```

2. **Install nltk and Download Necessary Resources:**

    Next, install and import the `nltk` library, then download the required resource packages:

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('punkt_tab')
    ```

3. **Install DDSP-SVC for Voice Synthesis:**

    Finally, clone the [DDSP-SVC](https://github.com/yxlllc/DDSP-SVC) repository and install its dependencies:

    ```bash
    git clone https://github.com/yxlllc/DDSP-SVC.git
    cd DDSP-SVC
    pip install pip==24.0  # Ensure pip is downgraded to avoid compatibility issues
    pip install -r requirements.txt
    ```
    > [NOTE]
    > Some packages listed in requirements.txt require pip version <24.1. Therefore, it's necessary to first downgrade pip to version 24.0 before installing the dependencies.

4. **Download Pre-trained DDSP-SVC Model Weights:**

   Download the pre-trained DDSP-SVC model [weights](https://drive.google.com/drive/u/0/folders/1DTx-_t5hh9bXSm_Va0xKCmMnQotQtCQD) and place them into the respective folders within the `StarRail` directory.

5. **Download and Set Up Additional Models:**

   - **Model 0:** Download the [model_0.pt](https://github.com/yxlllc/DDSP-SVC/releases/download/5.0/model_0.pt) file and place it into the `exp` folder within the DDSP-SVC directory.
   - **RMVPE Extractor:** Download the pre-trained [RMVPE](https://github.com/yxlllc/RMVPE/releases/download/230917/rmvpe.zip) extractor, unzip it, and place the contents into the `pretrain/rmvpe` folder within the DDSP-SVC directory.
   - **NSF-HiFiGAN Vocoder:** Download the pre-trained [NSF-HiFiGAN](https://github.com/openvpi/vocoders/releases/download/nsf-hifigan-44.1k-hop512-128bin-2024.02/nsf_hifigan_44.1k_hop512_128bin_2024.02.zip) vocoder, unzip it, and place the contents into the `pretrain/nsf_hifigan/model` folder within the DDSP-SVC directory.
   - **ContentVec Encoder:** Download the pre-trained [ContentVec](https://ibm.ent.box.com/s/z1wgl1stco8ffooyatzdwsqn2psd9lrr) encoder and place it into the `pretrain/contentvec` folder within the DDSP-SVC directory.

6. **Modify Configuration Files:**

   Update the `diffusion-fast.yaml` configuration file in the `DDSP-SVC/configs` directory. Specifically, you need to modify the `ckpt` path for the vocoder to point to `pretrain/nsf_hifigan/model/model.ckpt`.

### Directory Structure

The directory structure of the `DDSP-SVC` folder should look like this:

```markdown
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
│   │   └── model/
│   │       ├── config.json 
│   │       ├── model.ckpt  
│   │       ├── NOTICE.txt  
│   │       └── NOTICE.zh-CN.txt    
│   └── contentvec/ 
│       └── checkpoint_best_legacy_500.pt   
└── scripts/    
    ├── preprocess.py   
    └── train_diff.py   
```

## Running the Project

To run the project, simply execute the following command in the terminal:

```bash
python launch.py
```
