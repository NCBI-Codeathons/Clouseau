#!/usr/bin/env python


class AllSamples:
    """
    This Class will contain all information about samples in VCF files
    Beside that It willcontAin info about chromosomes
    """
    def __init__(self, sample_list, chr_list):
        self.sample_list = sample_list
        self.chr_list = chr_list
        
