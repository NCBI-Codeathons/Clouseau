#!/usr/bin/python

import argparse
from modules.VCFProcess import VCFRead


def parse_args():
    '''Parse the input arguments.'''
    ap = argparse.ArgumentParser(description='Calculate summary stat for VCF')

    ap.add_argument('-i', '--input_file',
                    help='file name',
                    required=False)

    ap.add_argument('-g', '--gap-analysis',
                    help='Analyze gap of variation',
                    action='store_true')


    args = ap.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()
    write_object = VCFRead.process_vcf(args.input_file)
    print(write_object)
