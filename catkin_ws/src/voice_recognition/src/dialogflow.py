#!/usr/bin/env python2

import dialogflow_v2
import os

def detect_intent_audio(project_id, session_id, audio_file_path,
                        language_code):
    session_client = dialogflow_v2.SessionsClient()

    audio_encoding = dialogflow_v2.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    sample_rate_hertz = 16000

    session = session_client.session_path(project_id, session_id)

    with open(audio_file_path, 'rb') as audio_file:
        input_audio = audio_file.read()

    audio_config = dialogflow_v2.types.InputAudioConfig(
        audio_encoding=audio_encoding, language_code=language_code,
        sample_rate_hertz=sample_rate_hertz)
    query_input = dialogflow_v2.types.QueryInput(audio_config=audio_config)

    response = session_client.detect_intent(
        session=session, query_input=query_input,
        input_audio=input_audio)

    return response.query_result.fulfillment_text

def dialogflow_main():
    user_input = 'user_input.wav'
    result = detect_intent_audio("turtlebot-1cb15", "1-1-1-1-1", user_input, 'en-US')
    return result

if __name__ == '__main__':
    dialogflow_main()
