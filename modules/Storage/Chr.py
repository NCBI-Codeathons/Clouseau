class Chr(object):
    """ Chromosome Variant object """

    def __init__(self, chrom_name, start, end):

        self.chrom_name = chrom_name
        self.start = start
        self.end = end
        self.variants = {}
