#Neccesary Import

import speech_recognition as sr
import os 
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

#handle warning
warnings.filterwarnings('ignore')

#record audio
def recordAudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Say')
        audio = r.listen(source,timeout=10, phrase_time_limit=10)

    data=''
    try:
        data=r.recognize_google(audio)
        print("You said: "+data)
    except sr.UnknownValueError:
        print("Unable To understand,Sorry!")
    except sr.RequestError as e:
        print('Request unable to connect'+e)
    return data


#text=recordAudio()
#response
def assistantResponse(text):
    print(text)
    #converting text to speech
    myobj=gTTS(text=text,lang='en',slow=False)
    #save this in mp3 file
    myobj.save('assistant_response.mp3')

    #PLay this file
    os.system('start assistant_response.mp3')

#text='this is a test'
#assistantResponse(text)


def wakeWord(text):
    wake_words=['hi','hey','hey computer','ok computer']
    text=text.lower()
    for i in wake_words:
        if i=='stop':
            exit()
        if i in text:
            return True
    return False


def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    monthNum=now.month
    dayNum=now.day

    month_name=['January','February','March','April','May','June','July','August','September','October','November','December']
    ordinalNumber =['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']

    return 'Today is '+weekday+' '+month_name[monthNum-1]+' '+ordinalNumber[dayNum-1]


#print(getDate())

def greeting(text):
    greeting_input=['hi','hello','wassup','hey']
    
    greeting_response=['hey','hey there','hello']
    for i in text.split():
        if i.lower() in greeting_input:
            return random.choice(greeting_response)
    return ''

def getPerson(text):
    wordList=text.split()
    for i in range(0,len(wordList)):
        if i+3<=len(wordList) -1 and wordList[i].lower()=='who' and wordList[i+1].lower()=='is':
            return wordList[i+2]+' '+wordList[i+3]

while True:
    text=recordAudio()
    response=''

    if wakeWord(text)==True:
        response=response+greeting(text)
         
        if ('date' in text):
            get_date=getDate()
            response=response+' '+get_date
        
        if ('who is' in text):
            person=getPerson(text)
            wiki=wikipedia.summary(person,sentences=2)
            response=response+" "+wiki

        if ('time' in text):
            now=datetime.datetime.now()
            meridiem=''
            if now.hour>=12:
                meridiem='p.m'
                hour=now.hour-12
            else:
                meridiem='am'
                hour=now.hour

            if now.minute<10:
                minute='0'+str(now.minute)
            else:
                minute=str(now.minute)
            
            response=response+' '+'It is'+str(hour)+':'+minute+' '+meridiem+'.'
            



        assistantResponse(response)








#assistantResponse(getDate())
#wakeWord()

 