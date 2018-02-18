

# 'W' is write
#outfile is a pointer to where the file is located named President.txt
outfile = open("Presidents.txt", "w")

outfile.write("Refer tp WriteFile.py\n")
outfile.write("Bill Clinton\n")
outfile.write("George Bush\n")
outfile.write("Barack Obama\n")
outfile.write("Foo Bar")


outfile.close()
