import gradio as gr
import subprocess
import os

class Tab2():
    def __init__(self):
        pass

    def audio_file(self, input_wav):
        return input_wav

    def clear_tab2(self):
        return "", "", None, None, 0, 1, "output.wav"

    def change_voice(self, star_rail_pt, input_wav, input_pt, keychange, output_wav, speedup):
        if not input_pt:
            pt = star_rail_pt
        elif not star_rail_pt:
            pt = input_pt[0]
        else:
            pt = input_pt[0]
            gr.Info("You have selected both StarRail and DDSP-SVC. We will use DDSP-SVC to change the voice.")
        
        if input_wav.split(".")[-1] != "wav":
            error_message = "Please upload a .wav file."
            gr.Warning(error_message)
        
        if not os.path.exists("result"):
            os.makedirs("result")

        print("input_wav:", input_wav, "input_pt:", pt, "star_rail_pt:", star_rail_pt, "keychange:", keychange, "output_wav:", output_wav, "speedup:", speedup)
        
        output_path = f"result/{output_wav}"
        command = f"python main_diff.py -i {input_wav} -diff {pt} -o ../{output_path} -k {keychange} -speedup {speedup} -method 'dpm-solver' -kstep 100"
        process = subprocess.run(command, shell=True, text=True, capture_output=True, cwd=r"./DDSP-SVC")

        print("Standard Output:", process.stdout)
        print("Error Output:", process.stderr)

        if process.returncode != 0:
            error_message = f"Error: The subprocess returned a non-zero exit code: {process.returncode}"
            print(error_message)
            return error_message, None
        print(process.stdout)
        result = "Successfully changed voice!"
        
        
        return result, output_path