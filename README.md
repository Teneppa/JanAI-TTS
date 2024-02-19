# JanAI-TTS
A simple TTS program that connects to the API provided by [JanAI Client](https://github.com/janhq/jan)

### Dependencies
For pytorch & TTS compability, pytorch 2.1.0 seemed to work fine. https://pytorch.org/get-started/previous-versions/

**Windows 11 - CUDA 12.1**
```
pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu121 --user
```

TTS: https://github.com/coqui-ai/TTS

NOTE: Requires pytorch for the installation to complete
```
pip install TTS --user
```


### Usage
1) Enable local api from Jan by clicking the [<>] icon on the bottom left, selecting the right model and by pressing start server
2) Start ai_converse.py
3) To use the TTS, start up tts_receive_ai.py as well (optional)

NOTE: If you have something else running on port 5000 you might want to change it to something else!
