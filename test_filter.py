#!/usr/bin/env python

from filter_reads import filter_one_line


Tests = [
	['8-38:@SRR073560.13773 HWI-EAS406:7:1:665:418 length=152	GGAAATGCCATGATAGGTAGGTATGGTGGCTGGTTTGAGGGAGGCCTATGGTGGGGGGGTGGT',	True, '@SRR073560.13773 HWI-EAS406:7:1:665:418 length=152	GGAAATGCCATGATAGGTAGGTATGGTGGCTGGTTTGAGGGAGGCCTATGGTGGGGGGGTGGT'],
    ['189-198:@SRR073560.13773 HWI-EAS406:7:1:665:418 length=152	GGAAATGCCATGATAGGTAGGTATGGTGGCTGGTTTGAGGGAGGCCTATGGTGGGGGGGTGGT',	True, ''],
    ['0-10:@SRR073560	ATGATGTGGTGAAATTTAGAG',	True, ''],
    ['100-130:@SRR073560	ATGATGTGGTGAAATTTAGAG',	False, '@SRR073560	ATGATGTGGTGAAATTTAGAG'],
#    ['',	False, ''],
#    ['',	False, ''],
#	['',	False, '']
]

passes = 0
for (i, (seq, prefix, expected)) in enumerate(Tests) :
	if filter_one_line(seq,prefix) == expected :
		passes += 1
	else:
		print('test %d failed'% i)
print('%d of %d passed' % (passes, len(Tests)))




