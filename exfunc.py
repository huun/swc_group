#!/usr/bin/env python
import sys

input=sys.argv
   
def gc_content(input_file):
    reader=open(input_file, 'r')
    line = reader.readline();
    iD=''
    dict3={}
    while line != '' :
        if line.startswith('>'):
            iD = line[1:].replace('\n','')
            count += 1
        else :
            line=line.replace('N','')
            dict3['C']=line.count('C')
            dict3['G']=line.count('G')
            total += len(line)
            print iD, float(dict3['G']+dict3['C']) / float(len(line)), "len=", len(line)
        line = reader.readline();           
    reader.close()    

    print '\n', count, "sequences in the file"
    #return float(dict3['G']+dict3['C']) / float(len(input_string)), len(input_string)

gc_content('fasta.fa')


def gc_cont(dna): 
    dict3={}
    dict3['C']=dna.count('C')
    dict3['G']=dna.count('G')
    total = len(dna)
    print float(dict3['G']+dict3['C']) / float(len(dna)), "len=", len(dna)


#def gc_content_multiline_fasta(input_file):
#    reader=open(input_file, 'r')
#    line = reader.readline();
#    total = 0
#    count = 0
#    iD=''
#    dict3={}
#    fasta=''    
#    while line != '' :
#        if line.startswith('>'):
#            if fasta != '':
#                print iD
#                print fasta
#                gc_cont(fasta)
#            iD = line[1:].replace('\n','')
#            count += 1
#            fasta=''
#        else :
#            fasta+=line.replace('N','').replace('\n','')           
#        line = reader.readline();           
#    reader.close()    
#    print iD
#    print fasta
#    gc_cont(fasta)
#    print '\n', count, "sequences in the file"
#    #return float(dict3['G']+dict3['C']) / float(len(input_string)), len(input_string)

gc_content_multiline_fasta('fasta2.fa')
