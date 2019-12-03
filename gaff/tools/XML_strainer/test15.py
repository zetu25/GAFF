#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# =============================================================================
#  Version: 0.1 (Oct 24, 2018)
#  Author: Tom DESHAIRES (tom.deshaires@mmtt.fr), Momenttech SAS
# =============================================================================

from lxml import etree
from scipy import *

list_ids = etree.parse("../../Corpus/WiCoPaCo/listIdError.xml")
tree = etree.parse("../../Corpus/WiCoPaCo/corpus-v1-15000.xml")

# listOfID = [idInList.text for idInList in list_ids.xpath("/spelling_labels/annotation/modif_id")]


# listOf = [[1] if idInList is not None else [0] for idInList in list_ids.xpath("/spelling_labels/annotation/modif_id")]

# print('\nList of modif_id generated !\n')
# print(listOf)

file_ascii = open("../../Corpus/WiCoPaCo/caracteresASCIIAcceptes", "r")
string_of_ascii_accepted = file_ascii.read()
list_af_ascii_accepted = string_of_ascii_accepted.strip().split(' ')
file_ascii.close()

arrayvalid_ascii = zeros(1000000)

for plo in list_af_ascii_accepted:
    arrayvalid_ascii[int(plo)] = 1

print(arrayvalid_ascii)

# arrayvalidId = zeros(1000000)

# for idInList in list_ids.xpath("/spelling_labels/annotation/modif_id"):
#     lok = int(idInList.text)
#     arrayvalidId[lok] = 1



# dictXML = {}

# for modificationId in tree.xpath("/modifs/modif"):
#     path_bfr = "/modifs/", tree.getelementpath(modificationId[0])
#     path_before= "".join(path_bfr)

#     pathAftr = "/modifs/", tree.getelementpath(modificationId[1])
#     pathAfter= "".join(pathAftr)

#     dictXML[modificationId.get("id")] = {}

#     for before in tree.xpath(path_before):
#         print(before)
#         dictXML[modificationId.get("id")]['before'] = before.text

#     # for after in tree.xpath(pathAfter):
# #    dictXML[modificationId.get("id")]['after'] = after.text

#     lol = int(modificationId.get('id'))

#     if lol%1000 == 0:
#         print("Step check: ", modificationId.get('id'))
