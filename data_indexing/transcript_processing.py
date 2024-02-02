import os
import json

def extract_transcript_from_string(json_string):
    try:
        # First deserialization to convert string to JSON
        intermediate_data = json.loads(json_string)

        # Second deserialization
        data = json.loads(intermediate_data)
    except json.JSONDecodeError:
        print("Error decoding JSON. The string might not be in a valid JSON format.")
        return []
    if 'results' in data and len(data['results']) > 0:
        transcripts = []
        for result in data['results']['channels']:
            if 'alternatives' in result and len(result['alternatives']) > 0:
                for alternative in result['alternatives']:
                    if 'transcript' in alternative:
                        transcripts.append(alternative['transcript'])
        return transcripts
    else:
        return []

def load_file_as_string(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def process_directory(directory_path):
    all_transcripts = {}

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            file_content = load_file_as_string(file_path)
            transcripts = extract_transcript_from_string(file_content)
            all_transcripts[filename] = transcripts

    return all_transcripts

# Specify your directory path here
directory_path = '/Users/vishnu_lanka/projects/pixie/cuisineAI/data_acquisition/transcripts'

# Process the directory and get all transcripts
transcripts_data = process_directory(directory_path)

# Specify the path for the new JSON file where all transcripts will be saved
output_file_path = './transcripts_consolidated.json'

# Save all transcripts into a new JSON file
with open(output_file_path, 'w') as output_file:
    json.dump(transcripts_data, output_file, indent=4)
