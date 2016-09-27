#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_csv import lib


def main():
    parser = argparse.ArgumentParser(
        description="csv ファイルからレコードを読み出します。")
    parser.add_argument(
        "path",
        help="csv ファイルのパス。")

    args = parser.parse_args()
    result = lib.get_record(args.path)

    if len(result) > 0:
        for record in result:
            print(" ".join(record))

if __name__ == "__main__":
    main()
