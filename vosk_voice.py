import speech_recognition as sr                                 ## used to convert speech into text.
import sys                                                      ## allowing the program to interact with the system (e.g., to exit the program).
import pyttsx3                                                  ##library for text-to-speech conversion.
import serial                                                   ##module for serial communication, typically with devices like Arduino.
import pyfirmata                                                ##Python wrapper for Arduino's Firmata protocol.
import time                                                     ##used for time-related functions like sleep.

board = pyfirmata.Arduino("COM8")                                   ##Initializes the connection to the Arduino board on the COM8 port.
it = pyfirmata.util.Iterator(board)                                 ## Creates an iterator that will handle incoming data from the Arduino asynchronously.
ser = serial('COM8', 115200)                                        ##Sets up serial communication on the COM8 port with a baud rate of 115200. 
if not ser.isOpen():
    ser.open()
print('com8 is open', ser.isOpen())
it.start()                                                           ## Starts the iterator, allowing it to read incoming data from the Arduino.

AudioPin = board.get_pin('d:7:i')                                    ##Configures pin 7 on the Arduino as a digital input (d) pin.
AudioPin.enable_reporting()                                          ## Enables the Arduino to report the state of the pin.
time.sleep(1)
Audio_input = AudioPin.read()                                        ##Reads the input value from the pin.
print(Audio_input)

file = {
    "lights on" : "turning on light",
    "lights off" : "turn off light",
    "devices on" : "turning on device",
    "devices off" : "turning off device"
}

engine = pyttsx3.init()                                                ##Initializes the text-to-speech engine.
engine.setProperty('rate', 125)                                        ## Sets the speech rate to 125 words per minute.
engine.setProperty('volume',1.0)                                        ## Sets the volume to maximum (1.0).



recording = sr.Recognizer()                                             ## Creates a Recognizer object for speech recognition.
while True:
    with sr.Microphone() as source:
        recording.adjust_for_ambient_noise(source)                        ## Adjusts for ambient noise to improve recognition accuracy.
        print("listening")
        audio = recording.listen(source)                                    ## Captures the audio from the microphone.
        

    try:
        input = recording.recognize_vosk(audio)[14:-3]                    ## ses the Vosk model to recognize speech from the audio and processes the recognized text (this line is specific to Vosk, which typically returns text with extra characters or brackets that are trimmed here).
        print(input)
        if input == "hello":
            engine.say("Hii, I am Janani. How can i help?")                ## Converts the response text to speech.
            engine.runAndWait()                                            ## Runs the text-to-speech engine to speak the text.

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
                    board.exit()                                            ## Exits the connection to the Arduino board.
                    sys.exit()                                                ## Exits the program.
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
