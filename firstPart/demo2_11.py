
# outfile = open("file/file1.txt","w")

# outfile.write("qwerty\nasdfgh\n")

# outfile.write(str(["zxcvb","pl,mko","ijnbhu"]))

# outfile.close()

# infile = open("file/file1.txt","r")

# print(infile.read())

infile = open("file/file1.txt","rb")
outfile = open("file/file2.log","wb")
countLines = countChars = 0
for line in infile:
	countLines +=1
	countChars +=len(line)
	outfile.write(line)
print (countLines,"lins and",countChars,"chars copies")

infile.close()
outfile.close()