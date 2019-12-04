#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# =============================================================================
#  Version: 0.1 (Oct 24, 2018)
#  Author: Tom DESHAIRES (tom.deshaires@mmtt.fr), Momenttech SAS
# =============================================================================

# This.py allows to create a new .csv or .txt file with only the content of the 
# "modif" tags in the corpus v1 or v2 from WiCoPaCo

# [ FOR CSV ] To use the code to extract in .csv fill in the "separator" 
# variable with what you want and give a name to your output file ending with 
# .csv in the "result_file" variable. Then on line 93-94 uncomment the method 
# call csv() and comment the method call txt()

# [ FOR TXT ] To use the code to extract in .txt, give a name to your output 
# file by ending with .txt in the "result_file" variable. Then on line 93-94
# uncomment the method call txt() and comment the method call csv() 
# [!] you don't have to enter the separator variable in this case.

from multiprocessing import Pool
from lxml import etree
from scipy import *

import os
import re

list_ids = etree.parse("../../Corpus/WiCoPaCo/listIdError.xml")
tree = etree.parse("../../Corpus/WiCoPaCo/corpus-v1.xml")

tag = "modif"
separator = "µ"
result_file = open("test2.txt", "a")

array_valid_id = zeros(1000000)
array_valid_ascii = zeros(1000000)

for id_in_list in list_ids.xpath("/spelling_labels/annotation/modif_id"):
    array_valid_id[int(id_in_list.text)] = 1

file_ascii = open("../../Corpus/WiCoPaCo/caracteresASCIIAcceptes", "r")

string_of_ascii_accepted = file_ascii.read()
list_of_ascii_accepted = string_of_ascii_accepted.strip().split(' ')
file_ascii.close()

for plo in list_of_ascii_accepted:
    array_valid_ascii[int(plo)] = 1

current_node = tree.find(tag)

def csv(id, content):
    result_file.write(id)
    result_file.write(separator)

    for child in content:
        result_file.write(child.text)
        result_file.write(separator)

    result_file.write("\n")

def txt(content):
    for child in content:
        result_file.write(child.text)
        result_file.write("\t")

    result_file.write("\n")

while current_node != 0:
    
    try:
        current_id = current_node.get('id')
    except:
        print("error in current_node.get('id')")

    if array_valid_id[int(current_id)] != 0:

        cpt_down = 0
        
        try:
            for child in current_node:
                if cpt_down == 0:
                    for char in child.text:
                        if array_valid_ascii[ord(char)] == 0:
                            cpt_down += 1
                            break

                    if re.findall('it : ', child.text) or re.findall('pl : ', child.text):
                        cpt_down += 1

                    if cpt_down == 0:
                        csv(current_id, current_node)
                        # txt(current_node)
                        cpt_down +=1
        except:
            print('no more child in current_node.')

    if int(current_id)%10000 == 0:
        print("Step check: ", int(current_id))

    try:
        current_node = current_node.getnext()
    except:
        print('Really no more child in current_node.')
        break

result_file.close()

print('\nEnd.\n')
