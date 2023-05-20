import speech_recognition as sr
import sys
import pyttsx3
import serial
import pyfirmata
import time

board = pyfirmata.Arduino("COM8")
it = pyfirmata.util.Iterator(board)
ser = serial('COM8', 115200)
if not ser.isOpen():
    ser.open()
print('com8 is open', ser.isOpen())
it.start()

AudioPin = board.get_pin('d:7:i')
AudioPin.enable_reporting()
time.sleep(1)
Audio_input = AudioPin.read()
print(Audio_input)

file = {
    "lights on" : "turning on light",
    "lights off" : "turn off light",
    "devices on" : "turning on device",
    "devices off" : "turning off device"
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
        input = recording.recognize_vosk(audio)[14:-3]
        print(input)
        if input == "hello":
            engine.say("Hii, I am Janani. How can i help?")
            engine.runAndWait()

            with sr.Microphone() as source:
                recording.adjust_for_ambient_noise(source)
                print("please say something")
                audio = recording.listen(source)
    
            try:
                input = recording.recognize_vosk(audio)[14:-3]
                print("you said: " + input)
                if input == "stop":
                    engine.say("bye")
                    engine.runAndWait()
                    board.exit()
                    sys.exit()
                elif input in file.keys() :
                    engine.say(file[input])
                    engine.runAndWait()
                    if input == "lights on":
                        board.digital[2].write(1)
                    elif input == "lights off":
                        board.digital[2].write(0)
                    elif input == "devices on":
                        board.digital[3].write(1)
                    elif input == "devices off":
                        board.digital[3].write(0)
                else:
                    engine.say("invalid command")
                    engine.runAndWait()
                
            except Exception as e:
                print(e)

    except Exception as e:
        print(e)        