from os import path
import pandas as pd


def assert_msg(condition, msg):
    if not condition:
        raise Exception(msg)


def read_file(filename):
    filepath = path.join(path.dirname(__file__), filename)

    assert_msg(path.exists(filepath), "file is not exist.")

    return pd.read_csv(filepath, index_col=0, parse_dates=True,
                       infer_datetime_format=True)


def SMA(values, n):
    """
    返回简单滑动平均
    """
    return pd.Series(values).rolling(n).mean()


def crossover(series1, series2) -> bool:
    """
    检查两个序列是否在结尾交叉
    :param series1:  序列1
    :param series2:  序列2
    :return:         如果交叉返回True，反之False
    """
    return series1[-2] < series2[-2] and series1[-1] > series2[-1]

# BTCUSD = read_file("BTCUSD_GEMINI.csv")
# assert_msg(BTCUSD.__len__() > 0, "read file failed.")
# print(BTCUSD.head())
