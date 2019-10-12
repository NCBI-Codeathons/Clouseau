import pytest
import math
from random import randint
from Storage import Chr

@pytest.fixture
def default_chr():
    chr_dict = {'name' :'test_chr_name', 'position': 25}
    return chr_dict


@pytest.mark.unit
def test_init_chromosome(default_chr):
    chrom_name = default_chr['name']
    position = default_chr['position']
    new_chr = Chr.Chr(chrom_name, position)
    assert new_chr.chrom_name == 'test_chr_name'
    assert new_chr.start == 25
    assert new_chr.end == 25
    assert len(new_chr.variants) == 0
