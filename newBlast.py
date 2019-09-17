def main ():
  import time,sys,os
  from Bio import Entrez, SeqIO
  from Bio.Blast import NCBIWWW
  print("\n")
  print("Starting to get " + sys.argv[3] + " BLAST results/other sequences in the " + sys.argv[1] + " protein family")
  
  start = time.time()   
  for numHits in [sys.argv[3]]:
    print("\n")
    print("Getting " + numHits + " BLAST results/sequences for the " + sys.argv[1] + " protein family")
    relative_name = "1_" + sys.argv[1] +"_Ref_Seq.fasta"
    absolute_name = "/home/" + sys.argv[2] + "/outputFiles/" + relative_name
    fasta_string = open(absolute_name).read()
    print("fetching from blast")
    result_handle = NCBIWWW.qblast("blastp", "nr", fasta_string, hitlist_size=int(numHits))
    print("done fetching from blast")
    blast_result = open("2_"+ sys.argv[1] +"_" + numHits + "_BLAST.xml", "w")
    blast_result.write(result_handle.read())
    blast_result.close()
    result_handle.close()
    print("\n")
    print("Done getting " + numHits + " BLAST results/sequences for the " + sys.argv[1] + " protein family")
  end = time.time()
  print("\n")
  print("This took " + str(end-start) + " seconds to complete")
main()
