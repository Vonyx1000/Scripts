from Bio import Entrez, SeqIO
import sys
Entrez.email = sys.argv[1]
proteinName = sys.argv[2]
accessionNum = sys.argv[3]
print("Starting to fetch the Reference Sequence for the protein associated with the accession number:",accessionNum)
download_handle = Entrez.efetch(db="protein", id=accessionNum, rettype="fasta", retmode="text")
data = download_handle.read()
download_handle.close()

# Store data into file:
out_handle = open("1_"+ proteinName +"_Ref_Seq.fasta", "w")
out_handle.write(data)
out_handle.close()
print ("\n")
print("Done getting Reference Sequence!")
