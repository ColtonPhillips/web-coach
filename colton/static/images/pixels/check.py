import glob
import os
def main():
	i = 0
	for file in glob.glob("*.png"):
		i = i + 1
	print(999 - i)

	last_one = ""
	for file in glob.glob("*.png"):
		if last_one != "":
			if file[1:3] == '00':
				if last_one[1:3] != '99':
					print(last_one)
				last_one = file
				continue

			if int(file[1:3]) != int(last_one[1:3]) + 1:
				print(last_one)
				return

		last_one = file

if __name__ == "__main__":
	main()
