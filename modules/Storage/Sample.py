#!/usr/bin/env python

"""assume sort VCF after header, uniq"""

class Sample(object):
    """ Sample Object """

    def __init__(self, sample_name):
        self.sample_name = sample_name
        self.chr_list = []

    def add_chrom(self, chr_name, position, variant):
        if chr_name in self.chr_list:
            chr_name.update_position(pos)
            chr_name.add_variant(variant)
        else:
            chr_name = Chr.Chr(chr_name, position)
            self.chr_list.append(chr_name)
            chr_name.add_variant(variant)
