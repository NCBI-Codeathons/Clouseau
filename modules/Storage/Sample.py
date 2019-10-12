#!/usr/bin/env python

from modules.Storage import Chr

"""assume sort VCF after header, uniq"""

class Sample(object):
    """ Sample Object """

    def __init__(self):
        self.chr_list = {}

    def add_new_chr(self, chr_name, position, variant, gap):
        if chr_name in self.chr_list.keys():
            self.chr_list[chr_name].update_position(position, gap)
            self.chr_list[chr_name].add_variant(variant)
        else:
            chr_obj = Chr.Chr(chr_name, position)
            self.chr_list[chr_name] = chr_obj
            self.chr_list[chr_name].add_variant(variant)
