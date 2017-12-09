##
## Split Luminex data
##

def get_all_diseases_in_file(data_file):
	## 
	## Return the list of disease
	## found in the data_file
	##


	## init variables
	list_of_diseases = []
	disease_index = -1

	## open data file
	input_data = open(data_file, "r")
	cmpt = 0
	for line in input_data:
		
		line = line.replace("\n", "")

		## parse header
		if(cmpt == 0):
			line_in_array = line.split(",")			
			index = 0
			for variable in line_in_array:
				if(variable == "Disease"):
					disease_index = index					
				index +=1
	
		## parse lines
		else:
			line_in_array = line.split(",")
			index = 0
			for scalar in line_in_array:
				if(index == disease_index and str(scalar) not in list_of_diseases):
					list_of_diseases.append(str(scalar))
				index+=1	
		cmpt += 1
	input_data.close()

	return list_of_diseases




def generate_data_file(disease_1, disease_2):
	##
	## split original data file into new specific
	## csv file containing only patients with disease_1
	## and patients with disease_2.
	##

	## open data file
	input_data = open("Luminex_data.csv", "r")
	output_data = open("data_"+str(disease_1)+"_"+str(disease_2)+".csv", "w")
	cmpt = 0
	for line in input_data:

		line = line.replace("\n", "")
		line = line.replace("\r", "")
		line = line.replace("\"", "")

		if(cmpt == 0):
			output_data.write(line+"\n")

		else:
			line_in_array = line.split(",")
			patient_disease = line_in_array[0]
			patient_disease = patient_disease.replace("\"", "")

			if(patient_disease in [str(disease_1), str(disease_2)]):

				line_to_write = ""
				index = 0
				for scalar in line_in_array:
					if(index == 0):
						line_to_write += str(patient_disease)+","
					else:
						line_to_write += str(scalar)+","
					index += 1
				
				line_to_write = line_to_write[:-1]
				output_data.write(line_to_write+"\n")



				output_data.write(line+"\n")

		cmpt +=1

	output_data.close()
	input_data.close()



def create_all_datasets():
	##
	## Create all dataset disease vs control
	## for each disease found in the luminex data file
	##


	list_of_diseases = get_all_diseases_in_file("Luminex_data.csv")
	
	for disease in list_of_diseases:
		if(disease != "control"):
			print "[DATA GENERATION] => control vs "+str(disease)
			generate_data_file("control", str(disease))	



### TEST SPACE ###
#generate_data_file("control", "RA")
#get_all_diseases_in_file("Luminex_data.csv")

## create control vs disease datasets
create_all_datasets()



