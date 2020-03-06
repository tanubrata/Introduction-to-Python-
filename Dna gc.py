#Name:Tanubrata Dey
#Date:February 6, 2018
#This program prints:GC content in DNA string

DNAb = "AAATATATA"

l = len(DNAb)
print("The length is", l)

numC = DNAb.count('C')
numG = DNAb.count('G')

print('Number of C nucleotides is', numC)
print('Number of G nucleotides is', numG)

gc = (numC + numG) / l


print('gc-content is', gc)

DNAa = "ACGCCCGGGATG"

l = len(DNAa)
print("The length is", l)

numC = DNAa.count('C')
numG = DNAa.count('G')

print('Number of C nucleotides is', numC)
print('Number of G nucleotides is', numG)

gc = (numC + numG) / l


print('gc-content is', gc)





