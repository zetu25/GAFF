#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# =============================================================================
#  Version: 0.1 (Oct 24, 2018)
#  Author: Tom DESHAIRES (tom.deshaires@mmtt.fr), Momenttech SAS
# =============================================================================

# This .py allows to divide a corpus extracted previously and in a very 
# specific format to be segmented into n-line files

import os

corpus_path = 'Sample_corpus/WikiQuote.txt'
result_file_name = 'wikiquote'
nb_seq = 5000

if not os.path.exists(result_file_name):
    os.makedirs(result_file_name)

with open(corpus_path, 'r') as data_file:
    lines = data_file.read().split('\n')

i = 0
j = 0

os.chdir(result_file_name)

result_path = result_file_name + str(j)
result_file = open(result_path,'a')

for line in lines:
    
    i += 1
    result_file.write(line)
    result_file.write('\n')
    

    if i % nb_seq == 0:
        result_file.close()
        j += 1
        result_path = result_file_name + str(j)
        result_file = open(result_path,'a')

