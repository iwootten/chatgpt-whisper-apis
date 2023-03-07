import openai
import subprocess
import os
import gradio

openai.api_key = os.getenv("OPENAI_SECRET_KEY")

messages = [{"role": "system", "content": "You are a helpful assistant"}]


def chat(audio_file):
    global messages
    transcription = openai.Audio.transcribe("whisper-1", open(audio_file, "rb"))
    messages.append({"role": "user", "content": transcription["text"]})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    print(transcription)
    return completion["choices"][0]["message"]["content"]


demo = gradio.Interface(
    fn=chat, inputs=gradio.Audio(source="microphone", type="filepath"), outputs="label"
)
demo.launch()
