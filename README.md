# Introduction
This is a project that is done for a module, Python Programming for IOT, where we are supposed to create a Proof of Concept (POC) which utilizes the skills we learnt through the module to create a functional POC as our final project in the module. 
Our group decided to create a smart security system as our idea for our group project

# Features
## Basic Features
- Flask Backend Web server
- Simple JSON Database

## Additional Features
- 

# Installation
 - Download *Insert Required Python version*
 - Run `pip3 install -r requirement.txt` in terminal to install all packages
## Installation on Raspberry Pi
- `git clone https://github.com/username/repo_name.git`

# Structure
This would be the structure of our Program
```
PYPROG Project/
├── app/                    # Most likely won't be added
│   └── tkinter.py
├── server/
│   ├── database/           # Storage of users and passwords
│   │   └── users.json
│   ├── sensors/            # Code for each sensor is stored here
│   │   ├── keypad.py      
│   │   ├── rfid.py      
│   │   └── servo.py
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── base.html       # Used for templating
│   │   ├── index.html       
│   │   └── login.html
│   ├── __init__.py         # Creates the Flask App
│   └── views.py            # Routes for website
├── .gitignore
├── main.py                 # Main point of entry
├── README.md
└── requirement.txt
```


