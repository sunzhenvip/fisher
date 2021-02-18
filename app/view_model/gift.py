"""
 Created by sz on 2021/2/19
"""
__author__ = 'sz'

from collections import namedtuple

from app.view_model.book import BookViewModel

MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


class MyGifts:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list

        self.gifts = self.__parse()

    def __parse(self):
        temp_gifts = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        r = {
            'wishes_count': count,
            'book': BookViewModel(gift.book),
            'id': gift.id
        }
        return r
        # 下面代码有问题
        # MyGift(id=gift.id, book=BookViewModel(gift.book), wishes_count=count)
        # return my_gift.__reduce__()


class MyGift:
    def __init__(self):
        pass
