import crypt


def testPass(cryptPass, username):
	
	dictFile = open('dictionary.txt', 'r')
	ctype = cryptPass.split("$")[1]

	if ctype == '6':
		salt = cryptPass.split("$")[2]
		insalt = "$" + ctype + "$" + salt + "$"
		for word in dictFile.readlines():
			word = word.strip('\n')
			cryptWord = crypt.crypt(word, insalt)
			if (cryptWord == cryptPass):
				print "Found password for the user: " + username + " " + word + "\n"
			else:
				print "Password not in dictionary"
		exit
def main():
	
  	
    	passFile = open ('/etc/shadow','r')
      	for line in passFile.readlines():
           line = line.replace("\n","").split(":")
           if  not line[1] in [ 'x', '*','!' ]:
           	user = line[0]
            	cryptPass = line[1]
            	testPass(cryptPass,user)
 
if __name__=="__main__":
   main()



