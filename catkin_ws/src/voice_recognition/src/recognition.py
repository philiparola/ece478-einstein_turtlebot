#!/usr/bin/env python2

import os, sys
#import record
import dialogflow

def recognition():
    #record.record()
    os.system("./record.py")
    response = dialogflow.dialogflow_main()
    print("test" + response)

if __name__ == '__main__':
    while(True):
        recognition()
        input("Press Enter to continue...")

