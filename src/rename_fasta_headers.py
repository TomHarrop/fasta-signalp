#!/usr/bin/env python3

from Bio import SeqIO
import csv

# load files
fasta_file = 'data/Trinity.fasta.transdecoder.pep'
records = list(SeqIO.parse(fasta_file, 'fasta'))

# declare dictionaries
pepid_to_id = {}
pepid_to_name = {}
pepid_to_desc = {}

# rename records, keep map of new id to old id
i = 0
for rec in records:
    i += 1
    # store old values in dictionaries
    pepid = 'PEP' + str(i)
    pepid_to_id[pepid] = rec.id
    pepid_to_name[pepid] = rec.name
    pepid_to_desc[pepid] = rec.description
    # replace values and rename
    rec.id = pepid
    rec.name = ''
    rec.description = ''

# generating list of new id to old id
result_lines = list([x, pepid_to_id[x], pepid_to_name[x], pepid_to_desc[x]]
                    for x in pepid_to_id.keys())

# write id mapping to file
header = ['pepid', 'id', 'name', 'desc']
with open('output/ids.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(result_lines)

# write renamed fasta
SeqIO.write(
    sequences=records,
    handle='output/renamed.fasta',
    format='fasta')
