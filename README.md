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
├── app/                    # Not confirm on this
│   └── tkinter.py
├── server/
│   ├── database/           # Storage of users and passwords
│   │   └── users.json
│   ├── module/
│   │   ├── module.py       # Create the main program here
│   │   └── __init__.py
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── example.html
│   │   └── index.html
│   └── server.py           # Creates the Flask App
├── .gitignore
├── main.py                 # Main point of entry? 
├── README.md
└── requirement.txt
```


