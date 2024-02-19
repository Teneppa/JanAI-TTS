# JanAI-TTS
A simple TTS program that connects to the API provided by JanAI Client

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
