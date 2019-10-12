#!/usr/bin/env python

from modules.Storage import Sample
from modules.Storage import Chr


class AllSamples:
    """
    This Class will contain all information about samples in VCF files
    Beside that It will contain info about chromosomes
    """
    def __init__(self):
        self.sample_list = {}
        self.chr_list = {}

    def add_new_sample(self, sample_name):
        if sample_name in self.sample_list.keys():
            pass
        else:
            sample = Sample.Sample()
            self.sample_list[sample_name] = sample

    def add_new_chr(self, chr_name, position, variant, gap):
        if chr_name in self.chr_list.keys():
            self.chr_list[chr_name].update_position(position, gap)
            self.chr_list[chr_name].add_variant(variant)
        else:
            chr_obj = Chr.Chr(chr_name, position)
            self.chr_list[chr_name] = chr_obj
            self.chr_list[chr_name].add_variant(variant)
