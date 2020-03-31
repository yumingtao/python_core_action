import abc
from typing import Callable
from utils import crossover, SMA, assert_msg


import numpy


class Strategy(metaclass=abc.ABCMeta):
    """
    抽象策略类，用户定义交易策略

    如果要定义自己的策略类，需要继承这个基类，并实现两个抽象方法：
    Strategy
    """

    def __init__(self, broker, data):
        """
        构造策略对象。

        :param broker: ExchangeAPI  交易API接口，用于模拟交易
        :param data: list           行情数据
        """
        self._indicators = []
        self._broker = broker
        self._data = data
        self._tick = 0

    def I(self, func: Callable, *args) -> numpy.ndarray:
        """
        计算买卖指标向量。
        买卖指标向量是一个数组，长度和历史数据对应；
        用于判定这个时间点上需要进行"买"还是"卖"
        :param func:
        :param args:
        :return:
        """
        value = func(*args)
        value = numpy.asarray(value)
        assert_msg(value.shape[-1] == len(self._data.Close),
                             "指示器长度必须和data长度相同")
        self._indicators.append(value)
        return value

    @property
    def tick(self):
        return self._tick

    @abc.abstractmethod
    def init(self):
        """
        初始化策略。
        在策略回测/执行过程中调用一次，用于初始化策略内部状态。
        也可以预计算策略的辅助参数，比如根据历史行情数据：
        计算买卖的指示器向量；
        训练模型/初始化模型参数
        """
        pass

    @abc.abstractmethod
    def next(self):
        """
        步进函数，执行第tick步的策略。
        tick代表当前的时间，比如data[tick]用于访问当前的市场价格
        """
        pass

    def buy(self):
        self._broker.buy()

    def sell(self):
        self._broker.sell()

    @property
    def data(self):
        return self._data


class SmaCross(Strategy):
    # 小窗口SMA的窗口大小，用于计算SMA快线
    fast = 30

    # 大窗口SMA的窗口大小，用于计算SMA慢线
    slow = 90

    def init(self):
        # 计算历史上每个时刻的快线和慢线
        self.sma1 = self.I(SMA, self.data.Close, self.fast)
        self.sma2 = self.I(SMA, self.data.Close, self.slow)

    def next(self, tick):
        # 如果此时快线刚好越过慢线，买入全部
        if crossover(self.sma1[:tick], self.sma2[:tick]):
            self.buy()

        # 如果是慢线刚好越过快线，卖出全部
        elif crossover(self.sma2[:tick], self.sma1[:tick]):
            self.sell()

        # 否则，这个时刻不执行任何操作。
        else:
            pass