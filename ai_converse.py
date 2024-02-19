import requests
import json
import pyttsx3
from threading import Thread

class TTSBuffer:
    def __init__(self) -> None:
        self.buffer = []

        self.tts_thread = Thread(target=self.run).start()

    def run(self):
        while True:
            if len(self.buffer) > 0:
                message = self.buffer.pop(0)
                print(f"TTS: {message}")

                try:
                  response = requests.get("http://localhost:5000", params={"message": message})
                except:
                  pass

                #if response.status_code == 200:
                    #print("Message sent successfully!")
                #else:
                    #print(f"Failed to send message. Status code: {response.status_code}")
                

    def add(self, message):
        self.buffer.append(message)

tts = TTSBuffer()

parameters = {
  "messages": [
    {
      "content": "You are here chatting with a person. Your name is Unknown and you are an AI capable of having conversations with people. You are designed to respond like a real human would.",
      "role": "system"
    },
    {
      "content": "Hello!",
      "role": "user"
    }
  ],
  "model": "mistral-ins-7b-q4",
  "stream": True,
  "max_tokens": 256,
  "stop": [
    "hello"
  ],
  "frequency_penalty": 0,
  "presence_penalty": 1,
  "temperature": 0.7,
  "top_p": 0.95
}

while True:
    inmsg = input("\n>")
    parameters['messages'][1]['content'] = inmsg

    response = requests.post("http://localhost:1337/v1/chat/completions", json=parameters)
    data = response.text

    #data = b'data: {"choices":[{"delta":{"content":" Hey"},"finish_reason":null,"index":0}],"created":1708266890,"id":"4GJ5EBBeomE2ct2jR1Aj","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" there"},"finish_reason":null,"index":0}],"created":1708266890,"id":"6pZzqkZno4Yox9RSFx8r","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":"!"},"finish_reason":null,"index":0}],"created":1708266890,"id":"c3Zod56DyaDvSR5P1tvy","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" How"},"finish_reason":null,"index":0}],"created":1708266890,"id":"GlJtB5dmc8iYaVipZSKw","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" can"},"finish_reason":null,"index":0}],"created":1708266890,"id":"Ea5fGJSGYLOMLVJiBvSy","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" I"},"finish_reason":null,"index":0}],"created":1708266890,"id":"Q1Qf98LB1Ipf2wksJcpW","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" help"},"finish_reason":null,"index":0}],"created":1708266890,"id":"PagUfRvLbALUER44cOvi","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" you"},"finish_reason":null,"index":0}],"created":1708266890,"id":"HuAElPfb17ikrXjeRztZ","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" today"},"finish_reason":null,"index":0}],"created":1708266890,"id":"4YTz3JeGvh7w5ChlYsuq","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":"?"},"finish_reason":null,"index":0}],"created":1708266890,"id":"jTinWNiXxdtFG7uC5rN2","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" I"},"finish_reason":null,"index":0}],"created":1708266890,"id":"FJc949lYSi0mJFdtL28Q","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":"\'"},"finish_reason":null,"index":0}],"created":1708266890,"id":"X6QWFGortzKLmwn46QBZ","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":"m"},"finish_reason":null,"index":0}],"created":1708266891,"id":"lDiXQVdOJX3KANtXwE6S","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" here"},"finish_reason":null,"index":0}],"created":1708266891,"id":"zuFICFvYYKPz9VyWxnR9","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" to"},"finish_reason":null,"index":0}],"created":1708266891,"id":"fdbv5R6brmlxJyIhCY7j","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" make"},"finish_reason":null,"index":0}],"created":1708266891,"id":"rtT84I27gmsNcYIteXuX","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" your"},"finish_reason":null,"index":0}],"created":1708266891,"id":"gVR7DlaoWJAnSspihvzG","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" day"},"finish_reason":null,"index":0}],"created":1708266891,"id":"BArsJCLmzHAeRFYC9KD5","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" a"},"finish_reason":null,"index":0}],"created":1708266891,"id":"iCw4vGv7Zg9RKk63iJNm","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" little"},"finish_reason":null,"index":0}],"created":1708266891,"id":"5pQN0K1bmZ2Bs9ZsME7j","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" br"},"finish_reason":null,"index":0}],"created":1708266891,"id":"FaqLiNuhhkaGxgDhm1OU","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":"ighter"},"finish_reason":null,"index":0}],"created":1708266891,"id":"a2hMmouzbyH0vqs8zZtP","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":""},"finish_reason":null,"index":0}],"created":1708266891,"id":"EyEmCAMVSuQPjVoUg0MC","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" with short"},"finish_reason":null,"index":0}],"created":1708266891,"id":"sFaA6jJcjV07ZSfvNeh3","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" and"},"finish_reason":null,"index":0}],"created":1708266891,"id":"Kjo2gpbpfHjxr4lKZKod","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" casual"},"finish_reason":null,"index":0}],"created":1708266891,"id":"LHXuyJ1R9nv2Xy5J38QJ","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" responses"},"finish_reason":null,"index":0}],"created":1708266891,"id":"Av7reNeGyRdyBsXNAKi5","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":"."},"finish_reason":null,"index":0}],"created":1708266891,"id":"jvSbDl6J44jxEbEKZUPE","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" Feel"},"finish_reason":null,"index":0}],"created":1708266891,"id":"qzQ2S9g0MFKkjZC02oaD","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" free"},"finish_reason":null,"index":0}],"created":1708266891,"id":"IOF1GDPT7Tr846VvRZAL","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" to"},"finish_reason":null,"index":0}],"created":1708266891,"id":"e1qOsRGVJ2BCAL5BI5cZ","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" ask"},"finish_reason":null,"index":0}],"created":1708266891,"id":"02OOnzEJDoOF5T3EJrx7","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" me"},"finish_reason":null,"index":0}],"created":1708266891,"id":"Y0spqvIIcunMpsMgnBIa","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" anything"},"finish_reason":null,"index":0}],"created":1708266891,"id":"W4j4rOwPlbgWVguqdMYo","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":","},"finish_reason":null,"index":0}],"created":1708266891,"id":"xlpOf9miKxOhfFRov79E","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" from"},"finish_reason":null,"index":0}],"created":1708266891,"id":"r7NjdzlLuaqV7YY5BWRD","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":""},"finish_reason":null,"index":0}],"created":1708266891,"id":"vWxElxrLTvBhXhdfbaW0","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" the weather"},"finish_reason":null,"index":0}],"created":1708266891,"id":"H04iq3YtOMmi5lYVioGM","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" to"},"finish_reason":null,"index":0}],"created":1708266891,"id":"QnzdqF9E4llrT5wjNuTQ","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" a"},"finish_reason":null,"index":0}],"created":1708266891,"id":"1C4fAlxckfaprbAuREss","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" funny"},"finish_reason":null,"index":0}],"created":1708266891,"id":"sPahHtKcPSJRuyyEDT0e","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" joke"},"finish_reason":null,"index":0}],"created":1708266891,"id":"bFjkbHrpkQUhxf4rW2To","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":"!"},"finish_reason":null,"index":0}],"created":1708266891,"id":"erWl2pq1vqLrQd0FzsZN","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":" :"},"finish_reason":null,"index":0}],"created":1708266891,"id":"rwTULAvJ1ZvHVpbmDJMS","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":"D"},"finish_reason":null,"index":0}],"created":1708266891,"id":"dKJEULVngaLHGBUqYzAr","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":""},"finish_reason":null,"index":0}],"created":1708266891,"id":"DQSpIA9IZIh9mdLj7zTp","model":"_","object":"chat.completion.chunk"}\n\ndata: {"choices":[{"delta":{"content":""},"finish_reason":"stop","index":0}],"created":1708266891,"id":"ClMrukuwA0qjGVYMq5LR","model":"_","object":"chat.completion.chunk"}\n\ndata: [DONE]\n\n'
    data = data.replace('data: ', '')
    datarray = data.split('\n\n')

    # Remove empty elements using list comprehension
    split_list = [item.strip() for item in datarray if item.strip()]

    constructed = []
    for item in split_list:
        try:
            data = json.loads(item)
            constructed.append(data)
        except:
            #print(f"could not parse: {item}")
            pass

    message = ""
    for data in constructed:
        message += (str(data['choices'][0]['delta']['content']))

    print(message, "\n")
    #engine.say(message)
    #engine.runAndWait()
    tts.add(message)
