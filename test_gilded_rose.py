# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_quality_not_over_50(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(50, items[0].quality)

    def test_Conjured_quality_degrade_twice(self):
        items = [Item("Conjured", 2, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(38, items[0].quality)

    def test_Conjured_quality_degrade_twice_when_negative(self):
        items = [Item("Conjured", -1, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-2, items[0].sell_in)
        self.assertEquals(36, items[0].quality)


if __name__ == '__main__':
    unittest.main()
