
#all: $(patsubst %.fastq, %_filtered.fastq, $(wildcard *.fastq))

clean:
	rm -f *.fastqmerged	*_filtered.fastq *.filteredreads

###python check fastq file format 
%.filtered: %.fastq
	cat $< | paste - - - - | tre-agrep --show-position GGGAGGCCG{#1} > $@_left.out
	cat $< | paste - - - - | tre-agrep --show-position CCTCCCATA{#1} > $@_right.out

##python to extract sequence left and right with a minimum length otherwise discard
%.filteredreads: %.out
	python filter_reads_wrapper.py $< > $@

## TODO: trim instead of filtering

%.new.fastq: %.filteredreads
	cat $< | tr '\t' '\n' > $@

test:
	python test_filter.py
