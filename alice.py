#!/usr/bin/python
import requests
import json
from google_speech import Speech
import speech_recognition as sr 

r = sr.Recognizer()

def speak(alice_speech):
    lang = "en-us"
    speach=Speech(alice_speech, lang)
    speach.play()

# query="dodd you like to talk?"
def question(quest):
    
    #crafting the headers and removed unwanted headers
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
             # 'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://chai.ml/',
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'developer_uid': 'mUCsg14rQqYbpRkcqMbiPKa29xg1',
            'developer_key': 'sLdHjVjwMKd_7pd4C4l8S8yugfqq8caILaez7KJAmtKrZErnAOIVx_RoyOF6xRcAMvQ_yqlkxEWi87X0FIoaOg',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
    }
    
    #crafting json data                 
    json_data = {
            'text': 'Alice: Hi, my name is Alice. What is weighing on your mind?\nMe: hey\nAlice: Hi. I\'m a computer assistant of ravanan. How are you feeling?\nMe: i miss you\nAlice: Why do you say that you miss me ?\nMe: because i like you so much\nAlice: Is that the real reason?\nMe: i love you\nAlice: You love me. That\'s lovely to hear!\nMe: who are you?\nAlice: i am a computer assistant and a girl friend for ravanan\n###\nAlice: Hi, my name is Alice. What is weighing on your mind?\nMe: who are you?\nAlice: i am a personal assistant of ravanan\nMe:'+ quest +'\nAlice:',
            'temperature': 0.6,
            'repetition_penalty': 1.1,
            'top_p': 1,
            'top_k': 40,
            'response_length': 64,
    }
    response = requests.post('https://model-api-shdxwd54ta-nw.a.run.app/generate/gptj', headers=headers, json=json_data).text
    #print(response)
    
    #"""parsing the json data from the response which is from the server"""
    res=json.loads(response)
    lol = res["data"]
    speak(lol)

#created main for looping the query
def main():
    while(True):
        with sr.Microphone() as source:
            print("talk")
            audio_text = r.listen(source, phrase_time_limit=10)
            print("time over")
            try:
                question(r.recognize_google(audio_text, language="en-us"))
            except:
                speak("sorry cant understand!!")

        

if __name__ == "__main__":
    main()
 

