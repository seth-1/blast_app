# blast_app

## Running the application

To run the application you'll need to:
* clone this github repository
* run ```docker-compose up```
* migrate the database ```docker-compose exec web python manage.py migrate```
* open firefox/ chrome or another browser and visit ```http://localhost:3000/```
* copy paste a DNA sequence and click **Submit** to create a BLASTx job
* The results will be displayed below the sequence input after refreshing the page

You can try the sequence submission with the following sequence:
```
ATGTTTAGAAAAAAATATACTAAAAAAATTAGTCCAACAGTTTTGTCAAAATTCCTAGAGCTTTACAAAG
ACAAGCAACCCAAATATGTTAAAATATTATTAAATAGATATAATAATCCATATCTTCGTACAAATCAAAC
GATCAAATCCCCTTTTCATACAAAGTCTTCAAAAAACAAATGTATTAAAAAAAATAAACATAGTATTAAA
AAATTAATTAATTTTTAA
```

# Data retrieval

## Creating a blastable database

Blast databases include proteins of the following NCBI entries: ​NC_000852, NC_007346, NC_008724, NC_009899, NC_014637, NC_020104, NC_023423, NC_023640, NC_023719, NC_027867.

Sequences have been downloaded from NCBI proteins written in fasta format to ```blast_application/data/proteins.fasta```
Database was prepared using ```makeblastdb -dbtype prot -in proteins.fasta```.

