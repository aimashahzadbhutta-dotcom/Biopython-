from Bio import SeqIO

record = SeqIO.read("sequence.gb", "genbank")
for feature in record.features:
    print(feature.location, feature.type)

for feature in record.features:
    print(feature.type)