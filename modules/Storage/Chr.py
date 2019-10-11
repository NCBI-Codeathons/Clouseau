class Chr(object):
    """ Chromosome Variant object """

    def __init__(self, chrom_name, start, end):
        self.chrom_name = chrom_name
        self.start = start
        self.end = end
        self.variants = {}
        
    def add_variant(self, variant):
        if variant in self.variants:
            self.variants[variant] += 1
        else:
            self.variants[variant] = 1
