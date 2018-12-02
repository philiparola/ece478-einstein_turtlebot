#!/usr/bin/env python2

import record
import dialogflow

def recognition():
    record.record()
    dialogflow.dialogflow_main()

if __name__ == '__main__':
    recognition()

