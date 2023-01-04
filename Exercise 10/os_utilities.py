"""
os_utilities.py
By: Abhinav Tyagi
Date: 02NOV22
"""

import platform, psutil

def detect_os()->str:
    return platform.system()

def cpu_load():
    return(psutil.cpu_count(), psutil.cpu_percent())

if(__name__=='__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    
    #Check OS
    my_os=detect_os()
    my_os=my_os.lower()
    
    #Parse OS
    if my_os=="windows":
        print("System is Windows")
    elif my_os=="Linux":
        print("System is Linux")
    elif my_os=="darwin":
        print("System is MacOS")
    elif my_os=="cygwin":
        print("System is MacOS")
    elif my_os=="aix":
        print("System is AIX")
    else:
        print(f"Unidentified system {my_os}")

else:
    pass