#!/usr/bin/env python3

"""
./change.py --corpus <filename> --output_vectors <filename> --output_model <filename>
"""

import gensim
import argparse
from scipy import spatial
import csv

parser = argparse.ArgumentParser()
parser.add_argument("--inputPrefix")
parser.add_argument("--words")
parser.add_argument("--year_points")
parser.add_argument("--output_csv")
#parser.add_argument("--model")
args = parser.parse_args()
print args
args.words = args.words.split('_')
args.year_points = args.year_points.split('_')
print args.words
print type(args.year_points)

# Define measures of interest
word2itself = dict()

for idx, y in enumerate(args.year_points):
    # load the model of each year
    model = gensim.models.Word2Vec.load(args.inputPrefix + y)
    # define reference year
    if y=='1750':
        model_ref = model
    # compute analysis of interest per word
    for w in args.words:
#        print model[y][w]        
#        word2itself[w].append()
#        print model[w].transpose()
        
        print [w, spatial.distance.cosine(model[w].transpose(),model[w].transpose()), spatial.distance.cosine(model_ref[w].transpose(),model[w].transpose())]

#f = open(args.output_csv,'wb')
#writing = csv.DictWriter(f,word2itself.keys())
#writing.writerows(word2itself)
#f.close()