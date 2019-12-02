#!/usr/bin/python
# -*- coding: UTF-8 -*-
a='nk gqsanez h yhxe ulj dklapdn e xhoaeu loylpneawyiyw'
import string

lowercase = string.ascii_lowercase

def substitution(text, key_table):
    text = text.lower()
    result = ''
    for l in text:
        i = lowercase.find(l)
        if i < 0:
            result += l
        else:
            result += key_table[i]
    return result

def caesar_cypher_encrypt(text, shift):
    key_table = lowercase[shift:] + lowercase[:shift]
    return substitution(text, key_table)

def caesar_cypher_decrypt(text, shift):
    return caesar_cypher_encrypt(text, -shift)

for i in range(0,26):
	print (caesar_cypher_decrypt(a,i))
