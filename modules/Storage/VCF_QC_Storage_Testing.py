import unittest
import math
from random import randint

#import storage classes to test

import Chr as chr_class

class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    name = 'test_chr_name'
    position1 = -1
    position2 = -1
    chr_variants = {}
    chr_objs = []

    # if chr_name in self.chr_list:
    #     chr_name.update_position(position)
    #     chr_name.add_variant(variant)
    # else:
    #     chr_name = Chr.Chr(chr_name, position)
    #     self.chr_list.append(chr_name)
    #     chr_name.add_variant(variant)
  

    # test case function to check the Chr init
    def test_0_init_chr(self):
        print("Start Chr Class Init test\n")
        #loop through a few times to allow checks of adding chrs
        for i in range(4):
            # make dummy values
            if i == 2:
                self.position1 = -1
            if i == 3:
                self.position1 = None
            if i == 4:
                self.position1 = 55234.2341
            else:
                self.position1 = int(math.exp(randint(1, 5))) * 30
            # check if init works
            chr_obj = chr_class.Chr(self.name + str(i), self.position1)
            self.chr_objs.append(chr_obj)
            self.assertEqual(chr_obj.chrom_name, self.name + str(i))
            self.assertEqual(chr_obj.start, self.position1)
            self.assertEqual(chr_obj.end, self.position1)
            self.assertIsInstance(chr_obj.start, int)
            self.assertIsInstance(chr_obj.end, int)
            self.assertIsInstance(chr_obj.chrom_name, str)

    def test_1_add_variant_chr(self):
        for i in range(4):
            self.position2 = int(math.exp(randint(1, 5))) * 30
            chr_obj =

    def test_2_update_chr(self):
        for i in range(6):
            # check if update position works
            chr_obj =
            self.position2 = int(math.exp(randint(1, 5))) * 30
            chr_obj.update_position(self.position2, 500)
            self.assertLogs()


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()