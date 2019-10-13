#!/usr/bin/env python

import sys
import os


def create_output_folder():
    path = os.getcwd()
    output_folder_name = 'results'
    output_path = os.path.join(path, output_folder_name)
    try:
         os.mkdir(output_path)
    except OSError:
        sys.exit("Creation of the directory {0} failed".format(output_path))
    else:
        print ("Successfully created the directory {0}".format(output_path))
    return output_path


def all_sv_type(all_samples):
    all_sv_composite_list = set()
    for chromosome in all_samples.chr_list.keys():
        all_sv_composite_list = all_sv_composite_list.union(all_samples.chr_list[chromosome].variants.keys())
    return sorted(list(all_sv_composite_list))


def sorted_chromosome(all_samples):
    """
    sorted_chromosome(AllSamples) -> list
    :return: list of chromosome found in all samples
    """
    sorted_chromosome_list = sorted(all_samples.chr_list.keys())
    return sorted_chromosome_list


def attribute_table(sample_name, sample, all_sv_list, sorted_chromosome_list,file):
    header = "{}\t{}\t{}\t{}".format("chr", "\t".join(all_sv_list), "start", "end")

    file.write(sample_name+'\n')
    file.write(header+'\n')
    for chromosome in sorted_chromosome_list:
        variant_count=[]
        for variant in all_sv_list:
            try:
                variant_count.append(sample.chr_list[chromosome].variants[variant])
            except KeyError:
                variant_count.append('0')

            file.write("{}\t{}\t{}\t{}\n".format(chromosome, "\t".join(map(str,(variant_count))),
                                          sample.chr_list[chromosome].start,
                                          sample.chr_list[chromosome].end))


# receiving all samples
def output_all_samples(all_samples):
    sub_samples_list = all_samples.sample_list
    sorted_chromosome_list = sorted_chromosome(all_samples)
    all_sv_list = all_sv_type(all_samples)
    print(sorted_chromosome_list)
    print(all_sv_list)
    output_folder_path = create_output_folder()

    output_file_path = os.path.join(output_folder_path, 'all_samples')

    with open(output_file_path, 'w') as file:
        attribute_table('all_samples', all_samples, all_sv_list, sorted_chromosome_list, file)

    # for sample in sub_samples_list:
    #     output_file_path=os.path.join(output_folder_path, sample)
    #     with open(output_file_path, 'w') as file:
    #         attribute_table(sample,all_samples.sample_list[sample],all_sv_list,sorted_chromosome_list,file)


def chromosome_start_stop(all_sample): # not currently use
    """
    chromosome_start_stop(AllSamples) -> int
    :return: number of samples
    """

    sorted_chromosome_list = sorted_chromosome(all_sample)
    print('chromosome\tstart\tstop')
    for chromosome in sorted_chromosome_list:
        print('{chr}\t{start}\t{stop}'.format(chr=chromosome, start=all_sample.chr_list.start, stop=all_sample.chr_list.end))



if __name__ == '__main__':
    pass