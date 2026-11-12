from Bio.Seq import Seq

genome_list = [
    Seq("ATTCCG"),
    Seq("N" * 5),
    Seq("TTCGACGGCAAT")
]

genome_list[1] = Seq("ATCGG")
complete_genome = sum(genome_list, Seq(""))
print(complete_genome)