from Bio import SeqIO

record = SeqIO.read("sequence.fasta", "fasta")
print(record.id)
print(record.description)
print(len(record.seq))

for rec in SeqIO.parse("sequence.fasta", "fasta"):
    print(rec.id)
    print(len(rec.seq))

record1 = SeqIO.read("keratin_protein.fasta", "fasta")
print(record1.seq)
print("*"*30)

record2 = SeqIO.read("albumin_protein.fasta", "fasta")
print(record2.seq)
print("*"*30)

record1 = SeqIO.read("myosin_protein.fasta", "fasta")
print(record1.seq)
print("*"*30)

record1 = SeqIO.read("actin_protein.fasta", "fasta")
print(record1.seq)
print("*"*30)
