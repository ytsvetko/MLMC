def SortByYear(filename):
    #import os
    f = dict()    
    # sorting each line of the txt file to a new byYear file    
    filename = filename.split('.')[0]
    print filename
    for line in open(filename + '.txt', 'r'):
        line_year = int(line.split()[5])
        if line_year not in f:
            f[line_year] = open('a'+str(line_year)+'.txt','wb')
        f[line_year].write(line)
    # remove the extracted txt file
    # os.remove(filename+'.txt')
    
def main(filename):
    SortByYear(filename)