#!/usr/bin/env python

#########################################################
##### Author: Renato Moreira Neto                   #####
##### Date: 03/10/2020                              #####
##### Version: 0.02                                 #####
##### App: Intact filter from PHASTER.CA files      #####
#########################################################

import os
import argparse


####### Command line arguments.
desc = 'Intact region filter from PHASTER.CA files'
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-s', '--summary', default='summary.txt', help='Summary file from PHASTER.CA "default=summary.txt"')
parser.add_argument('-r', '--regions', default='phage_regions.fna', help='Phage_regions file from PHASTER.CA "default=phage_regions.fna"')
parser.add_argument('-o', '--output', default='kesita_vagabunda.txt', help='Output file with results from regions intacts "default=kesita_vagabunda.txt"')
  
args = parser.parse_args()


####### Check if output file exists.
if os.path.isfile(args.output):
    print ('Output file already exists. Exiting!')
    exit(1)
    

####### Identify intact regions from file summary.txt
ids = []
string_to_search = 'intact('
list_of_results = []
####### Open the summary file in read only mode.
with open(args.summary, 'r') as readFileId:
        # Read all lines in the file one by one.
        for line in readFileId:
            # For each line, check if line contains the string.
            if string_to_search in line:
                # If yes, then store the ID.
                ids.append(line.split( )[0])
               
 
####### Print IDs found.
print ('Regions ID found to collect:', ids)


####### Parse regions function.
def parse_region(s):
    tmp = s.lstrip('\n').rstrip().split('\n', 2)
    header = tmp[0].split('\t')
    body = '\n'.join(tmp[2:])
    return {
        'id': header[0].lstrip('>'),
        'position': header[1],
        'sequence': body
    }


####### Open .fna file in read only mode.
list_of_sequence = []
with open(args.regions, 'r') as readFileRegions:
    ####### Map informations from file.
    seq = map(parse_region, readFileRegions.read().strip().split('\n\n'))
    for i in seq:
        ####### Find IDs from summary in .fna file.
        if i['id'] in ids:
            list_of_sequence.append('\n\nRegion: ')
            list_of_sequence.append(i['id'])
            list_of_sequence.append('\nPosition:')
            list_of_sequence.append(i['position'])
            list_of_sequence.append('\n\n')
            list_of_sequence.append(i['sequence'])
            list_of_sequence.append('\n------------------------------------------------------')

                             
###### Export results to file.
with open(args.output, 'w+') as fResult:
    fResult.write('Regions position by ID')
    fResult.write(''.join(list_of_results))
    fResult.write('\n\nList of regions: ')
    fResult.write(''.join(list_of_sequence))

print('Done! Your file "'+args.output+'" is ready.')
