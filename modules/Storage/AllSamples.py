#!/usr/bin/env python

from Storage import Sample
from Storage import Chr


class AllSamples:
    """
    This Class will contain all information about samples in VCF files
    Beside that It willcontAin info about chromosomes
    """
    def __init__(self):
        self.sample_list = []
        self.chr_list = []

    def add_new_sample(self, sample_name):
        if sample_name in self.sample_list:
            pass
        else:
            sample = Sample.Sample()
            sample.name = sample_name

    def add_new_chr(self, chr_name, position):
        if chr_name in self.chr_list:
            pass
        else:
            my_chr = Chr.Chr(chr_name, position)
            self.chr_list.append(my_chr)
