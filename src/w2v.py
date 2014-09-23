#!/usr/bin/env python3

"""
./w2v.py --corpus <filename> --output_vectors <filename> --output_model <filename>
"""

import gensim
import logging
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--corpus")
parser.add_argument("--output_vectors")
parser.add_argument("--output_model")
#parser.add_argument("--model")
args = parser.parse_args()



def TrainWord2VecModel(filename, min_count=5, workers=16):
  def ParseCorpus(filename):
    for line in open(filename):
      yield line.split()
  
  vocab = set()
  for line in ParseCorpus(filename):
    for word in line:
      vocab.add(word)
  model = gensim.models.Word2Vec(ParseCorpus(filename), min_count=min_count, workers=workers)
  return model, vocab


def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #if os.path.isfile(args.model):
    #    model = gensim.models.Word2Vec.load(args.model)
    model, vocab = TrainWord2VecModel(args.corpus, min_count=1, workers=16)
    model.save(args.output_model)
    output_vectors = open(args.output_vectors, "w")
    for word in vocab:
      output_vectors.write("{}\t{}\n".format(word, str(model[word])))


if __name__ == '__main__':
    main()






