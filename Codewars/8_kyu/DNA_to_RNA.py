"""'GCAT'  =>  'GCAU'"""


def dna_to_rna(dna):
    rna = dna.strip()
    return ''.join(rna.replace('T', 'U'))


print(dna_to_rna('GCAT'))


def DNAtoRNA(dna):
    return dna.replace('T', 'U')


print(DNAtoRNA('GCAT'))
