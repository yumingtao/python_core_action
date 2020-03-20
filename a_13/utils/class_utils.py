class Encoder1(object):
    @staticmethod
    def encode(s):
        return s[::-1]


class Decoder1(object):
    @staticmethod
    def decode(s):
        return "".join(reversed(list(s)))
