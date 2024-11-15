from datetime import datetime
import os
print("----------")
ts_file = f"{datetime.now().strftime('%y%m%d-%H%M')}"
ts_db = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}"
ts_time = f"{datetime.now().strftime('%H:%M:%S')}"
print(f"{ts_time} starting {os.path.basename(__file__)}")
import time
start_time = time.time()

from dotenv import load_dotenv
load_dotenv()

import pprint
pp = pprint.PrettyPrinter(indent=4)
print()
count = 0
count_row = 0

print(f"{os.path.basename(__file__)} boilerplate loaded -----------")
print()
####################
# Transcribe One File

import whisper
from whisper.utils import get_writer
import warnings
# from whisper.utils import get_writer
import re
import shutil
from collections import namedtuple # to return transcript result as namedtuple
import os, os.path
from pathlib import Path
import sys
import moviepy.editor # to calculate video duration

from openaee_get import ai_transcript_processing


""" TODO

TEST https://github.com/pyannote to diariaze speakers

"""



warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")





from datetime import datetime
from pathlib import Path
import os
import shutil
import whisper
from pyannote.audio import Pipeline

def transcribe_file(file_path, model_size="base"):
    print(f"\n\n{datetime.now().strftime('%H:%M:%S')} PROCESSING AS SINGLE RECORDING: {file_path}\n\n")

    filepath_parts = Path(file_path).parts
    uid = filepath_parts[-1]
    copy_to_path = os.path.abspath(os.path.join(file_path, os.pardir))

    # Convert video to audio if it's an MP4 file
    if file_path.lower().endswith('.mp4'):
        print("Converting video to audio...")
        temp_audio_path = os.path.join(copy_to_path, f"{uid}_temp.wav")
        try:
            video = moviepy.editor.VideoFileClip(file_path)
            video.audio.write_audiofile(temp_audio_path)
            video.close()
            diarization_audio_path = temp_audio_path
        except Exception as e:
            print(f"Error converting video to audio: {str(e)}")
            diarization_audio_path = file_path
    else:
        diarization_audio_path = file_path

    # Load Whisper model
    model = whisper.load_model(model_size)

    # Transcribe using original file (Whisper can handle MP4)
    result = model.transcribe(file_path)

    # Extract the transcription
    transcript = result['text']
    segments = result['segments']  # Segment timestamps for diarization

    # Save raw transcript
    output_file_txt = f"{copy_to_path}/{uid}.txt"
    with open(output_file_txt, 'w') as f:
        print(transcript, file=f)
    print(f"\n{output_file_txt} created.")

    # Diarization using converted audio file
    try:
        hf_token = os.getenv("HUGGING_FACE_TOKEN")
        if not hf_token:
            print("Warning: HUGGING_FACE_TOKEN not found in .env file")
            raise Exception("No HuggingFace token provided")

        print(f"Attempting diarization with token: {hf_token[:4]}...")
        pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization",
            use_auth_token=hf_token
        )
        
        if pipeline is None:
            raise Exception("Failed to initialize pipeline")
            
        diarization = pipeline(diarization_audio_path)
        
        # Combine diarization with transcription
        diarized_transcript = []
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            segment_texts = [
                seg['text']
                for seg in segments
                if seg['start'] >= turn.start and seg['end'] <= turn.end
            ]
            speaker_text = " ".join(segment_texts)
            diarized_transcript.append(f"[{speaker}] {speaker_text}")

        diarized_output = "\n".join(diarized_transcript)
        
    except Exception as e:
        print(f"\nWarning: Diarization failed - {str(e)}")
        print("\nPlease ensure you have:")
        print("1. Added your HuggingFace token to .env file as HUGGING_FACE_TOKEN=your_token_here")
        print("2. Accepted the user conditions at https://hf.co/pyannote/speaker-diarization")
        diarized_output = "Diarization not available"
        diarized_transcript = []

    # Clean up temporary audio file
    if 'temp_audio_path' in locals() and os.path.exists(temp_audio_path):
        try:
            os.remove(temp_audio_path)
        except Exception as e:
            print(f"Warning: Could not remove temporary audio file: {str(e)}")

    # Save diarized transcript
    output_file_diarized = f"{copy_to_path}/{uid}_diarized.txt"
    with open(output_file_diarized, 'w') as f:
        print(diarized_output, file=f)
    print(f"\n{output_file_diarized} created.")

    # Save enriched Markdown version
    enriched_transcript = ai_transcript_processing(transcript)
    final_transcript = f"## RAW TRANSCRIPT\n{file_path}\n\n{transcript}\n\n## DIARIZED TRANSCRIPT\n\n{diarized_output}\n\n{enriched_transcript}"
    output_file_md = f"/Users/nic/Dropbox/Notes/kaltura/transcripts/{uid}.md"
    with open(output_file_md, 'w') as f:
        print(final_transcript, file=f)
    print(f"\n{output_file_md} created.")

    # Save SRT
    srt_writer = get_writer("srt", copy_to_path)
    srt_output_file = f"{copy_to_path}/{uid}.srt"
    srt_writer(result, srt_output_file)
    print(f"\n{srt_output_file} created.")

    return transcript, diarized_transcript












########################################################################################################

if __name__ == '__main__':
    print()
    # processing(file=sys.argv[1])
    # language = 'english'

    file_path = input(f"\nEnter file path to transcribe: ")
    model_size = input(f"\nModel size (base.en, small.en, medium, medium.en, large, turbo) or just Enter for Turbo: ")

    if model_size == "":
        model_size = "turbo"
    else:
        model_size = model_size

    transcribe_file(file_path,model_size)

    # transcribe_file('/Users/nic/Movies/Recordings/240831-173202-test.mp4')
    print('-------------------------------')
    print(f"{os.path.basename(__file__)}")
    print()
    print()
    print('-------------------------------')
    run_time = round((time.time() - start_time), 1)
    if run_time > 60:
        print(f'{os.path.basename(__file__)} finished in {run_time/60} minutes.')
    else:
        print(f'{os.path.basename(__file__)} finished in {run_time}s.')
    print()