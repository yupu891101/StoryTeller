from web_ui.Tab1 import Tab1
from web_ui.Tab2 import Tab2
from web_ui.Tab3 import Tab3
import gradio as gr
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def main():
    tab1 = Tab1()
    tab2 = Tab2()
    tab3 = Tab3()

    StarRail = [
        ("Himeko", r"../StarRail/himeko/model_300000.pt"),
        ("rachG", r"../StarRail/rachG/model_300000.pt")
    ]

    with gr.Blocks(theme = 'xiaobaiyuan/theme_brief', title="StoryTeller") as story:
        gr.Markdown("# Storyteller's Voice Studio: Create and Clone")
        gr.Markdown("### Made by Yu-Pu Hsu, Yu-Han Tseng, Hsueh-Fu Shih\n---")
        gr.Markdown("""
        <div style='text-align: center;'>
            <h1 style='margin-bottom: 0.5rem;'>StoryTeller: Voice Studio - Create and Clone</h1>
            <h5 style='margin-top: 0.5rem;'>Made by Yu-Pu Hsu, Yu-Han Tseng, Hsueh-Fu Shih</h5>
        </div>
        """)
        
        gr.Markdown("### Let's choose a story!")
        
        with gr.Row():
            story_radio = gr.Radio(choices=["Little-Red-Riding-Hood", "The-Three-Little-Pigs", "Sleeping-Beauty", "The-Little-Match-Girl", "The-Ugly-Duckling"], container=False)
        with gr.Row():
            story_img = gr.Image("picture/pic.jpg", show_download_button=False, label=" ")
            with gr.Column():
                story_content = gr.Text(label="Story Content", placeholder="Select a story to see contents.")
                story_audio = gr.Audio(autoplay=True, label=" ")
                story_radio.change(fn=tab1.play_audio, inputs=story_radio, outputs=[story_img, story_content, story_audio])
            
        gr.Markdown("### Build your own text-to-speech story!")
        # Tab 1
        with gr.Tab("Customized Story"):
            with gr.Row():
                gr.Markdown("""
                Here is a list of non-speech sounds you can include in your story: 
                `[laughter]`, `[laughs]`, `[sighs]`, `[music]`, `[gasps]`, and `[clears throat]`. 
                Use an em dash (`—`) or ellipsis (`...`) to indicate hesitations, 
                a musical note (`♪`) to denote song lyrics, 
                and CAPITALIZATION when you want to emphasize a word.
                """)
            with gr.Row():
                text_input = gr.Textbox(label="Enter story content", info="Example: [clears throat] Once upon a time, there was a lovely princess.")
                with gr.Column():
                    gender_radio = gr.Radio(label="Select Gender", choices=["Male", "Female"])
                    speaker_select = gr.Dropdown(label="Select Speaker", allow_custom_value=True, info="Note: The input language must be consistent with the speaker’s language.")
                    gender_radio.change(fn=tab1.update_speaker_dropdown, inputs=gender_radio, outputs=speaker_select)
                    with gr.Row():
                        submit_button = gr.Button("Text to speech")
                        clear_button = gr.Button("Clear")
                    warning_text = gr.Text(label="Result")
            with gr.Row():
                audio_output = gr.Audio(label="Generated Audio", type="filepath")
            
            clear_button.click(
                fn=tab1.clear_tab1,
                outputs=[text_input, gender_radio, speaker_select]
            )
            submit_button.click(
                fn=tab1.text_to_speech,
                inputs=[text_input, speaker_select],
                outputs=[audio_output, warning_text]
            )

        # Tab 2
        with gr.Tab("Tell Story with Different Voices"):
            with gr.Row():
                with gr.Column(scale=1):
                    star_rail_pt = gr.Dropdown(label="Speakers from Star Rail !", choices=StarRail)
                    input_pt = gr.FileExplorer(label="Your voice's checkpoint file ", root_dir="./DDSP-SVC/exp", glob="**/*.pt*")
                with gr.Column(scale=2):
                    with gr.Row():
                        input_wav = gr.File(label="Choose the audio file")
                        audio = gr.Audio(label="Play the audio file")
                    input_wav.upload(fn=tab2.audio_file, inputs=input_wav, outputs=audio)
                    with gr.Row():
                        keychange = gr.Slider(label="Pitch", minimum=-20, maximum=20, step=1, value=0)
                        speedup = gr.Slider(label="Speedup", minimum=-10, maximum=10, step=1, value=1)
                    output_wav = gr.Textbox(label="Output file name", value="output.wav")
                    with gr.Row():
                        run_button = gr.Button("Start converting sounds")
                        clear_button2 = gr.Button("Refresh")
                    run_output = gr.Text(label="Result")
                    output_audio = gr.Audio()

            clear_button2.click(
                fn=tab2.clear_tab2,
                outputs=[star_rail_pt, input_pt, input_wav, audio, keychange, speedup, output_wav]
            )
            run_button.click(
                tab2.change_voice,
                inputs=[star_rail_pt, input_wav, input_pt, keychange, output_wav, speedup],
                outputs=[run_output, output_audio]
            )
            
        # Tab 3
        with gr.Tab("Clone Your Voice"):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("Each wav file takes more than 2 seconds, and it is recommended to upload 20 files.")
                    input_wav = gr.File(label="Upload audio file to train", file_count="multiple")
                with gr.Column():
                    dir_path = gr.Text(label="Your voice's name ")
                    epoch = gr.Number(label="Epoch", value=2500, interactive=True)
                    with gr.Row():
                        learn = gr.Button("Learn your voice")
                        stop_button = gr.Button("Stop learning")
                    run_output = gr.Text(label="Result")

            learn.click(
                tab3.learn_voice,
                inputs=[input_wav, dir_path,epoch],
                outputs=run_output
            )
            stop_button.click(tab3.stop_training)

    story.launch(share=True)

if __name__ == "__main__":
    main()