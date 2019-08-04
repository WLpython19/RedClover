#!/bin/sh
module load bedtools

bedtools getfasta -fo $output_file -name -fi $reference_file -bed $custom_bed_file

