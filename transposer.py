#Description: This program takes in an aligned .aln and .fasta/.fa file and transposes it such that
# the rows become columns and vice versa. So after running this, the output file has each row being
# a different amino acid position and each column corresponding to another sequence.
# Fun Fact: This program has linear algorithmic complexity, so it is pretty quick!  

def main():

#This section of code opens the original .aln of .fasta file and opens a new file that will be worked
#upon hence the name wipAlnFile (W.ork I.n P.rogress)

    fileName = "4_GDF9_250_MAFFT.fasta" 
    alnFile = open(fileName, mode='r')
    wipAlnFile = open('wipAlign.aln', mode='w') 
 
# Here, we copy the original .aln/.fasta file into a list called alignmentHolder. Next we want to
# delete the label tag of each sequence which is like >NP_005948.3/1-656 methylenetetrahydrofolate reductase isoform 2 [Homo sapiens]
# We do this by deleting lines that start with a ">"

    alignmentHolder = []
    lineIndex = 0
    for line in alnFile:
	alignmentHolder.append(line)
    for line in alignmentHolder:
	if alignmentHolder[lineIndex][0] == ">":
		alignmentHolder.pop(lineIndex)  
  	lineIndex += 1

# Each line in the file corresponds to a single element in the list called alignmentHolder. So each line in the file consists of 
# a string of amino acids and then to create a new line, there are "\r\n" characters. These characters are the reason why there are
# 6-8 lines of amino acids for a single sequence. We want to perform a transpose on the sequences, so we have to have an entire sequence
# on a single line (kind of like how Jalview does it). To do this, we delete the last 2 characters of every line except the last line 
# so that there is a line break after each sequence but not within one.       

    lineIndex = 0
    for line in alignmentHolder:
	lengthLine = len(alignmentHolder[0])
	if len(line) == lengthLine:
		line = alignmentHolder[lineIndex][:-2]
		wipAlnFile.write(line)
		lineIndex += 1
	else: 
		wipAlnFile.write(line)
		lineIndex += 1
    wipAlnFile.close()
    wipAlnFile = open('wipAlign.aln', mode='r')

# At this stage, we have the wip file contain each of the sequences in a single line, so the number of rows should be equal to the 
# total number of sequences. I need to transpose this file and write it somewhere, so I open a finalAlign.aln file to write the results
# of the transpose into. The last row after transposing is a bunch of new line characters from before to create a line break after each
# sequence, so we dont need to include this line in the file, hence why I break after reaching the end of the file (-1th position).
# Lastly, after column is transposed to become a row, I want to create a line break, which is why I write each row in with the addition 
# of a \n character

    newAlign = wipAlnFile.readlines()
    newAlign = [''.join(s) for s in zip(*newAlign)]
    finalAlign = open('finalAlign.aln', mode = 'w') 
    for lines in newAlign:
	if lines == newAlign[-1]:
		break
	else:
		finalAlign.write(lines + "\n")

# close the files
    
    alnFile.close()
    wipAlnFile.close()
    finalAlign.close()

main()
    
