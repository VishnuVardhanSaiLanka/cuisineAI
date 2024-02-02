# Steps:
1. Data acquisation:
- used data_acquisition/download_videos.py to download youtube videos using yt-dlp
- used data_acquisition/transcription.py to transcribe the audio into text using deepgram nova-2 model

2. Data Indexing:
- used data_indexing/transcript_processing.py to post-process the deepgram response and store all of the transcripts in a single json i.e, data_indexing/transcripts_consolidated.json
- used data_indexing/format_transcripts_with_openai.py to send the transcripts to openAI get
    1. chunks of transcript in the form of steps that can be used later
    2. summary of transcript in brief that can be used to search against the user input
- above step resulted in a structured data in the file data_indexing/transcripts_structured.json
- used data_indexing/split_summary_files.py to create a new folder data_indexing/summaries where we store all the summaries of individual transcripts as a seperate text file, that is used in llama_index query engine

3. Images:
- used data_indexing/ffmpeg_screenshots.py to extract screenshots from the videos. Extacting screenshots only once in 3 seconds.
- Above screenshots are stored in data_indexing/screenshots path that are later used for multimodel indexing using llama_index

4. Main Jupyter notebook:
- Main.ipynb is the main notebook to run.

# Run time Flow:
When a query comes in, we first run it against the stored indexes of summaries, and retrieve the closest matching transcript corresponding to the respective summary. Now we display the openAI generated wikiHow Step wise heading and content. We then take the step content as a query and do multimodal retrieval using openAI GPT-4-vision to search among the screenshots present screenshots/respective_transcript_folder and display the topmost screenshot