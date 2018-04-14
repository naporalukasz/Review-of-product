import nltk
import gensim

from gensim.models.keyedvectors import KeyedVectors

model = KeyedVectors.load_word2vec_format('D:/Magisterka/word2vec/v100m8.w2v.txt',binary=False)
model.save("word.txt")