import os
import re
from google.cloud import texttospeech
from playsound import playsound

output_file = "output.mp3"
client = texttospeech.TextToSpeechClient()

def synthesize(text):
    cleaned_text = clean_text(text)
    synthesis_input = texttospeech.SynthesisInput(text=cleaned_text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-GB",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(output_file, "wb") as out:
        out.write(response.audio_content)

    playsound(output_file)

    os.remove(output_file)

    return response

def clean_text(text):
    code_block_pattern = r'```.*?```'
    new_text = re.sub(code_block_pattern, '', text, flags=re.DOTALL)

    backtick_pattern = r'`'
    new_text = re.sub(backtick_pattern, '', new_text)

    return new_text
