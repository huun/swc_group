

fastq_filtered: example.fastq
	cat example.fastq | paste - - - - | tre-agrep --show-position --color GGGAGGCCG > fastq_filtered_left
	cat example.fastq | paste - - - - | tre-agrep --show-position --color CCTCCCATA > fastq_filtered_right


