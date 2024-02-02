# Example filename: deepgram_test.py

import json
import asyncio
import sys
import deepgram
from tqdm import tqdm

MIMETYPE = 'm4a'


from deepgram import DeepgramClient, PrerecordedOptions, FileSource
import asyncio, json, os


deepgram = DeepgramClient()

#Note: You can use '.' if your audio is in the root
DIRECTORY = "/Users/vishnu_lanka/projects/pixie/cuisineAI/downloaded_videos"


# Feel free to modify your model's parameters as you wish!
options = PrerecordedOptions(
    punctuate=True,
    model='nova-2',
    diarize=True,
    utterances=True
)

#This function is what calls on the model to transcribe
def main():
    audio_folder = os.listdir(DIRECTORY)
    for audio_file in tqdm(audio_folder, desc="Processing audio files"):
        if audio_file.endswith(MIMETYPE):
          with open(f"{DIRECTORY}/{audio_file}", "rb") as f:
              buffer_data = f.read()
              payload: FileSource = {
                    "buffer": buffer_data,
                }
              res = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
              resp = res.to_json(indent=4)
            #   print(resp)
              with open(f"/Users/vishnu_lanka/projects/pixie/cuisineAI/data_acquisition/transcripts/{audio_file[:-4]}.json", "w") as transcript:
                  json.dump(resp, transcript)
    return

main()

# Set this variable to the path of the output file you wish to read
# OUTPUT = 'Pick your favorite output json file :)'


# The JSON is loaded with information, but if you just want to read the
# transcript, run the code below!
# def print_transcript(transcription_file):
#   with open(transcription_file, "r") as file:
#         data = json.load(file)
#         result = data['results']['channels'][0]['alternatives'][0]['transcript']
#         result = result.split('.')
#         for sentence in result:
#           print(sentence + '.')

# print_transcript(OUTPUT)