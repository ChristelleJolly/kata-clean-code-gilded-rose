# -*- coding: utf-8 -*-
import unittest
from gilded_rose import *
from difflib import Differ

class GildedRoseTextTest(unittest.TestCase):

    def _write_result_file(self, days):
        with open("tests/result.txt", "w+") as res_file:
            res_file.write("OMGHAI!\n")
            items = [
                    Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
                    Item(name="Aged Brie", sell_in=2, quality=0),
                    Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
                    Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                    Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
                    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
                    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
                    Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
                    ]

            for day in range(days + 1):
                res_file.write("-------- day %s --------\n" % day)
                res_file.write("name, sellIn, quality\n")
                for item in items:
                    res_file.write(repr(item) + "\n")
                res_file.write("\n")
                GildedRose(items).update_quality()

    def test_thirty_days_same_result_as_golden_master(self):
        self._write_result_file(30)
        identical = True
        with open("tests/expected_result.txt", "r") as exp_res, open("tests/result.txt", "r") as res:
            differ = Differ()
            for line in differ.compare(exp_res.readlines(), res.readlines()):
                if not line.startswith(" "):
                    print(line)
                    identical = False
                    break
        self.assertTrue(identical)

        
if __name__ == '__main__':
    unittest.main()