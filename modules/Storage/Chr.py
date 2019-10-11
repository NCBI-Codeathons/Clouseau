#!/usr/bin/env python

import logging

logger = logging.getLogger(__name__)


class Chr(object):
    """ Chromosome Variant object """

    def __init__(self, chrom_name, position):
        self.chrom_name = chrom_name
        self.start = position
        self.end = position
        self.variants = {}


    def update_position(self, position, gap):
        if self.start > position:
            diff_start_position = self.start - position
            self.start = position
        elif self.end < position:
            diff_end_position = self.end - position
            self.end = position

        if diff_start_position and abs(diff_start_position) > gap :
            logger.error('%s\t%s', self.chrom_name, position )
        elif diff_end_position and abs(diff_end_position) > gap :
            logger.error('%s\t%s\t', self.chrom_name, position )


    def add_variant(self, variant):
        if variant in self.variants:
            self.variants[variant] += 1
        else:
            self.variants[variant] = 1
