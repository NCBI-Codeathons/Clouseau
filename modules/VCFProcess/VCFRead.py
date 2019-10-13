#!/usr/bin/env python

import multiprocessing as mp
import os
from modules import Storage


class ReadVcf(object):
    """
    Read the vcf file based on the ending into chunks
    """

    def __init__(self, vcf_file):
        self.vcf_file = vcf_file
        self.all_sample_storage = Storage.AllSamples()
        # print(self.all_sample_storage)
        self.sample_names = []

    @staticmethod
    def file_type(vcf_file):
        if vcf_file.endswith('vcf'):
            return('VCF')

    def process_wrapper(self, chunkStart, chunkSize):
        with open(self.vcf_file, 'rb') as f:
            f.seek(chunkStart)
            lines = f.read(chunkSize).splitlines()
            for line in lines:
                self.process_vcf(line)

    def chunkify(self, size=1024*1024):
        fileEnd = os.path.getsize(self.vcf_file)
        with open(self.vcf_file,'rb') as f:
            chunkEnd = f.tell()
            while True:
                chunkStart = chunkEnd
                f.seek(size,1)
                f.readline()
                chunkEnd = f.tell()
                yield chunkStart, chunkEnd - chunkStart
                if chunkEnd > fileEnd:
                    break

    def read_file(self, cores=1):
        pool = mp.Pool(cores)
        jobs = []
        # create jobs
        for chunkStart, chunkSize in self.chunkify():
            jobs.append( pool.apply_async(self.process_wrapper, (chunkStart, chunkSize)))
        # wait for all jobs to finish
        for job in jobs:
            job.get()
        # clean up
        pool.close()

    def process_vcf(self, vcf_line):
        vcf_line = vcf_line.decode("utf-8")
        line_split = vcf_line.split()
        if vcf_line.startswith("##"):
            pass
        elif vcf_line.startswith("#C"): # if it  is the header line
            sample_names = line_split[9:12]
            self.sample_names = sample_names
            # print(self)
            print("names from vcf >>> {}".format(sample_names))
            print(">>>>>>>>>>>>>> {}".format(self.sample_names))
            # adding samples to all samples object
            for sample in sample_names:
                # create object with sample name
                self.all_sample_storage.add_new_sample(sample)
        else: # sample already added now we are updating values
                chr = line_split[0]
                pos = line_split[1]
                inf = line_split[7]
                sv = inf.split(";")[8].split("=")[1] # Do a string match if SVTYPE not in 8th field
                samples_values = line_split[9:]
                self.all_sample_storage.add_new_chr(chr_name=chr, position=pos, variant=sv, gap=0)
                # get sample object by name
                for sample_name, sample_value in zip(self.sample_names, samples_values):
                    # get sample object
                    sample = self.all_sample_storage.sample_list[sample_name]
                    if sample_value != ".":
                        sample.add_new_chr(sample_name, chr_name=chr, position=pos, variant=sv, gap=0)
                        self.all_sample_storage.sample_list[sample_name] = sample


if __name__ == "__main__":
    all_sample = ReadVcf("/users/mmahmoud/home/projects/apps/VCF_QC/samples/new_test_10.vcf")
    # print(all_sample.__dict__)
