import speech_recognition as sr
import sys
import pyttsx3
import pyfirmata
import time

board = pyfirmata.Arduino("COM8")
it = pyfirmata.util.Iterator(board)
it.start()

AudioPin = board.get_pin('d:7:i')
AudioPin.enable_reporting()
time.sleep(1)
Audio_input = AudioPin.read()
print(Audio_input)

file = {
    "turn on light" : "turning on light",
    "turn off light" : "turn off light",
    "turn on device" : "turning on device",
    "turn off device" : "turning off device"
}

engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume',1.0)



recording = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        recording.adjust_for_ambient_noise(source)
        print("listening")
        audio = recording.listen(source)
        

    try:
        input = recording.recognize_google(audio)
        print(input)
        if input == "hello":
            engine.say("Hii, I am Janani. How can i help?")
            engine.runAndWait()

            with sr.Microphone() as source:
                recording.adjust_for_ambient_noise(source)
                print("please say something")
                audio = recording.listen(source)
    
            try:
                input = recording.recognize_google(audio)
                print("you said: " + input)
                if input == "stop":
                    engine.say("bye")
                    engine.runAndWait()
                    board.exit()
                    sys.exit()
                elif input in file.keys() :
                    engine.say(file[input])
                    engine.runAndWait()
                    if input == "turn on light":
                        board.digital[7].write(1)
                    elif input == "turn off light":
                        board.digital[7].write(0)
                    elif input == "turn on device":
                        board.digital[8].write(1)
                    elif input == "turn off device":
                        board.digital[8].write(0)
                else:
                    engine.say("invalid command")
                    engine.runAndWait()
                
            except Exception as e:
                print(e)

    except Exception as e:
        print(e)        