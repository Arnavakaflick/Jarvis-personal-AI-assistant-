import speech_recognition as sr
import os
import openai
print(openai.__version__)
import sys

print(sys.version)

from openai import OpenAI

apikey = "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"
os.environ["OPENAI_API_KEY"] = apikey
client = OpenAI(api_key=apikey)
from config import apikey
import datetime
import webbrowser

chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"Arnav: {query}\n Jarvis: "


    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[

            {"role": "user", "content": chatStr}
        ]
    )

    say(response.choices[0].message.content)
    chatStr += f"{response.choices[0].message.content}\n"
    return response.choices[0].message


    say(response.choices[0].message.content)
    chatStr += f"{response.choices[0].message.content}\n"
    return response.choices[0].message.content


    # todo: Wrap this inside of a  try catch block
    say(response.choices[0].text)
    chatStr += f"{response.choices[0].text}\n"
    return response.choices[0].text


def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[

            {"role": "user", "content": prompt}
        ]
    )


    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response.choices[0].text
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    os.system(f'say "{text}"')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('pycharm')
    say("hello I am Jarvis A.I")
    while True:
        print("listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["The knowledge society", "https://www.tks.world"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir..")
                webbrowser.open(site[1])
        if "open music" in query:
            musicPath = "/Users/arzflicky/Downloads/dance-like-crazy-136338.mp3"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            musicPath = "/Users/arzflicky/Downloads/dance-like-crazy-136338.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} : {min} minutes")

        elif "open spotify".lower() in query.lower():
            os.system(f"open /Applications/Spotify.app")

        elif "open Discord".lower() in query.lower():
            os.system(f"open /Applications/Discord.app ")

        elif "open Whatsapp".lower() in query.lower():
            os.system(f"open /Applications/Xcode.app ")

        elif "open Python".lower() in query.lower():
            os.system(f"open /Applications/Python 3.11 ")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
