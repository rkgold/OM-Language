from sys import *

def main():
	if len(argv) == 1:
		print("OM v1.0.0")
	else:
		if argv[1].endswith(".om"):
			data = open(argv[1], "r").read()
		else:
			print('The extention must be ".om"')
			return
		dataset = data.split("\n")
		if len(argv) == 3:
			if argv[2] == "-d":
				print("Data set:"+str(dataset))
		if len(argv) == 4:
			if argv[2] == "-py":
				f = open(argv[3], "w")
		vars = []
		isOutputing = False
		for dat in dataset:
			if ":output" == dat:
				isOutputing = False
			if isOutputing != False:
				if dat.startswith("var: "):
					temp = dat.split(" ",1)[1]
					if len(temp.split(" ")) == 2:
						temp = temp.split(" ")
						vars.append(temp)
						f.write(temp[0] + "=" + temp[1] + "\n")
					continue
				
				if dat.startswith("input: "):
					temp = dat.split(" ",1)[1]
					temp = dat.split(" ",1)[1].split(" ",1)
					# vars.append([temp[0],input(temp[1])])
					c = 0
					for _ in vars:
						if _[0] == temp[0]:
							break
						c = c + 1
					vars[c] = [temp[0],input(temp[1])]

					# if len(temp.split(" ")) == 2:
					# 	temp = temp.split(" ")
					# 	vars.append(temp)
					continue
				_temp = ""
				abc = False
				for v in vars:
					if v[0] in dat:
						dat = dat.replace(v[0],v[1])
						if dat.startswith('"') and dat.endswith('"'):
							_temp = "'"+dat+"'"
							abc = True
						else:
							_temp = dat
				if abc:
					f.write("print("+_temp+")\n")
				else:
					f.write("print('"+_temp+"')\n")
				print(dat)
			if "output:" == dat:
				isOutputing = True

if __name__ == "__main__":
	main()