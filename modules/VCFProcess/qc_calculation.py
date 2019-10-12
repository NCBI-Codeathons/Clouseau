#!/usr/bin/env python

from Storage import Sample
from Storage import Chr
from Storage import AllSamples

def chromosome_check(all_sample):
    """
    chromosome_check(AllSamples) -> list
    :return: list of chromosome found in all samples
    """
    return all_sample.chr_list


def number_of_sample(all_sample):
    """
    number_of_sample(AllSamples) -> int
    :return: number of samples
    """
    return len(sample_list)

