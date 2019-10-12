#!/usr/bin/env python

#from Storage import Sample
#from Storage import Chr
#from Storage import AllSamples


def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

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

def gender_check(sample):
    """
    gender_check(Sample) -> character
    :return: M or F representing gender for individual samples
    """
    MALE_SIGNATURE = ['Y','y']

    chromosome_list = sample.chr_name
    #chromosome_list=['chr1','chr2']
    chromosome_list = map(lambda x: remove_prefix(x,'chr'), chromosome_list)
    chromosome_list = map(lambda x: remove_prefix(x, 'Chr'), chromosome_list)
    first_chr_chrommosome_list = set(map(lambda x: x[0], chromosome_list))
    if len(MALE_SIGNATURE.intersection(first_chr_chrommosome_list)) >0:
        return 'M'
    else:
        return 'F'


if __name__ == '__main__':
    gender_check(2)
