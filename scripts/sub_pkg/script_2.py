#!/usr/bin/env python3
# coding: utf-8

# SPDX-FileCopyrightText: 2022 Krzysztof Królczyk
#
# SPDX-License-Identifier: GPL-3.0-or-later

""" xxxxx """

import argparse
import sys
import os
import logging
import script_3

parser = argparse.ArgumentParser(description='')
parser.add_argument('-o', '--output-file', action='store',
                    help='Path where to save the JSON ouptut. Default: stdout')
parser.add_argument('-v', '--verbosity', action='store', default="ERROR",
                    help='Verbosity level, default: ERROR')


def main(args):
    return script_3.convert(vars(args))


if __name__ == "__main__":
    sys.exit(main(parser.parse_args()))
