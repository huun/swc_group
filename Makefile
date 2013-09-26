
#all: $(patsubst %.fastq, %_filtered.fastq, $(wildcard *.fastq))

clean:
	rm -f *.fastqmerged	*_filtered.fastq *.filteredreads

###python check fastq file format 
%_left.out: %.fastq
	cat $< | paste - - - - | tre-agrep --show-position GGGAGGCCG{#1} > $@
%_right.out: %.fastq
	cat $< | paste - - - - | tre-agrep --show-position CCTCCCATA{#1} > $@

##python to extract sequence left and right with a minimum length otherwise discard
%_left.filteredreads: %_left.out
	python filter_reads_wrapper.py $< > $@
%_right.filteredreads: %_right.out
	python filter_reads_wrapper.py $< > $@
## TODO: trim instead of filtering

%.new: %_left.filteredreads %_right.filteredreads
	cat $< | tr '\t' '\n' > $@

test:
	python test_filter.py
