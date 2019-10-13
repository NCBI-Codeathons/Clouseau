#!/usr/bin/env python

import logging

logger = logging.getLogger(__name__)


class Chr(object):
    """ Chromosome Variant object """

    def __init__(self, chrom_name, position):
        self.chrom_name = chrom_name
        self.start = int(position)
        self.end = int(position)
        self.variants = {}

    # Update the start or end position if new variant is higher/lower
    def update_position(self, position, gap):
        # assuming ordered input check if next variant is too far away from current end position
        position = int(position)
        if position - self.end > gap:
            #logger.error('%s\t%s', self.chrom_name, position )
            pass
        if self.start > position:
            self.start = position
        elif self.end < position:
            self.end = position

    def add_variant(self, variant):
        if variant in self.variants:
            self.variants[variant] += 1
        else:
            self.variants[variant] = 1
