# J.A.N.I.N.I
# (Just A Nested Improvised Novelle Innovation)
An home automation project using gsm module for communication without internet which can be operated with text messages as well voice-commands.

# Inspiration
The inspiration behind the JANINI project came from the need to create a reliable and affordable home automation system for areas with limited internet connectivity. In many remote locations, internet access is either unreliable or non-existent, making traditional IoT solutions impractical. The idea was to develop a system that can be controlled via SMS and voice commands, leveraging the widespread availability of GSM networks.

# What it does
JANINI represents a novel innovation that opens up possibilities for home automation in previously underserved areas, improving convenience and comfort for residents. By leveraging SMS and voice commands, the system offered an accessible and user-friendly solution for controlling home devices remotely. Throughout the development process, we learned about GSM communication, Arduino programming, voice automation, and the challenges associated with creating a reliable and secure IoT system.

# How we built it
The JANINI system was built using the following components: Arduino UNO: The microcontroller responsible for receiving and processing commands. GSM Module: To establish a connection with the GSM network and receive SMS commands. Devices for Home Automation: Various home devices were connected to the Arduino UNO via relays to control their power state. VS Code: Used to implement voice automation for controlling the devices.

The process of building the project involved the following steps:

Setting up the Arduino and GSM Module:
The Arduino IDE was used to program the Arduino UNO to communicate with the GSM module through AT commands. The GSM module was configured to receive SMS messages.

Creating the Home Automation Interface: 
Relays were connected to the Arduino, which acted as switches for controlling the power supply of different home devices. The microcontroller was programmed to interpret specific keywords in received SMS and toggle the corresponding relays accordingly.

Implementing Voice Automation: 
VS Code was utilized to develop voice automation functionality. Speech recognition libraries were employed to convert voice commands into text. The Arduino was connected to the computer running VS Code, and the commands were transmitted to the Arduino via a serial connection.

Password Protection: 
To ensure security, a password system was implemented in the SMS commands. Only authorized users with the correct password could control the home devices.

Testing and Debugging: 
Rigorous testing was carried out to verify the system's functionality and robustness. Bugs and issues were identified and fixed during this phase.

Challenges we ran into
Some of the main hurdles encountered were:

GSM Module Compatibility: 
Not all GSM modules were compatible with the Arduino, leading to compatibility issues. Selecting the right GSM module was crucial for smooth communication.

Speech Recognition Accuracy:
Voice automation presented challenges in accuracy, especially in noisy environments or with accents. Fine-tuning the speech recognition system was necessary to enhance its performance.

Real-time Responsiveness: 
Ensuring real-time responsiveness of the system was essential, especially when receiving SMS commands. Delays in processing SMS messages could lead to unsatisfactory user experiences.

Power Management: 
Managing power consumption was critical, especially in areas with limited power supply. The system needed to be energy-efficient to conserve resources.

# Accomplishments:  
We're proud of this project Ranked top 5 among 30 teams in IIT KANPUR’s Techfest TECHKRITI’23 for Embedded competition (Home automation - JANINI)

# What we learned
Before diving into the project, extensive research was conducted on GSM technology, Arduino programming, and home automation concepts. Understanding how GSM modules communicate with microcontrollers and how to integrate voice automation with VS Code was essential.

# What's next for J.A.N.I.N.I
The SMS Based Home Automation (JANINI) project aimed to bring the benefits of home automation to areas with low internet connectivity. Future iterations may involve enhancing speech recognition, exploring power-saving techniques, and expanding the range of controllable devices. The journey of creating JANINI has been an enlightening experience, and we look forward to further refining and expanding the project in the future.
