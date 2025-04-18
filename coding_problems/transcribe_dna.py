"""
Transcribe the given DNA strand into corresponding mRNA - a type of RNA, that will be formed from it after transcription. DNA has the bases A, T, G and C, while RNA converts to U, A, C and G respectively.

Examples
dna_to_rna("ATTAGCGCGATATACGCGTAC") ➞ "UAAUCGCGCUAUAUGCGCAUG"

dna_to_rna("CGATATA") ➞ "GCUAUAU"

dna_to_rna("GTCATACGACGTA") ➞ "CAGUAUGCUGCAU"
"""

def dna_to_rna(dna):
    dict = {"A": "U", "T": "A", "C": "G", "G": "C"}
    ret = ""
    for letter in dna:
        ret += dict[letter]
    return ret

print(dna_to_rna("ATTAGCGCGATATACGCGTAC"))
print(dna_to_rna("CGATATA"))
print(dna_to_rna("GTCATACGACGTA"))
