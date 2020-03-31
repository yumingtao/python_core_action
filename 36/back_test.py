from numbers import Number

import pandas as pd
import utils
from numpy import float64
from strategy import Strategy, SmaCross
import numpy


class ExchangeAPI:
    def __init__(self, data, cash, commission):
        utils.assert_msg(0 < cash,
                         "初始现金数量须大于0，输入现金数量: {}".format(cash))
        utils.assert_msg(0 <= commission <= 0.05,
                         "合理的手续费率一般不会超过5%，输入的费率:{"
                         "}".format(commission))
        self._initial_cash = cash
        self._data = data
        self._commission = commission
        self._position = 0
        self._cash = cash
        self._i = 0

    @property
    def cash(self):
        """
        :return: 返回当前账户现金数量
        """
        return self._cash

    @property
    def position(self):
        """
        :return: 返回当前账户仓位
        """
        return self._position

    @property
    def initial_cash(self):
        """
        :return: 返回初始现金数量
        """
        return self._initial_cash

    @property
    def market_value(self):
        """
        :return: 返回当前市值
        """
        return self._cash + self._position * self.current_price

    @property
    def current_price(self):
        """
        :return: 返回当前市场价格
        """
        return self._data.Close[self._i]

    def buy(self):
        """
        用当前账户剩余资金，按照市场价格全部买入
        :return:
        """
        self._position = float(
            self._cash * (1 - self._commission) / self.current_price)
        self._cash = 0.0

    def sell(self):
        """
        卖出当前账户剩余持仓
        :return:
        """
        self._cash += float(
            self._position * self.current_price * (1 - self._commission))
        self._position = 0.0

    def next(self, tick):
        self._i = tick

class BackTest:
    """
    回测类，用于读取历史行情数据，执行策略，模拟交易并估计收益。
    初始化的时候，调用Backtest.run
    """

    def __init__(self,
                 data: pd.DataFrame,  # pandas Dataframe格式的历史OHLCV数据
                 strategy_type: type(Strategy),  # 交易所API类型，负责执行买卖操作以及账户状态的维护
                 broker_type: type(ExchangeAPI),  # 策略类型
                 cash: float = 10000,  # 初始资金数量
                 commission: float = .0):  # 每次交易手续费率。如2%的手续费此处为0.02
        utils.assert_msg(issubclass(strategy_type, Strategy),
                         "strategy_type不是一个Strategy类型")
        utils.assert_msg(issubclass(broker_type, ExchangeAPI),
                         "broker_type不是一个ExchangeAPI类型")
        utils.assert_msg(isinstance(commission, Number),
                         "commission不是浮点类型数值")
        # False代表浅复制，没有内存拷贝
        data = data.copy(False)

        # 如果没有Volume列，填充NaN
        if "Volume" not in data:
            data["Volume"] = numpy.nan

        # 验证OHLC数据格式
        utils.assert_msg(len(data.columns &
                             {"Open", "High", "Low", "Close", "Volume"}) == 5,
                         "部分OHLC包含缺失值，请去掉那些行或者通过差值填充.")

        # 如果行情数据没有按时间排序，重新排序一下
        if not data.index.is_monotonic_increasing:
            data = data.sort_index()

        # 利用数据，初始化交易所对象和策略对象
        self._data = data
        self._broker = broker_type(data, cash, commission)
        self._strategy = strategy_type(self._broker, self._data)
        self._results = None

    def run(self) -> pd.Series:
        """
        运行回测，迭代历史数据，执行模拟交易并返回回测结果。
        :return:
        """
        strategy = self._strategy
        broker = self._broker

        # 策略初始化
        strategy.init()

        # 设置回测开始和结束位置
        start = 100
        end = len(self._data)

        # 回测主循环，更新市场状态，然后执行策略
        for i in range(start, end):
            # 注意要先把市场状态移动到第i时刻，然后再执行策略
            broker.next(i)
            strategy.next(i)

        # 计算结果并返回
        self._results = self._compute_result(broker)
        return self._results

    def _compute_result(self, broker):
        s = pd.Series(float64)
        s["初始市值"] = broker.initial_cash
        s["结束市值"] = broker.market_value
        s["收益"] = broker.market_value - broker.initial_cash

        return s


def main():
    BTCUSD = utils.read_file("BTCUSD_GEMINI.csv")
    ret = BackTest(BTCUSD, SmaCross, ExchangeAPI, 10000.0, 0.003).run()
    print(ret)


if __name__ == '__main__':
    main()

