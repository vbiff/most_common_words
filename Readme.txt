Hello!
I made it learn spanish!:)
This program parses N amount of .txt Spanish texts from www.rulit.me website and then 
analyze text and give back most common N words.
Besides result file, you will see words and counters in your terminal

i've made 3 files:
parser_file_from_link.py -  for parser
words_counter.py - read and write files and words counter
pipeline_mcw - pipeline file

Enjoy!

I used next modules for words2

import Collection -> Counter.most_common
#This is to get most_common words

import os
# to work with OS and find all .txt in the folder

import sys
# for arguments from command line

I used modules for parser

requests
# Send request to host

beautifulsoup4
# parse data from webpage

import io, zipfile
# to uzip and get zipfile

