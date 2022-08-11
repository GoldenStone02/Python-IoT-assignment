# Introduction
This is a project that is done for a module, Python Programming for IOT, where we are supposed to create a Proof of Concept (POC) which utilizes the skills we learnt through the module to create a functional POC as our final project in the module. 
Our group decided to create a smart security system as our idea for our group project

# Features

## Basic Features
- Sensors attached via backend APIs
- Flask Backend Web server
- Simple JSON/Text Database
- Socket Programming in the Backend

# Installation
 - Download **Python Version 3.7 and onwards**
 - Run `pip3 install -r requirement.txt` in terminal to install all packages
## Installation on Raspberry Pi from Github
- `git clone https://github.com/GoldenStone02/Python-IoT-assignment`

# File Structure
This would be the structure of our Program
```
PYPROG Project/
├── server/
│   ├── database/           # Storage of users and passwords
│   │   ├── image_upload/   # Storage of images and video      
│   │   ├── authlist.txt    # RFID authentication list      
│   │   └── users.json
│   ├── sensors/            # Code for each sensor
│   │   ├── MFRC522         # RFID Library
│   │   ├── buzzer.py
│   │   ├── camera.py      
│   │   ├── l2C_LCD_driver.py      
│   │   ├── keypay.py
│   │   ├── LCD.py
│   │   ├── LED.py
│   │   ├── PIR.py
│   │   ├── rfid.py      
│   │   └── servo.py
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── base.html       # Used for templating
│   │   ├── index.html       
│   │   └── login.html
│   ├── __init__.py         # Creates the Flask App
│   ├── iot_logic.py        # Main IOT logic
│   └── views.py            # Routes for websites
├── .gitignore
├── main.py                 # Main point of entry
├── README.md
└── requirement.txt         # Download required files
```


