class Encoder(object):
    @staticmethod
    def encode(s):
        return s[::-1]


class Decoder(object):
    @staticmethod
    def decode(s):
        return "".join(reversed(list(s)))
