import streamlit as s
import requests 
s.title("Come Have Fun")
word = s.text_input("Enter a word : ")
btn = s.button(" Click To Generate")
if btn:
    url = "https://api.datamuse.com/words?ml={word}"
    response = requests.get(url)
    data = response.json()
    if response.status_code==200:
        for item in data :
            s.write(item["word"])
    else :
        s.write("There has been error")

