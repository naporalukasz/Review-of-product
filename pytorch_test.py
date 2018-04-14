import os
import numpy as np
import re
import itertools
from collections import Counter

EMBEDDING_DIM = 100


def preperData():
    tokens = []
    file = open("rev_sentence.txt", encoding="utf8")
    for line in file:
        tokens.extend(line.split())

    file.close
    print(tokens)
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    # print(fileDir)

    filename = os.path.join(fileDir,
                            '../../word2vec/word2vec/v100m8w2v/w2v_kgr_nomwe/kgr_nomwe/cbow_v100m8_nomwe.w2v.txt')  # v100m8w2v.txt  test_file.txt
    filename = os.path.abspath(os.path.realpath(filename))
    # print(filename)

    f = open(filename, encoding="utf8")
    # sentences = f.readlines()
    print("Start read wector")
    embeddings_index = {}
    previousLine = ""
    intdex = 1
    for line in f:
        print(intdex)
        # print(line)
        intdex = intdex + 1
        if line.strip():
            splitLine = line.split()
            values = splitLine[1].split()
            word = splitLine[0]
            coefs = np.asarray(values[1:], dtype='float32')
            # if word in tokens:
            embeddings_index[word] = coefs
            # previousLine = ""

    f.close
    print("End read wector")

    # matchw2v = open("matchw2v.txt", encoding="utf8")

    # for k, v in embeddings_index.items():
    #    matchw2v.write(str(k) + ' >>> ' + str(v) + '\n\n')

    # matchw2v.close()

    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir,
                            '../../word2vec/word2vec/v100m8w2v/w2v_kgr_nomwe/kgr_nomwe/cbow_v100m8_nomwe.w2v.txt')  # v100m8w2v.txt  test_file.txt
    filename = os.path.abspath(os.path.realpath(filename))

    f = open(filename, encoding="utf8")
    print("Start read wector")
    embeddings_index = {}
    previousLine = ""
    intdex = 1
    for line in f:
        intdex = intdex + 1
        if line.strip():
            splitLine = line.split()
            values = splitLine[1].split()
            word = splitLine[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs

    f.close
    print("End read wector")

    print(embeddings_index)


def createEmmbedings():
    maxNumWord = 0
    tokens = []
    padding_word = " "
    print("Processing text data")

    sentences = list(open("rev_sentence.txt", encoding="utf8").readlines())
    sentences = [s.strip() for s in sentences]

    x_text = [s.split(" ") for s in sentences]

    # dodajemy sztuczne slowa do sentencji aby mialy taka sama dlugosc
    sequence_length = 1
    for x in x_text:
        if len(x) > sequence_length:
            sequence_length = len(x)

    padded_sentences = []
    for i in range(len(x_text)):
        sentence = x_text[i]
        num_padding = sequence_length - len(sentence)
        new_sentence = sentence + [padding_word] * num_padding
        padded_sentences.append(new_sentence)

    print("End processsing text data")

    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir,
                            '../../word2vec/word2vec/v100m8w2v/w2v_kgr_nomwe/kgr_nomwe/cbow_v100m8_nomwe.w2v.txt')  # v100m8w2v.txt  test_file.txt
    filename = os.path.abspath(os.path.realpath(filename))

    f = open(filename, encoding="utf8")
    print("Start read wector")
    embeddings_index = {}
    for line in f:
        if line.strip():
            splitLine = line.split()
            values = splitLine[1:]
            word = splitLine[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs

    f.close

    print("End read wector")

    embedding_matrix = np.zeros((len(sentences), EMBEDDING_DIM * sequence_length))
    counterLine = 0
    for words in padded_sentences:
        counterWord = 0
        for word in words:
            embedding_vector = embeddings_index.get(word)
            if embedding_vector is not None:
                index = 0
                while index < EMBEDDING_DIM - 1:
                    embedding_matrix[counterLine, counterWord + index] = embedding_vector[index]
                    index = index + 1
            print(embedding_matrix[counterLine])
            counterWord = counterWord + EMBEDDING_DIM
        counterLine = counterLine + 1

    np.savetxt('matchw2v.txt', embedding_matrix, delimiter=' ')


    return embedding_matrix

def getClassFromLabels():
    parents = list(open("rev_parents.txt", encoding="utf8").readlines())
    parents = [s.strip() for s in parents]

    labels = list(open("rev_labels.txt", encoding="utf8").readlines())
    labels = [s.strip() for s in labels]

    classLabelsForParent = np.zeros(len(parents))

    index = 0
    for parent in parents:
        parentIndex = parent.split().index('0')
        label = labels[index].split()
        classLabelsForParent[index] = label[parentIndex]
        index = index + 1

    return classLabelsForParent

def main():



if __name__ == "__main__":
    main()
