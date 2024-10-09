# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class UpdateBehavior(ABC):
    @abstractmethod
    def update_quality(self, item: Item):
        pass


class NormalItem(UpdateBehavior):
    def update_quality(self, item: Item):
        if item.quality > 0:
            item.quality -= 1

        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class AgedBrie(UpdateBehavior):
    def update_quality(self, item: Item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1


class BackstagePasses(UpdateBehavior):
    def update_quality(self, item: Item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1

        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0


class Conjured(UpdateBehavior):
    def update_quality(self, item: Item):
        if item.quality > 0:
            item.quality -= 2

        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                AgedBrie().update_quality(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                continue
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                BackstagePasses().update_quality(item)
            elif item.name == "Conjured":
                Conjured().update_quality(item)
            else:
                NormalItem().update_quality(item)
