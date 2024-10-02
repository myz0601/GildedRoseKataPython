# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_backstage_sellin_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

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
