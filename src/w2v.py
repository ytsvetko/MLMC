#!/usr/bin/env python3

"""
./w2v.py --corpus <filename> --output_vectors <filename> --output_model <filename>
"""

import gensim
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--corpus")
parser.add_argument("--start")
parser.add_argument("--end")
parser.add_argument("--output_model")
#parser.add_argument("--model")
args = parser.parse_args()


def ParseCorpora(filenames):
    for filename in filenames:    
        for line in open(filename):     
            # tagged case
            line_split = line.split()
            if all([len(line_split)==8, line.count('_') == 5, line.count('_.')==0]):
#                print line            
                comp_line = [w.split('_') for w in line_split[0:5]]
                if all([len(c)==2 for c in comp_line]):
                    [words,pos]= zip(*comp_line)
                    if all([len(pos)==5, all([p.isupper() for p in pos])]):
                        sent = list(words) + [line_split[6]]
              
            # non-tagged case
            elif all([len(line_split)==8, line.count('_') == 0]):
                sent = line_split[0:5] + [line_split[6]]
                    
            # Preprocessing: no numbers, special characters etc.
            if 'sent' in locals() or 'sent' in globals():
                if all([w.isalpha() for w in sent[0:5]]):
                    Sent = [w.lower() for w in sent[0:5]]
                    for i in range(int(sent[5])):
                        yield Sent

def ParseCorpus(filename):
    for line in open(filename):     
        # tagged case
        line_split = line.split()
        if all([len(line_split)==8, line.count('_') == 5, line.count('_.')==0]):
            #print line            
            [words,pos]= zip(*[w.split('_') for w in line_split[0:5]])
            if all([len(pos)==5, all([p.isupper() for p in pos])]):
                sent = list(words) + [line_split[6]]
          
        # non-tagged case
        elif all([len(line_split)==8, line.count('_') == 0]):
            sent = line_split[0:5] + [line_split[6]]
                
        # Preprocessing: no numbers, special characters etc.
        if 'sent' in locals() or 'sent' in globals():
            if all([w.isalpha() for w in sent[0:5]]):
                Sent = [w.lower() for w in sent[0:5]]
                for i in range(int(sent[5])):
                    yield Sent

#def ParseCorpora(filenames):    
#    if isinstance (filenames,list):
#        for filename in filenames:
#            yield ParseCorpus(filename)
#        else:
#            yield ParseCorpus(filename)
            


def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #if os.path.isfile(args.model):
    #    model = gensim.models.Word2Vec.load(args.model)
    
    if args.start > args.end:
        years = range(int(args.start), int(args.end),-1)
    else:
        years = range(int(args.start), int(args.end))
    print years
    model = gensim.models.Word2Vec(min_count=10, workers=16)
    filenames = [args.corpus + str(y) + '.txt' for y in years]
    model.build_vocab(ParseCorpora(filenames))

    for idx,y in enumerate(years):
        model.train(ParseCorpus(filenames[idx]))
        model.save(args.output_model + str(y))
                
    
      #output_vectors.write("{}\t{}\n".format(word, str(model[word])))


if __name__ == '__main__':
    main()