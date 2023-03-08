# chatgpt-whisper-apis

A collection of example scripts for using the OpenAI ChatGPT and Whisper APIs. Each one is under 35 lines.


# Installation

Make sure you have rust and ffmpeg to be able to use the gradio examples. On a Mac, you can install with brew.

```sh
brew install rust
brew install ffmpeg
```

Install the dependencies from the Pipfile, or install openai and gradio with your package manager of choice.

```sh
pipenv install
```

# Description

- intro.py - the default OpenAI example.
- chat.py - A simple CLI using input()
- chat2.py - Recording mic input using a gradio webapp
- chat3.py - Recording mic input using gradio and responding using say()