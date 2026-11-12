from Bio.Blast import NCBIXML
from pathlib import Path

Base = Path(__file__).resolve().parent
xml_file = Base / "blast_result.xml"
with open(xml_file) as b:
    blast_record = NCBIXML.read(b)

first_alignment = blast_record.alignments[9]

# print("Number of alignments: ", len(blast_record.alignments))
# print("Title of 1st alignment:" ,first_alignment.title)
# print("Length of 1st alignment:" ,first_alignment.length)

# print("Title of all alignments for insulin protein: ")
# for alignment in blast_record.alignments:
#     print(alignment.title)
#     print("*" * 20)

hsp_1st_alignment = first_alignment.hsps[0]
print("Extracing information of a particular Highest Scoring Segment pair: ( the hsp of the first alignment):")

print("Score: ", hsp_1st_alignment.score)
print("Expect: ", hsp_1st_alignment.expect)
print("Querry sequence: ", hsp_1st_alignment.query)
print("Query range:", hsp_1st_alignment.query_start, "-", hsp_1st_alignment.query_end)
print("Subject sequence: ", hsp_1st_alignment.sbjct)
print("Alignment sequence: ", hsp_1st_alignment.match)
print("Subject range:", hsp_1st_alignment.sbjct_start, "-", hsp_1st_alignment.sbjct_end)
