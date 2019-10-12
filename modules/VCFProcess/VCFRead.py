#!/usr/bin/env python

import multiprocessing as  mp
from modules import Storage

all_sample_storage = Storage.AllSamples()
sample_names = []

def process(vcf_line):
    line_split = vcf_line.split()
    if vcf_line.statswith("#C"): # if it  is the header line
        sample_names = line_split[9:]
        # adding samples to allsamples object
        for sample in sample_names:
            # create object with sample name
            all_sample_storage.add_new_sample(sample)

    else: # sample already added now we are updating values
        chr = line_split[0]
        pos = line_split[1]
        inf = line_split[7]
        sv = inf.split(";")[8].split("=")[1] # Do a string match if SVTYPE not in 8th field
        samples_values = line_split[9:]
        all_sample_storage.add_new_chr(chr_name=chr, position=pos, variant=sv)
        # get sample object by name
        for sample_name, sample_value in zip(sample_names, samples_values):
            # get sample object
            sample_object = all_sample_storage[sample_name]
            if sample_value != ".":
                sample_object.add_new_chr(chr_name=chr, position=pos, variant=sv)




class ReadVcf:
    """
    Read the vcf file based on the ending into chunks
    """

    def __init__(self, vcf_file):
        self.vcf_file = vcf_file

    @staticmethod
    def file_type(vcf_file):
        if vcf_file.endswith('vcf'):
            return('VCF')

    def process_wrapper(self, chunkStart, chunkSize):
        with open(self.vcf_file) as f:
            f.seek(chunkStart)
            lines = f.read(chunkSize).splitlines()

            for line in lines:
                print(line)

    def chunkify(self, size=1024*1024):
        fileEnd = os.path.getsize(vcf_file)
        with open(self.vcf_file,'r') as f:
            chunkEnd = f.tell()
            while True:
                chunkStart = chunkEnd
                f.seek(size,1)
                f.readline()
                chunkEnd = f.tell()
                yield chunkStart, chunkEnd - chunkStart
                if chunkEnd > fileEnd:
                    break

    def read_file(self, cores=mp.cpu_count()):
        pool = mp.Pool(cores)
        jobs = []

        #create jobs
        for chunkStart,chunkSize in chunkify(self.vcf_file):
            jobs.append( pool.apply_async(process_wrapper,( chunkStart,chunkSize)) )

        #wait for all jobs to finish
        for job in jobs:
            job.get()

        #clean up
        pool.close()
