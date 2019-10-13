#!/usr/bin/env python

import multiprocessing as  mp
import os
from modules import Storage


class ReadVcf(object):
    """
    Read the vcf file based on the ending into chunks
    """

    def __init__(self, vcf_file):
        self.vcf_file = vcf_file
        self.all_sample_storage = Storage.AllSamples()
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
                print("pro")
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

        #create jobs
        for chunkStart,chunkSize in self.chunkify():
            jobs.append( pool.apply_async(self.process_wrapper,(chunkStart,chunkSize)) )

        #wait for all jobs to finish
        for job in jobs:
            job.get()

        #clean up
        pool.close()

    def process_vcf(self, vcf_line):
        vcf_line = vcf_line.decode("utf-8")
        line_split = vcf_line.split()
        if vcf_line.startswith("##"):
            pass
        elif vcf_line.startswith("#C"): # if it  is the header line
            print(vcf_line)
            sample_names = line_split[9:]
            print(sample_names)
            self.sample_names = sample_names


            # adding samples to allsamples object
            for sample in sample_names:
                # create object with sample name
                self.all_sample_storage.add_new_sample(sample)


if __name__ == "main":
    all_sample = ReadVcf("/users/mmahmoud/home/projects/apps/VCF_QC/samples/samples/new_test_10.vcf")
    all_sample.read_file()
    print(all_sample.sample_names)
