

clean:
	rm -f *.fastqmerged	*_filtered.fastq *.filteredreads

fastq_filtered: example.fastq
	###python check fastq file format 
	cat example.fastq | paste - - - - | tre-agrep --show-position GGGAGGCCG{#1} > fastq_filtered_left.fastqmerged
	cat example.fastq | paste - - - - | tre-agrep --show-position CCTCCCATA{#1} > fastq_filtered_right.fastqmerged

%.filteredreads: %.fastqmerged
	###python to extract sequence left and right with a minimum length otherwise discard
	python filter_reads.py $< > $@

## TODO: trim instead of filtering

%_filtered.fastq: %.filteredreads
	cat $< | tr '\t' '\n' > $@

test: 
	test_filter_reads.py test_input_left
	test_filter_reads.py test_input_right

	
