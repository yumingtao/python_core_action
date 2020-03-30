import time
import _thread

import websocket


def on_message(ws, message):
    print("received : ", message)


def on_open(ws):
    def go():
        for i in range(5):
            time.sleep(0.01)
            msg = "{}".format(i)
            ws.send(msg)
            print("sent : ", msg)
        time.sleep(1)

        ws.close()
        print("websocket closed.")

    _thread.start_new_thread(go, ())


# pip install websocket_client
if __name__ == '__main__':
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                                on_message=on_message,
                                on_open=on_open)
    ws.run_forever()
