import time

import zmq

# 多个publisher的模式参考XPUB/XSUB
# https://blog.csdn.net/weixin_43214364/article/details/82811095
def run():
    context = zmq.Context.instance()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:6666")

    print("publisher 1")
    cnt = 1
    while True:
        time.sleep(1)
        socket.send_string("server1 cnt{}".format(cnt))
        print("send {}".format(cnt))
        cnt += 1


if __name__ == '__main__':
    run()
