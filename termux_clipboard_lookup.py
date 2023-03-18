'''Myanmar Word Segment + dictionary lookup
Generated with the support of ChatGPT
18 Mar 2023
'''

import os
import subprocess
import re
from termux_lookup_cli import main_viterbi
import datetime
import unicodedata
# from unidecode import unidecode

def convert_to_latin(text):
    # Convert any non-Latin characters to Latin using Unicode normalization
    normalized_text = unicodedata.normalize('NFD', text)
    latin_text = ''.join(c for c in normalized_text if unicodedata.category(c) != 'Mn')
    return latin_text

# def convert_to_latin_2(text):
#     # Convert any non-Latin characters to Latin using unidecode
#     latin_text = unidecode(text)
#     return latin_text


def main(text):
    # Define the prefix for the output file
    text = text.strip()

    # Get the first 8 words of the input text and convert any non-Latin characters to Latin
    words = re.findall(r'\b\w+\b', txt)
    first_8_words = ''.join(words[:8])
    filename = convert_to_latin(first_8_words)

    # Get the current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")

    # Define the path to the new directory
    dir_path = './_textFiles'

    # Create the new directory if it does not exist
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Define the path to the output file
    save_path = os.path.join(dir_path, f'{current_time}_{filename}.txt')

    # Write the input text to the output file
    with open(save_path, 'w') as f:
        f.write(text)

    # Run the main Viterbi algorithm
    main_viterbi(save_path, True)


if __name__ == '__main__':
    # Get the text from the clipboard
    txt = subprocess.getoutput('termux-clipboard-get')

    # Call the main function with the input text
    main(txt)
