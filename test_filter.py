#!/usr/bin/env python

import filter_reads.py

filter_one_line("")

#def dna_starts_with(dna, prefix) :
#    if dna.startswith(prefix) :
#        return True
#    return False

#print dna_starts_with('actgggt', 'act')
#print dna_starts_with('actgggt', 'agt')

#assert dna_starts_with('a', 'a')
#assert dna_starts_with('at', 'a')
#assert dna_starts_with('at', 'at')
#assert not dna_starts_with('at', 't')


#Tests = [
#	['a',	'a',	True],
#    ['at',	'at',	True],
#    ['at',	'at',	True],
#    ['at',	't',	False],
#	['at',	't',	True]
#]

#passes = 0
#for (i, (seq, prefix, expected)) in enumerate(Tests) :
#	if dna_starts_with(seq,prefix) == expected :
#		passes += 1
#	else:
#		print('test %d failed'% i)
#print('%d of %d passed' % (passes, len(Tests)))

