def DNA_strand(dna):
    return ''.join('TAGC'['ATCG'.index(x)] for x in dna)


print(DNA_strand("AAAA"))


def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

print(DNA_strand("AAAA"))


pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])


print(DNA_strand("AAAA"))
