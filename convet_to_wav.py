from pydub import AudioSegment
from pydub.utils import which

import os
import csv
import numpy as np

AudioSegment.converter = which("ffmpeg")
wrong_folder_path = '/Users/daria/Desktop/GRAD_PROJECT/recordings_london_raw'
right_folder_path = '/Users/daria/Desktop/GRAD_PROJECT/recordings_london_wav'
audio_files = []
audio_max_val = []

def make_wave(wrong_folder_path, right_folder_path):
    #loop through files
    for file in os.scandir (wrong_folder_path):
        print(file)
        #if file has m4a extension
        if file.path.endswith(".m4a"):
                #create wav file
                out_file = right_folder_path + os.path.splitext(os.path.basename(file.path))[0] + ".wav"
                AudioSegment.from_file(file.path).export(out_file, format="wav")
                print(f"Creating {out_file}")

print("inceput")
make_wave(wrong_folder_path, right_folder_path)
print("gata")





#----------------------------------

