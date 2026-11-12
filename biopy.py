from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# dna = Seq("ATGCAA")
# print(type(dna))
# record = SeqRecord(
#     dna,
#     "seq01",
#     "Example seq01",
#     "1st seq for dna"
# )

# print(record)

# print(dna.complement())
# reversed_dna = dna.complement()
# print(reversed_dna.transcribe())
# print(dna.transcribe())

# new_record = SeqRecord(
#     dna,
#     id="Gene1",
#     description="Sample gene sequence"
# )

# print(new_record)

dna1 = Seq("ATGC")
record1 = SeqRecord(
    dna1,
    id = "GeneA"
)

dna2 = Seq("TTAA")
record2 = SeqRecord(
    dna2,
    id = "GeneB"
)

my_list = [record1, record2]
for data in my_list:
    print(data)

