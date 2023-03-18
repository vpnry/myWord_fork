'''Myanmar Word Segment + dictionary lookup
Generated with the support of ChatGPT
18 Mar 2023

You need to put Stardict dictionary data to
dictionaries/mm-en.ifo

'''

import sys
import argparse
import json
import os
import subprocess
import string
from collections import defaultdict
from typing import Dict, List, Tuple

from termux_word_segment import text_to_words


def parse_file_to_words(file_path: str) -> List[str]:
    with open(file_path, 'r') as f:
        text = f.read()
    # Replace Myanmar '။' and '၊' with space
    text = text.replace('။', ' ').replace('၊', ' ')
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    return [word.strip() for word in text.split() if word.strip()]


def stardict_to_json(stardict_file: str) -> Dict[str, List[str]]:
    base_name = os.path.splitext(stardict_file)[0]
    json_file = base_name + '.json'
    json_combined = base_name + 'combined.json'

    if os.path.exists(json_combined):
        with open(json_combined, 'r') as f:
            return json.load(f)

    check_cmd = "which pyglossary"
    result = subprocess.run(check_cmd, shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("pyglossary is not installed. Do you want to install it? (y/n)")
        user_input = input()
        if user_input.lower() == 'y':
            cmd = ['pip3', "install", "pyglossary"]
            subprocess.run(cmd)
        else:
            sys.exit("pyglossary is required for this script to run.")

    cmd = ['pyglossary', stardict_file, json_file,
           '--read-format=Stardict', '--write-format=Json']
    subprocess.run(cmd)

    with open(json_file, 'r') as f:
        star_dict = json.load(f)

    combined_json_dict = defaultdict(list)
    for key, value in star_dict.items():
        key = key.split(' (')[0]
        combined_json_dict[key].append(value)

    with open(json_combined, 'w') as f:
        json.dump(combined_json_dict, f, ensure_ascii=False, indent=2)

    return combined_json_dict


def lookup_stardict_from_file(file_path: str, dict_data: dict) -> List[Tuple[str, str]]:
    words = parse_file_to_words(text_to_words(file_path))
    dict_size = len(dict_data)
    print(f"Total dictionary entries: {dict_size}")
    word_count = len(words)
    print(f"Total words in the input text: {word_count}")

    results = []
    known_words_count = 0
    unknown_words_count = 0
    word_id = 0
    word_id_map = {}

    for word in words:
        if word not in word_id_map:
            word_id += 1
            word_id_map[word] = word_id
            if word in dict_data:
                known_words_count += 1
                results.append(
                    (f'<span id="{word_id}"></span>{word}', '<br>'.join(dict_data[word])))
            else:
                results.append((word, '?'))
        else:
            word_id += 1
            if word in dict_data:
                known_words_count += 1
                results.append(
                    (word, f'pls see no. <a href="#{word_id_map[word]}">{word_id_map[word]} above</a>'))
            else:
                results.append((word, f'? ~ no. {word_id}'))

    covered_percent = known_words_count / word_count * 100
    print(
        f"\nKnown words: {known_words_count}/{word_count} ({covered_percent:.2f}%)")
    unknown_words_count = word_count - known_words_count
    print(f"Unknown words: {unknown_words_count} ({100-covered_percent:.2f}%)")

    return results


def save_results_to_html(results: List[tuple], out_file: str, open_url_http_server: bool = False) -> None:
    with open(out_file, 'w') as f:
        f.write('''<!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Myanmar Word Segment Results</title>
        </head>
        <body>
        <h3><a href='./'>Home</a></h3>\n''')

        for i, (word, definition) in enumerate(results, start=1):
            f.write(f'<p>{i}. <b>{word}</b></p>\n<p>{definition}</p><hr>\n')
        f.write('</body></html>')

    print('Saved output_file: ', out_file)
    if open_url_http_server:
        serve_http_termux(out_file)


def serve_http_termux(out_file: str) -> None:
    import time
    # import urllib.parse
    cmd = ["python3", "-m", 'http.server', '8888']
    server_process = subprocess.Popen(cmd)

    # out_file_encode = urllib.parse.quote(out_file.encode("utf-8"), safe="")
    # url = f'http://0.0.0.0:8888/{out_file_encode}'
    url = f'http://0.0.0.0:8888/{out_file}'
    print(url)
    check_cmd = "which termux-open-url"
    result = subprocess.run(check_cmd, shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Openning... {url}")
        cmd = ["termux-open-url", url]
        subprocess.run(cmd)
    else:
        # print('Termux Android https://f-droid.org/en/packages/com.termux/')
        import webbrowser
        import urllib.parse

        webbrowser.open(url)

    print(f"Closing python http.server in 8 minutes.")
    time.sleep(480)
    server_process.terminate()


def main_viterbi(input_file: str, open_url_http_server: bool = False, stardict_file: str = 'dictionaries/mm-en.ifo') -> None:
    stardict_json = stardict_to_json(stardict_file)
    results = lookup_stardict_from_file(input_file, stardict_json)
    save_results_to_html(
        results, f'{input_file}.dictionary.html', open_url_http_server)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('in_file', type=str, help='Input file file.txt')
    parser.add_argument('open_url_http_server', type=str, nargs='?', default=True,
                        help='Serve file via http-server (npm i -g http-server). Default = True')

    parser.add_argument('stardict_file', type=str, nargs='?',
                        default='dictionaries/mm-en.ifo', help='Stardict file dict.ifo')

    args = parser.parse_args()
    main_viterbi(args.in_file, args.open_url_http_server, args.stardict_file)
