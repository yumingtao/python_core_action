import re


class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, "r") as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception("process_corpus not implemented.")

    def search(self):
        raise Exception("search not implemented.")


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        # 对文件分词，保存到set
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        # 查询分词
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words_set in self.__id_to_words.items():
            if self.query_match(query_words, words_set):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query in query_words:
            # 只要有一个词不在里边，返回false
            if query not in words:
                return False
        return True

    @staticmethod
    def parse_text_to_words(text):
        text = re.sub('[^\w]', " ", text)
        text = text.lower()
        word_list = text.split(" ")
        word_list = filter(None, word_list)
        return set(word_list)


class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.inverted_index = {}
        self._parent_filed

    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(id)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        query_words_index = list()

        for query in query_words:
            query_words_index.append(0)

        # 如果不在反向索引，直接返回空
        for query in query_words:
            if query not in self.inverted_index:
                return []

        result = []

        while True:
            # 获取当前所有反向索引的index
            current_idxes = []
            for idx, query_word in enumerate(query_words):
                current_idx = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]

                # 遍历到某一个倒序索引的末尾，结束
                if current_idx >= len(current_inverted_list):
                    return result

                current_idxes.append(current_inverted_list[current_idx])
            # 判断current_idxes列表中的元素是否都相等
            # 如果都相等，表明查询的两个词都在该文档中出现了
            if all(x == current_idxes[0] for x in current_idxes):
                result.append(current_idxes[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue

            # 如果搜索的单词没有在同一个文档出现，找到最小的索引，找到最小索引对应单词在的下标位置，对其存储的值+1
            # 也就是说，在循环这个词反向索引列表的时候，来到了下一个反向索引值
            min_val = min(current_idxes)
            min_val_pos = current_idxes.index(min_val)
            query_words_index[min_val_pos] += 1

    @staticmethod
    def parse_text_to_words(text):
        text = re.sub('[^\w]', " ", text)
        text = text.lower()
        word_list = text.split(" ")
        word_list = filter(None, word_list)
        return set(word_list)


import pylru


class LRUCache(object):
    def __init__(self, size=32):
        self.cache = pylru.lrucache(size)

    def has(self, key):
        return key in self.cache

    def get(self, key):
        return self.cache[key]

    def set(self, key, val):
        self.cache[key] = val


class BOWInvertedIndexEngingWithCache(BOWInvertedIndexEngine, LRUCache):
    def __init__(self):
        # super(BOWInvertedIndexEngingWithCache, self).__init__()
        super().__init__()
        LRUCache.__init__(self)

    def search(self, query):
        if self.has(query):
            print("cache hit!")
            return self.get(query)

        # result = super(BOWInvertedIndexEngingWithCache, self).search(query)
        result = super().search(query)
        self.set(query, result)

        return result


def main(search_engine):
    for file_path in ["1.txt", "2.txt", "3.txt", "4.txt", "5.txt"]:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print("found {} result(s)".format(len(results)))
        for result in results:
            print(result)


if __name__ == '__main__':
    # simple_engine = SimpleEngine()
    # main(simple_engine)
    # bow_engine = BOWEngine()
    # main(bow_engine)
    # bow_inverted_idx_engine = BOWInvertedIndexEngine()
    # main(bow_inverted_idx_engine)
    bow_inverted_idx_engine_with_cache = BOWInvertedIndexEngingWithCache()
    main(bow_inverted_idx_engine_with_cache)
