import timeit

import requests


def get_orderbook():
    orderbook = requests.get("https://api.gemini.com/v1/book/btcusd").json()


n = 10
latency = timeit.timeit("get_orderbook()",
                        setup="from __main__ import get_orderbook",
                        number=n) * 1.0 / n


print("latency is {} ms".format(latency * 1000))


# curl -w "TCP handshake: %{time_connect}s, SSL handshake: %{
# time_appconnect}s\n" -so /dev/null https://www.gemini.com