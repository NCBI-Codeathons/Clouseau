#!/usr/bin/env python


import os


def create_output_folder():
    path = os.getcwd()
    output_folder = 'results'

    try:
        os.mkdir(path, output_folder)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s" % path)
    return os.path.join(path, output_folder)


def Union(lsts):
    set_output=set()
    for lst in lsts:
        set_output = set_output.union(lst)
    return sorted(list(set_output))


def all_sv_type(all_samples):
    return Union(all_samples.chr_list.keys().variant.keys())


def attribute_table(sample_name, sample, all_sv_list):
    varinat_list = max(sv for sv in chr_list_for_allsamples.keys().variant.keys())
    header = "{}\t{}\t{}\t{}".format("chr", "\t".join(varinat_list), "start", "end")


# receiving all samples
def output_all_samples(all_samples):
    sub_samples_list = all_samples.sample_list
    for sample in sub_samples_list:
        # pass the sample name and sample object to Chi
        





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