for i in range(0,35):
	try:
		with open("test{}.txt".format(i)) as f:
			for line in f:
				if(line[0:4]=="10100"):
					print("found")
					break
				else:
					print(line[0:4])	
	except Exception as e:
		print("File not found")