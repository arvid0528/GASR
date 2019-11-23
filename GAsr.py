import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("\n",text)
    except:
        print("Sorry, could not recognize what you said")   
    
# DETTA ÄR EN KOMMENTAR SKRIVEN AV OSCAR BITCH    
