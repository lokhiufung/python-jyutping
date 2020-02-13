"""
Dictionary
"""
from __future__ import absolute_import
import os
import io
from jyutping import logger

CHT_DICT = {}
CHS_DICT = {}


def load_dictionary():
    source_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(source_path, 'data')
    dictionary_file = os.listdir(data_path)[0]
    logger.log('Load dictionary %s.' % dictionary_file)
    dictionary_file_full_path = os.path.join(data_path, dictionary_file)
    with io.open(dictionary_file_full_path, mode='r', encoding='utf-8') as f:
        index = 0
        for line in f:
            index += 1
            if index < 10:
                continue
            line = line.strip().split('\t')
            cht, chs, jyp = line
            CHT_DICT[cht] = jyp
            CHS_DICT[chs] = jyp


def update_dictionary(update_list):
    source_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(source_path, 'data')
    dictionary_file = os.listdir(data_path)[0]
    logger.log('Load dictionary %s.' % dictionary_file)
    dictionary_file_full_path = os.path.join(data_path, dictionary_file)
    with io.open(dictionary_file_full_path, mode='a', encoding='utf-8') as f:
        updates = []
        for row in update_list:
            updates.append('\t'.join(row))
        f.write('\n' + '\n'.join(updates))
        logger.log('Added {} words into dictionary {}'.format(len(updates), dictionary_file))


if __name__ == '__main__':
    load_dictionary()
