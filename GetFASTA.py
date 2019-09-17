# Description: Given BLAST Results CSV file, Program outputs a file of protein sequences in FASTA format
# Requires: Biopython
# Note: Input file and this file should be in the same location, Output file will be written in same location

def main ():
  from Bio import Entrez, SeqIO
  from Bio.Blast import NCBIWWW
  import csv,time,Bio,sys
    
#getting email
  startTime = time.time()
  Entrez.email = sys.argv[1]
  
  print("\n")
  print("Starting to get fasta files for each BLAST result, this might take a while...")
  #ask for input file and name of output file
  for fileName in ["2_" + sys.argv[3] + "_" + sys.argv[4] + "_BLAST"]:
    infile = fileName + ".csv"
    outfile = fileName + ".fasta"

  #open input file, use accension number to search entrez, and store relevant info
    with open(infile,'a') as csvfile:
      csvfile.write(sys.argv[2])
    with open(infile) as csvfile:
      readCSV = csv.reader(csvfile,delimiter = '\n')
      line_list = []
      for row in readCSV:
        print (row)
        try:
            handle = Entrez.efetch(db="protein", id=row[0], rettype="gb", retmode="text")
            record = SeqIO.read(handle, "genbank")                                         #stores results of search as record
            handle.close()
            line = str(">" + row[0] + record.description +"\n" + record.seq + "\n")        #record.description and record.seq refer to
            line_list.append(line)                                                         #store FASTA info in list
        except IndexError:                                                                 #index error indicates end of csv file
          print("break")
          break
        except:                                                                            #other errors indicate genbank file not found
          continue

  
  
  #write info in output file
    with open(outfile, "w") as fasfile:
      for line in line_list:
        fasfile.write(line)
    print("Done")
  endTime = time.time()
  print("\n")
  print("This took " + str(endTime-startTime) + " seconds to complete")
main()
