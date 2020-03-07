#!/usr/bin/env python

#########################################################
##### Author: Renato Moreira Neto                   #####
##### Date: 03/06/2020                              #####
##### Version: 0.01                                 #####
##### App: Intact filter from PHASTER.CA files      #####
#########################################################

from os import path
import os
import argparse
import os.path


# Command line arguments.

desc = "Intact region filter from PHASTER.CA files"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument("-s", "--summary", default="summary.txt", help="Summary file from PHASTER.CA 'default=summary.txt'")
parser.add_argument("-r", "--regions", default="phage_regions.fna", help="Phage_regions file from PHASTER.CA 'default=phage_regions.fna'")
parser.add_argument("-o", "--output",default="kesita_vagabunda.txt", help="Output file with results from regions intacts 'default=kesita_vagabunda.txt'")
  
args = parser.parse_args()


####### Check if output file exists.

if os.path.isfile(args.output):
    print ("File already exists. Exiting!")
    exit(1)
    

####### Identify intact regions from file summary.txt

ids = []
string_to_search = 'intact('
list_of_results = []
# Open the file in read only mode
with open(args.summary, 'r') as read_file:
        # Read all lines in the file one by one
        for line in read_file:
            # For each line, check if line contains the string
            if string_to_search in line:
                # If yes, then store the ID
                list_of_results.append(line.split( )[0] + ' --> ' + line.split( )[4])
                ids.append(line.split( )[0])
               
 
####### Print IDs found.
print ("IDs found to collect")
print (ids)


####### Search IDs in the regions file phage_regions.fna

list_of_sequence = []
dna = []
collect = False
# Open the file in read only mode
with open(args.regions, 'r') as read_dna:
    # Search for ids in this file
    for i in ids:
        # Look this file from the start
        read_dna.seek(0)
        dna = (">" + i)
        # Read all lines in the file one by one
        for line in read_dna:
            # If it's an empty line, do nothing.(Used to collect all other lines besides the first)
            if line == '\n':
                collect = False
            # If ID found, start collect regions
            if dna in line:
                list_of_sequence.append( "\n\n\nRegion " + dna + "\n")
                collect = True
            # Collect entire sequence
            if collect == True:
                list_of_sequence.append(line.rstrip('/n'))                    

                    
###### Export to file.

f=open(args.output, "w+")
f.write("List of regions: ")
f.write("".join(list_of_sequence))
f.close()
print("Done! Your file is ready.")
            
