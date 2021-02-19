"""
 Created by sz on 2021/2/17
"""
__author__ = 'sz'

from app.view_model.book import BookViewModel


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)
        pass

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        # if single.create_time:
        #     time = single.create_time.strftime('%Y-%m-%d')
        # else:
        #     time = '未知'
        return dict(
            user_name=single.user.nickname,
            # time=time,
            time=single.create_datetime.strftime('%Y-%m-%d'),
            id=single.id,
        )


class MyTrades:
    def __init__(self, trades_of_mine, trade_count_list):
        self.trades = []
        self.__trades_of_mine = trades_of_mine
        self.__trade_count_list = trade_count_list
        self.trades = self.__parse()

    def __parse(self):
        temp_trades = []
        for trade in self.__trades_of_mine:
            my_trade = self.__matching(trade)
            temp_trades.append(my_trade)
        return temp_trades

    def __matching(self, trade):
        count = 0
        for trade_count in self.__trade_count_list:
            if trade_count['isbn'] == trade.isbn:
                count = trade_count['count']

        my_trade = {
            'wishes_count': count,
            'book': BookViewModel(trade.book),
            'id': trade.id
        }
        return my_trade
