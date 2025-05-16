

# # Dependencies
# 1) sudo apt-get install pyaudio
# 3) sudo apt-get install espeak 
# 2) pip3 install SpeechRecognition
# 3) pip3 install numpy
# 4) pip3 install pillow
# 5) sudo apt-get install pytesseract
# 6) sudo apt-get install opencv-python
# 7) pip3 install opencv
# 8) pip3 install matplotlib



import numpy as np

import os

from PIL import Image

from pytesseract import image_to_string

import matplotlib.pyplot as plt

import PIL

from model import charToArray, asciicodes, brailles
python
import speech_recognition as sr

from gtts import gTTS

import os
import time


r = sr.Recognizer()

with sr.Microphone() as source:
    
    print("Speak Anything :")
    
    audio = r.listen(source,timeout=1,phrase_time_limit=10)
    
    print('Done, Please wait while we are processing what you said...')
    
    try:
        
        text = r.recognize_google(audio)
        print('\n\n\n')
        print("You said : {}".format(text))
        print('\n\n\n')
    except:
        
        print("Sorry we could not recognize what you said. You can try again.")





ascii_braille = {}


arrayLength = len(asciicodes)

counter = 0

while counter < arrayLength:
    
    ascii_braille[asciicodes[counter]] = brailles[counter]
    
    
    counter = counter + 1

letterToImgPath = {
    "a": "images/a.png",
    "b": "images/b.png",
    "c": "images/c.png",
    "d": "images/d.png",
    "e": "images/e.png",
    "f": "images/f.png",
    "g": "images/g.png",
    "h": "images/h.png",
    "i": "images/i.png",
    "j": "images/j.png",
    "k": "images/k.png",
    "l": "images/l.png",
    "m": "images/m.png",
    "n": "images/n.png",
    "o": "images/o.png",
    "p": "images/p.png",
    "q": "images/q.png",
    "r": "images/r.png",
    "s": "images/s.png",
    "t": "images/t.png",
    "u": "images/u.png",
    "v": "images/v.png",
    "w": "images/w.png",
    "x": "images/x.png",
    "y": "images/y.png",
    "z": "images/z.png",
    " ": "images/void.png",
}

def addImages(list_im):
    
    imgs = [ PIL.Image.open(i) for i in list_im ]
    
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
   
    imgs_comb = PIL.Image.fromarray(imgs_comb)
    
    imgs_comb.save('output.jpg')  

def writeImage(b_string):
    
    images = []
    
    for letter in b_string:
        
        images.append(letterToImgPath[letter])
    
    addImages(images)    
    
    img = Image.open('output.jpg')
    
    img.show()

def writeText(b_string):
    
    final_string = ''
    
    for letters in b_string:
        
        final_string = final_string + ascii_braille[letters.lower()]
    
    print(final_string)

def textToBraille(text):
    
    final_string = ''
    
    for char in text:
       
        char = char.lower()
        if char == "a":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["a"]))
        elif char == "b":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["b"]))
        elif char == "c":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["c"]))
        elif char == "d":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["d"]))
        elif char == "e": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["e"]))
        elif char == "f": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["f"]))
        elif char == "g":
            final_string = final_string + ascii_braille[char] 
            print(char + " " + str(charToArray["g"]))
        elif char == "h": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["h"]))
        elif char == "i":
            final_string = final_string + ascii_braille[char] 
            print(char + " " + str(charToArray["i"]))
        elif char == "j": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["j"]))
        elif char == "k": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["k"]))
        elif char == "l": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["l"]))
        elif char == "m": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["m"]))
        elif char == "n": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["n"]))
        elif char == "o":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["o"]))
        elif char == "p": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["p"]))
        elif char == "q": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["q"]))
        elif char == "r": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["r"]))
        elif char == "s": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["s"]))
        elif char == "t": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["t"]))
        elif char == "u": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["u"]))
        elif char == "v": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["v"]))
        elif char == "w":
            final_string = final_string + ascii_braille[char] 
            print(char + " " + str(charToArray["w"]))
        elif char == "x": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["x"]))
        elif char == "y": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["y"]))
        elif char == "z":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["z"]))
        elif char == " ":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray[" "]))
    print('\n\n\n')  
    #time.sleep()      
    print(final_string)
    print('\n\n\n')
    return final_string

textToBraille(text)

myText = text

language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")