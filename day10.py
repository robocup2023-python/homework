with open('codon.txt','r') as f:
    content=f.readlines()
condon_dict={}
for line in content:
    codon,amino_acid=line.strip().split()
    condon_dict[codon]=amino_acid

def transcript(dna_sequence):
    return dna_sequence.replace("T","U")
def translate(dna_sequence):
    mrna_sequence=transcript(dna_sequence)
    protein_sequence=""
    start_codon="AUG"
    if start_codon in mrna_sequence:
        start_index=mrna_sequence.index(start_codon)
        mrna_sequence=mrna_sequence[start_index:]
    for i in range(0,len(mrna_sequence),3):
        codon=mrna_sequence[i:i+3]
        if codon in condon_dict:
            amino_acid=codon_dict[codon]
            if amino_acid="stop":
                break
            protein_sequence+=amino_acid
    return protein_sequence
seq=""
for line in content:
    if line.startswith(">"):
        if seq_name !="":
            seq_dict[seq_name]=seq
            seq_name=line.strip()[1:]
            seq=""
        else:
            seq+=line.strip()
        seq_dict[seq_name]=seq

protein_dict[seq_name]=translate(seq)
with open("protein.txt","w") as file:
    for seq_name,protein_sequence in protein_dict.items():
        file.write(seq_name+":"+protein_sequence+"\n")

