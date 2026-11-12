from Bio import SeqIO

for record in SeqIO.parse("read.fasta", "fasta"):
    print(record)
    print("*"*30)