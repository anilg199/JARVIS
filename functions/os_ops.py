import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


# Open camera
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    
#open notepad and discord
def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])
    
    
#open CMD
def open_cmd():
    os.system('start cmd')
    
# open calculator
def open_calculator():
    sp.Popen(paths['calculator'])