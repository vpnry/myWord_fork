'''Myanmar Word Segment + dictionary lookup
Generated with the support of ChatGPT
18 Mar 2023
'''

"""
Syllable, Word, Phrase Segmenter for Burmese (Myanmar language)
Written by Ye Kyaw Thu
(Visiting Professor, LST, NECTEC, Thailand)
Last Updated: 5 Sept 2021
"""


import word_segment as wseg
from decimal import *
getcontext().prec = 1


def text_to_words(filein_path, uni_dict_bin="unigram-word.bin", bi_dict_bin="bigram-word.bin"):

    print("\nInput file:", filein_path)
    print(
        "Processing text to words with Viterbi algorithm for word segmentation.")
    print(
        f"Using: the default {uni_dict_bin} and {bi_dict_bin}")

    wordDelimiter = " "
    fileout_path = filein_path.strip() + '.words.txt'

    outputFILE = open(fileout_path, "w")

    wseg.P_unigram = wseg.ProbDist(uni_dict_bin, True)
    wseg.P_bigram = wseg.ProbDist(bi_dict_bin, False)

    with open(filein_path, 'r') as fh:
        for line in fh:
            listString = wseg.viterbi(line.replace(" ", "").strip())
            wordStr = wordDelimiter.join(listString[1])
            wordClean1 = wordStr.strip()
            wordClean2 = wordClean1.strip(wordDelimiter)
            outputFILE.write(wordClean2+"\n")
    outputFILE.close()
    return fileout_path


if __name__ == "__main__":
    pass
   # inputFile = sys.argv[1]
   # outputFile = inputFile.strip() + '.words'

   # text_to_words(inputFile)
