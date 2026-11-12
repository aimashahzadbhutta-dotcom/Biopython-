from Bio import SeqIO
from pathlib import Path
from Bio.Blast import NCBIWWW

Base = Path(__file__).resolve().parent.parent
result = SeqIO.read(Base / "fasta_files" / "insulin_protein.fasta" , "fasta")

# result_handle = NCBIWWW.qblast(
#     program = "blastp",
#     database = "nr",
#     sequence = result.seq
# )

# with open("blast_result.xml", "w") as b:
#     b.write(result_handle.read())

# print("Blast performed successfully !")
print(len(result))