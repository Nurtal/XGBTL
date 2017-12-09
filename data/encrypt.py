# -*- coding: utf-8 -*-
##
## -> script to encrypt and decrypt a txt file
## -> use vigenere
## -> take 2 arguments:
## 	- action :
##		- encrypt
##		- decrypt
## 	- key
## 

import sys
import os.path


instruction = str(sys.argv[1])
clef = str(sys.argv[2])


data_files = ["data_control_RA.csv", "data_control_SLE.csv", "data_control_SjS.csv", "data_control_SSc.csv", "data_control_MCTD.csv", "data_control_PAPs.csv","data_control_UCTD.csv", "data_control_MCTD_NA_filtered.csv","data_control_PAPs_NA_filtered.csv","data_control_RA_NA_filtered.csv","data_control_SjS_NA_filtered.csv","data_control_SLE_NA_filtered.csv","data_control_SSc_NA_filtered.csv","data_control_UCTD_NA_filtered.csv", "Luminex_data.csv"]



## encrypt captainlog.md
if(instruction == "encrypt"):
	

	for target_file in data_files:

		if(os.path.isfile(target_file)):		

			# lecture du fichier messageclair.txt
			fichier=open(target_file,"r")
			texteclair=fichier.read()
			fichier.close()
	
			# initialisation du texte chiffre
			textechiffre=""

			# chiffrement
			for i in range (0,len(texteclair)):
			
				caractere=texteclair[i]
				code=ord(caractere)
				decalage=ord(clef[i%len(clef)])
				codechiffre=(code+decalage)%256
				caracterechiffre=chr(codechiffre)
				textechiffre=textechiffre+caracterechiffre

			# ecriture dans le fichier messagechiffre.txt
			fichier=open(target_file,"w")
			fichier.write(textechiffre)
			fichier.close()

		else:
			print "[WARNINGS] => can't find "+str(target_file)



## decrypt captainlog.md
elif(instruction == "decrypt"):

	for target_file in data_files:	
		if(os.path.isfile(target_file)):
			# lecture du fichier messagechiffre.txt
			fichier=open(target_file,"r")
			textechiffre=fichier.read()
			fichier.close()

			# initialisation du texte clair
			texteclair=""

			# dechiffrement
			for i in range (0,len(textechiffre)):
				caractere=textechiffre[i]
				code=ord(caractere)
				decalage=ord(clef[i%len(clef)])
				codeclair=(code-decalage)%256
				caractereclair=chr(codeclair)
				texteclair=texteclair+caractereclair

			# ecriture dans le fichier messageclair.txt
			fichier=open(target_file,"w")
			fichier.write(texteclair)
			fichier.close()

		else:
			print "[WARNINGS] => can't find "+str(target_file)

			

else:

	print "[ERROR] => wrong instruction"
