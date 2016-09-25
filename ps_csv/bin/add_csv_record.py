#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_csv import lib


def main():
    parser = argparse.ArgumentParser(
        description="csv ファイルへレコードを追加します。")
    parser.add_argument(
        "path",
        help="csv ファイルのパス。")
    parser.add_argument(
        "record",
        nargs="+",
        help="csv へ追加するレコード。")
    args = parser.parse_args()

    lib.add_record(args.path, args.record)

if __name__ == "__main__":
    main()
