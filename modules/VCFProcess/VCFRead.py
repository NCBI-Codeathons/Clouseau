

def open_handle(myfile):
    if opath.isfile(myfile):
        if myfile.endswith('vcf.gz'):
            import gzip
            return gzip.open(myfile, 'rt'), "fastq"
        elif myfile.endswith('fasta.gz'):
            import gzip
            return gzip.open(myfile, 'rt'), "fasta"
        elif myfile.endswith('.fasta',):
            return open(myfile, 'r'), 'fasta'
        elif myfile.endswith('.fastq'):
            return open(myfile, 'r'), 'fastq'
        else:
            sys.exit("This file {} is of unknow extesnion.".format(myfile))
    else:
        sys.exit("This file {} does not exist.".format(myfile))


class ReadVcf:
    """
    Read the vcf file based on the ending into chunks
    """

    def __init__(self, vcf_file):
        self.vcf_file = vcf_file

    @staticmethod
    def file_type(vcf_file):
        if vcf_file.endswith('vcf'):

