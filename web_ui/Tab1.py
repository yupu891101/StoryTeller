from bark.generation import generate_text_semantic, preload_models
from bark.api import semantic_to_waveform
from bark import SAMPLE_RATE
import soundfile as sf
import gradio as gr
import numpy as np
import nltk
import os

class Tab1():
    def __init__(self):
        preload_models()

        self.male_speakers = [
            ("English", "v2/en_speaker_6"),
            ("German", "v2/de_speaker_6"),
            ("Italian", "v2/it_speaker_4"),
            ("Korean", "v2/ko_speaker_9"),
            ("Japanese", "v2/ja_speaker_2"),
            ("Chinese", "v2/zh_speaker_8"),
        ]
        self.female_speakers = [
            ("English", "v2/en_speaker_9"),
            ("German", "v2/de_speaker_3"),
            ("Italian", "v2/it_speaker_9"),
            ("Korean", "v2/ko_speaker_0"),
            ("Japanese", "v2/ja_speaker_3"),
            ("Chinese", "v2/zh_speaker_9"),
        ]

    def play_audio(self, story_name):
        if story_name == "Little-Red-Riding-Hood":
            with open("story_template/Little-Red-Riding-Hood.txt", 'r', encoding='utf-8') as file:
                story = file.read()
            return "picture/Little-Red-Riding-Hood.png", story, "story_template/English9_[]_Little-Red-Riding-Hood.wav"
        elif story_name == "The-Three-Little-Pigs":
            with open("story_template/The-Three-Little-Pigs.txt", 'r', encoding='utf-8') as file:
                story = file.read()
            return "picture/The-Three-Little-Pigs.png", story, "story_template/English9_[]_The-Three-Little-Pigs.wav"
        elif story_name == "Sleeping-Beauty":
            with open("story_template/Sleeping-Beauty.txt", 'r', encoding='utf-8') as file:
                story = file.read()
            return "picture/Sleeping-Beauty.png", story, "story_template/English9_[]_Sleeping-Beauty.wav"
        elif story_name == "The-Little-Match-Girl":
            with open("story_template/The-Little-Match-Girl.txt", 'r', encoding='utf-8') as file:
                story = file.read()
            return "picture/The-Little-Match-Girl.png", story, "story_template/English9_[]_The-Little-Match-Girl.wav"
        elif story_name == "The-Ugly-Duckling":
            with open("story_template/The-Ugly-Duckling.txt", 'r', encoding='utf-8') as file:
                story = file.read()
            return "picture/The-Ugly-Duckling.png", story, "story_template/English9_[]_The-Ugly-Duckling.wav"

    def update_speaker_dropdown(self, gender):
        if gender == "Male":
            result = self.male_speakers
        elif gender == "Female":
            result = self.female_speakers
        else:
            result = None
        return gr.update(choices=result)

    def clear_tab1(self):
        return "", None, ""

    def text_to_speech(self, script, speaker):
        if not script or not speaker:
            warning_msg = "Please "
            warning_msg += "enter story content" if not script else ""
            warning_msg += " and " if not script and not speaker else ""
            warning_msg += "select a speaker" if not speaker else ""
            warning_msg += "."
            return None, warning_msg
        else:
            result = "Successfully converted text to speech!"
            sentences = nltk.sent_tokenize(script)
            GEN_TEMP = 0.6
            silence = np.zeros(int(0.25 * SAMPLE_RATE))

            pieces = []
            for sentence in sentences:
                semantic_tokens = generate_text_semantic(
                    sentence,
                    history_prompt=speaker,
                    temp=GEN_TEMP,
                    min_eos_p=0.05,
                )

                audio_array = semantic_to_waveform(semantic_tokens, history_prompt=speaker)
                pieces += [audio_array, silence.copy()]

            combined_audio = np.concatenate(pieces, axis=0)

            if not os.path.exists("result"):
                os.makedirs("result")
            output_path = 'result/generated_audio.wav'
            sf.write(output_path, combined_audio, SAMPLE_RATE)
            return output_path, result