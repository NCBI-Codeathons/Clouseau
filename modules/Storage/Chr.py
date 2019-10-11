class Chr(object):
    """ Chromosome Variant object """

    def __init__(self, chrom_name, pos):
        self.chrom_name = chrom_name
        self.start = pos
        self.end = pos
        self.variants = {}

    def update_position(self, pos):
        if self.start > pos:
            self.start = pos
        elif self.end < pos:
            self.end = pos

    def add_variant(self, variant):
        if variant in self.variants:
            self.variants[variant] += 1
        else:
            self.variants[variant] = 1
