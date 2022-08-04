import os
print(os.getcwd())

dirname=input("What pathway would you like to create?: ")

checkpoint=os.path.exists(dirname)#https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/

while checkpoint == False:
	dirname=input("please enter a valid pathway: ")
	checkpoint=os.path.exists(dirname)

def new_directory():
	os.chdir(dirname)
	print(os.getcwd())

filename=input("What is the name of the file you would like to create? Please include the file type(.txt, .pdf, and so on): ")

def new_file():
	with open(os.path.join(dirname,filename),'w') as fp:
		pass
		fp.write(f"{name},{address},{phone_number}")

name=input("To whom do I have the pleasure of conversing with?: ")

address=input("What's your home address? ...for reasons: ")

phone_number=input("While we're at it, what's your phone number?: ")

new_directory()
new_file()


#lines 19, 20, and part of 21 are from https://www.geeksforgeeks.org/create-an-empty-file-using-python/
#lines 2 and 13 are from https://www.tutorialsteacher.com/python/os-module