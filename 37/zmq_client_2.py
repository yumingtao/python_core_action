import zmq


def run():
    context = zmq.Context.instance()
    socket = context.socket(zmq.XSUB)
    socket.connect("tcp://127.0.0.1:6666")
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    print("client 2")
    while True:
        msg = socket.recv()
        print("msg: %s" % msg)


if __name__ == '__main__':
    run()

