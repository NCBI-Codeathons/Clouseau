#!/usr/bin/env python


# receiving all samples
def output_all_samples(all_samples):
    sub_samples_list = all_samples.sample_list
    chr_list_for_allsamples = all_samples.chr_list
    varinat_list = max(sv for sv in chr_list_for_allsamples.keys().variant)


def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]


def sorted_chromosome(all_sample):
    """
    sorted_chromosome(AllSamples) -> list
    :return: list of chromosome found in all samples
    """
    sorted_chromosome = sorted(all_sample.chr_list.keys())
    return sorted_chromosome


def number_of_sample(all_sample):
    """
    number_of_sample(AllSamples) -> int
    :return: number of samples
    """
    print('Number of sample {0}'.format(len(sample_list)))


# def gender_check(sample):
#     """
#     gender_check(Sample) -> character
#     :return: M or F representing gender for individual samples
#     """
#     MALE_SIGNATURE = ['Y','y']
#
#     chromosome_list = sample.chr_name
#     #chromosome_list=['chr1','chr2']
#     chromosome_list = map(lambda x: remove_prefix(x,'chr'), chromosome_list)
#     chromosome_list = map(lambda x: remove_prefix(x, 'Chr'), chromosome_list)
#     first_chr_chrommosome_list = set(map(lambda x: x[0], chromosome_list))
#     if len(MALE_SIGNATURE.intersection(first_chr_chrommosome_list)) >0:
#         return 'M'
#     else:
#         return 'F'

def chromosome_start_stop(all_sample):
    """
    chromosome_start_stop(AllSamples) -> int
    :return: number of samples
    """
    sorted_chromosome = sorted_chromosome(all_sample)
    print('chromosome\tstart\tstop')
    for chromosome in sorted_chromosome:
        print('{chr}\t{start}\t{stop}'.format(chr=chromosome, start=all_sample.chr_list.start, stop=all_sample.chr_list.end))


def variant_per_chromosome(all_sample):
    pass

if __name__ == '__main__':
    pass