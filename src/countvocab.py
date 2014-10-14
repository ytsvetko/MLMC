#!/usr/bin/env python3

"""
./countvocab.py --file <filename> --output <filename>
"""
import argparse
#from collections import Counter
import time
import pickle
#import re

parser = argparse.ArgumentParser()
parser.add_argument("--file")
parser.add_argument("--output")
#parser.add_argument("--model")
args = parser.parse_args()

start_time = time.ctime()


vocab = dict()
vocab_set = set(vocab)

for line in open(args.file):
    line_split = line.split()
    line_ = line.count('_') # count underscores, for the tagged case
    sent = []
    
    if len(line_split)==8:

        # untagged case
        if line_ == 0:
            sent = line_split[0:5] + [line_split[6]]


        # tagged case
        elif all([line_ == 5, line.count('_.')==0]):
            comp_line = [w.split('_') for w in line_split[0:5]]
            if all([len(c)==2 for c in comp_line]):
                [words,pos]= zip(*comp_line)
                if all([len(pos)==5, all([p.isupper() for p in pos])]):
                    sent = list(words) + [line_split[6]]

#        using regular expression actually slowed down the performace
#        elif line.count('_') == 5:
#            tagged = [bool(re.match(r'([a-zA-Z]+)_([A-Z]*$)',w)) for w in line_split[0:5]]
#            if all(tagged):
#                [words,pos]= zip(*[w.split('_') for w in line_split[0:5]])
#                sent = list(words) + [line_split[6]]
        
      
            
    # count words #if sent==0 it means none of the formar ifs were true
    if len(sent)>0:
        if all([w.isalpha() for w in sent[0:5]]):
#            print sent
            sent[0:5] = [w.lower() for w in sent[0:5]]
            for w in sent[0:5]:
                if w in vocab_set:
                    vocab[w] += int(sent[5])
                else:
                    vocab[w] = int(sent[5])
                    vocab_set.add(w)
            
#f=open(args.output,'w')
#f.writelines('{0}={1}\n'.format(k,v) for k,v in vocab.items())
#f.close()
#print vocab
#print len(vocab)
f=open(args.output,'wb')
pickle.dump(vocab,f)
f.close()


print [start_time,time.ctime()]