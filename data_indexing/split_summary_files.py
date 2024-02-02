import json
import os

# Load the JSON file
file_path = '/Users/vishnu_lanka/projects/pixie/cuisineAI/data_indexing/transcripts_structured.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Iterate through each key-value pair in the JSON file
for video_name, content in data.items():
    # Create a .txt file for each key (video name)
    txt_file_name = os.path.join('/Users/vishnu_lanka/projects/pixie/cuisineAI/data_indexing/summaries/', video_name + '.txt')
    
    # Write the 'Summary' content to the .txt file
    with open(txt_file_name, 'w') as txt_file:
        if content["openai_response"] is not None:
            x = json.loads(content["openai_response"])
            txt_file.write(x.get('Summary', ''))  # Writing the summary if available
        else:
            print("content is None")

# Confirm completion
"Text files created for each key in the JSON file."
