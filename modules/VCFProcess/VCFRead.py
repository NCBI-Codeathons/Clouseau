#!/usr/bin/env python

import multiprocessing as  mp



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
                chunkSize = chunkEnd - chunkStart
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
