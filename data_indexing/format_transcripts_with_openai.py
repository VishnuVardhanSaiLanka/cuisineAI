import json
from tqdm import tqdm
from openai import OpenAI


sys_prompt = '''you are an helpful assistant. Your job is to do data transformation, i.e, converting text data of one format to another. Follow below guidelines\n\n1. You are given a transcript of a YouTube video by legendary chef Jaques Pepin talking about cooking.\n2. Your job is to chunk and summarize transcripts.\n3. Generate a WikiHow style article with steps, for the given transcript. The content of the steps must as if the chef Jaques Pepin must be narrating them\n4. A brief summary of one or two lines on what the transcript is about. DONOT to mention the chef name.  Summary must focus ONLY ON what the actual recipe or cooking related thing it is\n\nResponse to be generated in the below JSON format:\n\n{ "WikiHow Style Article": {"step1": {"Heading": <>, "content": <>}, {"step2": {"Heading": <>, "content": <>}....},\n"Summary": <str>}'''

client = OpenAI(
        api_key='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',  # this is also the default, it can be omitted
        )

# Function to read the JSON file
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to make an API call to OpenAI and get the completion
def get_openai_completion( user_prompt):
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",  # Specify the model
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_prompt[0]}
            ],
            temperature=0.1,
            max_tokens=2500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["###"]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to process the JSON and make API calls
def process_json_and_call_api(input_file_path, output_file_path, system_prompt):
    data = read_json(input_file_path)
    output_data = {}
    # import itertools
    # data = dict(itertools.islice(data.items(), 2))

    for key in tqdm(data.keys(), desc="Processing API calls"):
        user_prompt = data[key]
        openai_output = get_openai_completion(user_prompt)
        output_data[key] = {
            "transcription": user_prompt,
            "openai_response": openai_output
        }

        with open(output_file_path, 'w') as output_file:
            json.dump(output_data, output_file, indent=4)

# Specify your file paths and system prompt
input_json_path = '/Users/vishnu_lanka/projects/pixie/cuisineAI/data_indexing/transcripts_consolidated.json'
output_json_path = '/Users/vishnu_lanka/projects/pixie/cuisineAI/data_indexing/transcripts_structured.json'

# Process the file and make API calls
process_json_and_call_api(input_json_path, output_json_path, sys_prompt)
