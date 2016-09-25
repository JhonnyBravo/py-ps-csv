# coding: utf-8

import os
import sys
import codecs
import csv


def test_path(path):
    if not os.path.isfile(path):
        print(path + " は存在しません。")
        sys.exit(1)


def get_record(path):
    test_path(path)

    with codecs.open(path, "r", encoding="utf-8")as file:
        result = []
        obj_csv = csv.reader(file)

        for record in obj_csv:
            result.append(record)

    return result


def add_record(path, record):
    with codecs.open(path, "at", encoding="utf-8")as file:
        obj_csv = csv.writer(file)
        obj_csv.writerow(record)
