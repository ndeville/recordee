from datetime import datetime
import os
print("----------")
ts_file = f"{datetime.now().strftime('%y%m%d-%H%M')}"
ts_db = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}"
ts_time = f"{datetime.now().strftime('%H:%M:%S')}"
print(f"{ts_time} starting {os.path.basename(__file__)}")
import time
start_time = time.time()

import sys
sys.path.append("/Users/nic/Python/indeXee")
sys.path.append("/Users/nic/Python/scrapee")

#from dotenv import load_dotenv
#load_dotenv()
# bearer_token = os.getenv("TOKEN")

# import my_utils
# import grist_BB
# import grist_WN
# import grist_6C
# import dbee

import pprint
pp = pprint.PrettyPrinter(indent=4)
print()
count = 0
count_row = 0

print(f"{os.path.basename(__file__)} boilerplate loaded -----------")
print()
####################
# TESTS

#1

# from pydub import AudioSegment

# test_file = '/Users/nic/Library/Mobile Documents/iCloud~com~openplanetsoftware~just-press-record/Documents/2022-09-17/12-15-32.m4a'

# audio = AudioSegment.from_file(test_file)

# print(audio)

#2  

# import os 
# from pydub import AudioSegment
# import speech_recognition as sr
# from pydub.silence import split_on_silence

# recognizer = sr.Recognizer()

# def load_chunks(filename):
#     print(f"{filename=}")
#     long_audio = AudioSegment.from_file(filename, "m4a")
#     audio_chunks = split_on_silence(
#         long_audio, min_silence_len=1800,
#         silence_thresh=-17
#     )
#     return audio_chunks

# for audio_chunk in load_chunks('test/3.m4a'):
#     audio_chunk.export("temp", format="wav")
#     with sr.AudioFile("temp") as source:
#         audio = recognizer.listen(source)
#         try:
#             text = recognizer.recognize_google(audio)
#             print("Chunk : {}".format(text))
#         except Exception as ex:
#             print("Error occured")
#             print(ex)

# print("++++++")


#3 - Clean beginning of strings / WORKING, IN NOTES


list_to_clean = [
    ' This is',
    '  another beginning',
    '           for the first time',
    ' ?or is it',
    '?perhaps not',
    '.who knows',
]

# from inspect import currentframe

# def get_linenumber():
#     cf = currentframe()
#     return cf.f_back.f_lineno

# v = False # verbose

# for str in list_to_clean:
#     if v:
#         print(f"\n---\nProcessing {repr(str)}\n")
#     valid = False
#     for i in range(1,16): # run enough time
#         if valid == False:
#             first_letter = str[0]
#             if v:
#                 print(f"line {get_linenumber()}: {repr(first_letter)}")
#             if not first_letter.isalpha():
#                 str = str[1:]
#                 if v:
#                     print(i, str)
#             else:
#                 valid = True
#         else:
#             break
#     if not str[0].isupper():
#         str = str.replace(str[0], str[0].upper(), 1) # replace only first occurence
#     if v:
#         print(f"\nFinal string: {repr(str)}")
#     else:
#         print(str)


# def clean_beginning_string(string_input):
#     valid = False
#     for i in range(1,21): # run enough time
#         if valid == False: # run as long as 1st character is not alphabetical
#             first_letter = string_input[0]
#             if not first_letter.isalpha():
#                 string_input = string_input[1:]
                
#             else:
#                 valid = True
#         else:
#             break # break loop once 1st character is alphabetical
#     # Capitalise
#     if not string_input[0].isupper():
#         string_output = string_input.replace(string_input[0], string_input[0].upper(), 1) # replace only first occurence of character with capital
#     else:
#         string_output = string_input

#     return string_output

# for line in list_to_clean:
#     print(clean_beginning_string(line))



# import transcribe

# transcribe.processing('/Users/nic/Downloads/test/20220925-155549.m4a')



x = sys.argv[1]

print(x)

########################################################################################################

if __name__ == '__main__':
    print()
    print()
    print('-------------------------------')
    print(f"{os.path.basename(__file__)}")
    print()
    print(f"{count=}")
    print()
    print('-------------------------------')
    run_time = round((time.time() - start_time), 1)
    if run_time > 60:
        print(f'{os.path.basename(__file__)} finished in {run_time/60} minutes.')
    else:
        print(f'{os.path.basename(__file__)} finished in {run_time}s.')
    print()