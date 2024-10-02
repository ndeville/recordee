


import os
import mimetypes

def is_audio_file(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith('audio')

def find_audio_files(folder_path):
    # Expand the tilde to the full home directory path
    folder_path = os.path.expanduser(folder_path)

    # os.walk will go through all files and directories, including hidden ones
    for root, dirs, files in os.walk(folder_path, topdown=True):
        try:
            # print(f"Searching in: {root}")
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Checking file: {file_path}")
                if is_audio_file(file_path):
                    print(f"Audio file found: {file_path}")
        except PermissionError as e:
            print(f"Permission denied for {root}. Error: {e}")

folder_path = "~/Library/Containers/com.apple.VoiceMemos"
find_audio_files(folder_path)


