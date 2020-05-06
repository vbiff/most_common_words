#This is pipeline for parser and most_common words creator
# here you can specify Url(but i'm quite sure you need to modify parcer_file_from_link.py if you use any other url

import parser_file_from_link
import words_counter

# how many pages do you want to pars
page = 1

# creepy dynamic url
url = 'https://www.rulit.me/books/es/' + str(page) + '/date'

parser_file_from_link.download_zip(parser_file_from_link.trade_spider(page, url))

words_counter.make_mcw()
