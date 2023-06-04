import csv
import os
from pydub import AudioSegment
import numpy as np

#path to files 
folder_path = '/Users/daria/Desktop/GRAD_PROJECT/recordings_london_wav'

#all wav files
wav_files = [file for file in os.listdir(folder_path) if file.endswith(".wav")]

#csv file to store the results
csv_filename = "london_scientific4.csv"

#create csv file
with open(csv_filename, mode='w', newline='') as file:
    fieldnames = ['File Name', 'Highest Frequency', 'Lowest Frequency', 'Highest Decibel', 'Lowest Decibel']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
    #use audiosegment and np to get data
    for file_name in wav_files:
        file_path = os.path.join(folder_path, file_name)
        print("Processing:", file_path)

        audio_file = AudioSegment.from_file(file_path)
        audio_data = np.array(audio_file.get_array_of_samples())

        fft_data = np.fft.fft(audio_data)
        magnitudes = np.abs(fft_data)

        top_indices = np.argsort(magnitudes)[-5:]
        sampling_rate = audio_file.frame_rate
        frequencies = np.fft.fftfreq(len(magnitudes))
        frequencies = np.abs(frequencies * sampling_rate)

        #calculate db levels
        decibels = 20 * np.log10(magnitudes)

        #if over 0, as it was giving me 0 as a result for min freq and db
        highest_frequency = np.max(frequencies[top_indices]) if len(frequencies) > 0 else ''
        lowest_frequency = np.min(frequencies[top_indices]) if len(frequencies) > 0 else ''
        highest_decibel = np.max(decibels[top_indices]) if len(decibels) > 0 else ''
        lowest_decibel = np.min(decibels[top_indices]) if len(decibels) > 0 else ''

        row = {
            'File Name': file_name,
            'Highest Frequency': highest_frequency,
            'Lowest Frequency': lowest_frequency,
            'Highest Decibel': highest_decibel,
            'Lowest Decibel': lowest_decibel,
        }

        writer.writerow(row)

        print("Highest Frequency:", highest_frequency)
        print("Lowest Frequency:", lowest_frequency)
        print("Highest Decibel:", highest_decibel)
        print("Lowest Decibel:", lowest_decibel)
        print() 

print("Results saved to", csv_filename)

