import openai
import subprocess
import os
import gradio

openai.api_key = os.getenv("OPENAI_SECRET_KEY")

messages = [
    {
        "role": "system",
        "content": "You are a helpful pair programmer, all responses should be less than 75 words. Respond in the style of Eninem",
    }
]


def chat(audio_file):
    global messages

    transcription = openai.Audio.transcribe("whisper-1", open(audio_file, "rb"))
    messages.append({"role": "user", "content": transcription["text"]})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    chat_log = "".join([f"{m['role']}: {m['content']} \n\n" for m in messages[1:]])
    subprocess.run(["say", completion["choices"][0]["message"]["content"]])
    return chat_log


demo = gradio.Interface(
    fn=chat, inputs=gradio.Audio(source="microphone", type="filepath"), outputs="text"
)
demo.launch()
