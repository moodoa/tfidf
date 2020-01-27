# coding: utf-8
import speech_recognition
from selenium import webdriver
import tempfile
from gtts import gTTS
from pygame import mixer



r = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

query = r.recognize_google(audio,language='zh-TW')

mixer.init()

sentence = '馬上幫你搜尋'+query+'的影片'

def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence,lang='zh-TW')
        tts.save('{}.mp3'.format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()
speak(sentence)

driver = webdriver.Chrome()

driver.get('https://www.youtube.com/')

search_input = driver.find_element_by_id('search')
search_input.send_keys(query)
go = driver.find_element_by_id('search-icon-legacy')
go.click()
