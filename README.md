Phaster filter


Extract your result file from phaster.ca in same directory of this application.
Then, run application.
Your result file will be saved in same directory by default.
Result file contains all of regions marked as intact in the summary file.


usage: phaster-filter.py [-h] [-s SUMMARY] [-r REGIONS] [-o OUTPUT]

Intact region filter from PHASTER.CA files

optional arguments:
  -h, --help            show this help message and exit
  -s SUMMARY, --summary SUMMARY
                        Summary file from PHASTER.CA "default=summary.txt"
  -r REGIONS, --regions REGIONS
                        Phage_regions file from PHASTER.CA
                        "default=phage_regions.fna"
  -o OUTPUT, --output OUTPUT
                        Output file with results from regions intacts
                        "default=kesita_vagabunda.txt"
