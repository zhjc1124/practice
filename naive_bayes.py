import numpy as np


class NBayes(object):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
        self.doclength = len(data)

        self.probs = {}
        self.indexs = {}
        self.cate_prob()

        self.vocabulary = set()
        for doc in data:
            for word in doc:
                self.vocabulary.add(word)
        self.vocabulary = list(self.vocabulary)

        self.idf = np.zeros(len(self.vocabulary))
        self.tf = np.zeros([self.doclength, len(self.vocabulary)])
        self.calc_freq()

        self.tdm = np.zeros([len(self.probs), len(self.vocabulary)])
        self.build_tdm()

        self.testset = None

    def cate_prob(self):
        i = 0
        for label in self.labels:
            if label in self.probs:
                self.probs[label] += 1
                self.indexs[label] = i
                i += 1
            else:
                self.probs[label] = 1
        self.probs /= len(self.labels)

    def calc_freq(self):
        for index in range(self.doclength):
            for word in self.data[index]:
                self.tf[index, self.vocabulary.index(word)] += 1
        self.idf = np.sum(self.tf, axis=0)
        # 以TF-IDF方式生成向量空间， 注释掉为普通词频
        self.tf = np.log2(self.doclength/self.idf) * self.idf

    def build_tdm(self):
        for i in range(len(self.labels)):
            index = self.indexs[self.labels[i]]
            self.tdm[index] += self.tf[i]
        self.tdm /= np.sum(self.tdm, axis=1)

    def map2vocab(self, testdata):
        self.testset = np.zeros(len(self.vocabulary))
        for word in testdata:
            self.testset[self.vocabulary.index(word)] += 1

    def predict(self, testdata):
        self.map2vocab(testdata)
        temp = np.sum(self.testset * self.tdm * self.probs, axis=1)
        index = temp.argmax()
        label = self.labels[index]
        return label


if __name__ == '__main__':
    from dataset import *
    nb = NBayes(data, labels)
    nb.cate_prob()

