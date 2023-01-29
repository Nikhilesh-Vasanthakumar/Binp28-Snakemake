# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:08:35 2023

@author: vnikh
"""
import io
import pandas as pd

with open("sample.vcf", 'r') as f:
    lines = [l for l in f if not l.startswith('##')]
    df= pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str},
        sep='\t'
    ).rename(columns={'#CHROM': 'CHROM'})


mylist=list(df["CHROM"])
with open("output.tsv",'w') as output:
    for count, elem in sorted(((mylist.count(e), e) for e in set(mylist)), reverse=True):
        print('%s\t(%d)' % (elem, count),file=output)