# blast_app

## Creating a blastable database

Sequences have been downloaded from NCBI proteins written in fasta format to ```blast_application/data/proteins.fasta```
Database was prepared using ```makeblastdb -dbtype prot -in proteins.fasta```

## Inspect rabbitmq

```docker-compose exec broker rabbitmqctl status```