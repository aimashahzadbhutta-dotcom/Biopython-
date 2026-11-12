from Bio.Blast import NCBIWWW
from Bio import SeqIO

record = SeqIO.read("insulin_protein.fasta", "fasta")

print("Still processing")

result_handle = NCBIWWW.qblast("blastp", "swissprot", record.seq, hitlist_size=10)

with open("blast_result.xml", "w") as b:
    b.write(result_handle.read())

result_handle.close()
print("successfully created blast_result.xml file")
