import os

for filename in os.listdir("./"):
	if filename.endswith(".c"):
		print filename
		infile = open(filename, "a+")
		lines = []
		outlines=[]

		for line in infile:
			lines.append(line)

		for x in range(len(lines)):
			words = lines[x].split()
			modif = False
			print words
			if(("return" in words) and ("-1;" in words or "ERROR;" in words)):
				print "Found error"
				modif = True
			if(modif):
				prevw = lines[x-1].split()
				print "Checking for log"
				if("LOG*" not in prevw):
					print "Log not found"
					outlines.append("LOG(\"HELLO\\n\");\n")
			outlines.append(lines[x])
			pass

		infile.truncate(0)
		for line in outlines:
			infile.write(line)
			pass