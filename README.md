# Introduction
This is a project that is done for a module, Python Programming for IOT, where we are supposed to create a Proof of Concept (POC) where we utilize the skills we learnt through the module to create a funcitonal POC as our final project.

# Features
## Basic Features
- Tkinter GUI
- Flask Backend Web server

## Advanced Features

# Installation
 - Download *Insert Required Python version*
 - Run `pip3 install -r requirement.txt` in terminal to install all packages

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
│   │   └── test.py
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


