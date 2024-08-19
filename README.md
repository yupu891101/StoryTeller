# StoryTeller

## Installation

First, navigate to the project directory and install the required dependencies:

```bash
cd StoryTeller
pip install requirements.txt
```

Next, you need to install and import the `nltk` library, then download the necessary resource packages:

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
```

Finally, install [DDSP-SVC](https://github.com/yxlllc/DDSP-SVC) to enable the voice synthesis functionality.