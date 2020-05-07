# -*- coding: utf-8 -*-
"""
Convert Chinese characters to Jyutping.
"""
from __future__ import absolute_import
from jyutping import dictionary


def get_jyutping(characters, external_dictionary=None, unk_char='<UNK>'):
    """
    Convert Chinese characters to Jyutping.
    @return an array of Jyutping for each character.
    """
    result = []
    for ch in characters:
        jyp = search_single_internal(ch, unk_char)
        if jyp == unk_char and external_dictionary:
            jyp = search_single_external(ch, external_dictionary, unk_char)
        result.append(jyp)
    return result


def search_single_internal(character, unk_char):
    if len(dictionary.CHS_DICT) == 0 or len(dictionary.CHT_DICT) == 0:
        dictionary.load_dictionary()
    jyp = dictionary.CHS_DICT.get(character, unk_char) or dictionary.CHT_DICT.get(character, unk_char)
    if jyp and '/' in jyp:
        jyp = jyp.split('/')
    return jyp


def search_single_external(character, external_dictionary, unk_char):
    jyp = external_dictionary.get(character, unk_char)
    return jyp


def update_dictionary(update_list):
    dictionary.update_dictionary(update_list)

    
def _test(word):
    print(word, get_jyutping(word))

if __name__ == '__main__':
    _test('广东话')
