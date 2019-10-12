import pytest
import math
from random import randint
from modules.Storage import Chr

@pytest.fixture
def default_chr():
    chr_dict = {'name' :'test_chr_name', 'position': 25}
    return chr_dict


@pytest.fixture
def default_chr_1(default_chr):
    chr_dict = default_chr
    chr_dict['variant_type'] = 'variant1'
    return chr_dict


@pytest.fixture
def default_chr_2(default_chr):
    chr_dict = default_chr
    chr_dict['position'] = 50
    chr_dict['variant_type'] = 'variant1'
    return chr_dict


@pytest.fixture
def default_chr_object(default_chr_1):
    chrom_name = default_chr_1['name']
    position = default_chr_1['position']
    new_chr = Chr(chrom_name, position)
    variant_type = default_chr_1['variant_type']
    new_chr.add_variant(variant_type)
    return new_chr


@pytest.mark.unit
def test_init_chromosome(default_chr):
    chrom_name = default_chr['name']
    position = default_chr['position']
    new_chr = Chr(chrom_name, position)
    assert new_chr.chrom_name == 'test_chr_name'
    assert new_chr.start == 25
    assert new_chr.end == 25
    assert len(new_chr.variants) == 0


@pytest.mark.unit
def test_add_variant(default_chr_1):
    chrom_name = default_chr_1['name']
    position = default_chr_1['position']
    new_chr = Chr(chrom_name, position)
    variant_type = default_chr_1['variant_type']
    new_chr.add_variant(variant_type)
    assert len(new_chr.variants) == 1
    assert new_chr.variants['variant1'] == 1


@pytest.mark.unit
def test_update_position(default_chr_object, default_chr_2):
    position = default_chr_2['position']
    default_chr_object.update_position(position, 100)
    assert default_chr_object.start == 25
    assert default_chr_object.end == 50


@pytest.mark.unit
def test_update_variants(default_chr_object, default_chr_2):
    variant_type = default_chr_2['variant_type']
    default_chr_object.add_variant(variant_type)
    assert default_chr_object.variants['variant1'] == 2
