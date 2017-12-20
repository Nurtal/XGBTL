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





def get_specific_metabo():
	##
	## Custom function to get GDF15 and PENTRAXIN 3 data for control
	## and SjS patient.
	##

	input_data = open("data_control_SjS.csv", "r")
	output_data = open("data_control_SjS_PENTRAXIN3_vs_GDF15.csv", "w")

	cmpt = 0
	DISEASE_index = -1
	PENTRAXIN3_index = -1
	GDF15_index = -1


	for line in input_data:

		line_in_array = line.split(",")
		
		## deal with the header
		if(cmpt == 0):
			header = "Disease,GDF15,PENTRAXIN3\n"
			index = 0
			for variable in line_in_array:
				if("Disease" in variable):
					DISEASE_index = index
				elif("GDF15" in variable):
					GDF15_index = index
				elif("PENTRAXIN3" in variable):
					PENTRAXIN3_index = index
				index +=1
			output_data.write(header)
		else:
			DISEASE_value = line_in_array[DISEASE_index]
			PENTRAXIN3_value = line_in_array[PENTRAXIN3_index]
			GDF15_value = line_in_array[GDF15_index]

			line_to_write = str(DISEASE_value)+","+str(GDF15_value)+","+str(PENTRAXIN3_value)+"\n"
			output_data.write(line_to_write)

		cmpt += 1

	output_data.close()
	input_data.close()


def get_treatment():
	##
	## custom function
	##

	input_data = open("transmart_10_08_2017_PHASE_I_II.tsv", "r")
	output_data = open("data_with_medication.csv", "w")




	DISEASE_index = -1
	ABATACEPT_index = -1
	AMALARIA_index = -1
	ATNFALL_index = -1
	ATNF_index = -1
	IMSUPPR_index = -1
	STEROID_index = -1
	SYSABIO_index = -1

	PENTRAXIN3_index = -1
	GDF15_index = -1




	cmpt = 0
	for line in input_data:

		line_in_array = line.split("\t")
		
		if(cmpt == 0):
			

			header = "DISEASE,ABATACEPT,AMALARIA,ATNFALL,IMSUPPR,STEROID,SYSABIO,PENTRAXIN3,GDF15\n"

			index = 0
			for variable in line_in_array:

				if("DISEASE" in variable):
					DISEASE_index = index
				elif("ABATACEPT" in variable):
					ABATACEPT_index = index
				elif("AMALARIA" in variable):
					AMALARIA_index = index
				elif("ATNFALL" in variable):
					ATNFALL_index = index
				elif("IMSUPPR" in variable):
					IMSUPPR_index = index
				elif("CM STEROID" in variable):
					STEROID_index = index
				elif("SYSABIO" in variable):
					SYSABIO_index = index
				elif("PENTRAXIN" in variable):
					PENTRAXIN3_index = index
				elif("GDF 15" in variable):
					GDF15_index = index

				index +=1

			output_data.write(header)
		
		else:

			DISEASE_value = "choucroute"
			ABATACEPT_value = -1
			AMALARIA_value = -1
			ATNFALL_value = -1
			ATNF_value = -1
			IMSUPPR_value = -1
			STEROID_value = -1
			SYSABIO_value = -1

			PENTRAXIN3_value = -1
			GDF15_value = -1
			
			if(line_in_array[DISEASE_index] == ""):
				DISEASE_value = "Control"
				ABATACEPT_value = "No"
				AMALARIA_value = "No"
				ATNFALL_value = "No"
				ATNF_value = "No"
				IMSUPPR_value = "No"
				STEROID_value = "No"
				SYSABIO_value = "No"

				PENTRAXIN3_value = line_in_array[PENTRAXIN3_index]
				GDF15_value = line_in_array[GDF15_index]



			elif(line_in_array[DISEASE_index] == "\"SjS\""):
				DISEASE_value = "SjS"
				ABATACEPT_value = line_in_array[ABATACEPT_index]
				AMALARIA_value = line_in_array[AMALARIA_index]
				ATNFALL_value = line_in_array[ATNFALL_index]
				ATNF_value = line_in_array[ATNF_index]
				IMSUPPR_value = line_in_array[IMSUPPR_index]
				STEROID_value = line_in_array[STEROID_index]
				SYSABIO_value = line_in_array[SYSABIO_index]

				PENTRAXIN3_value = line_in_array[PENTRAXIN3_index]
				GDF15_value = line_in_array[GDF15_index]



			line_to_write = DISEASE_value+","+str(ABATACEPT_value)+","+str(AMALARIA_value)+","+str(ATNFALL_value)+","+str(IMSUPPR_value)+","+str(STEROID_value)+","+str(SYSABIO_value)+","+str(PENTRAXIN3_value)+","+str(GDF15_value)+"\n"

			if(line_in_array[DISEASE_index] == "\"SjS\""):
				output_data.write(line_to_write)
			elif(line_in_array[DISEASE_index] == ""):
				output_data.write(line_to_write)


				

		cmpt +=1


	output_data.close()
	input_data.close()


### TEST SPACE ###
#generate_data_file("control", "RA")
#get_all_diseases_in_file("Luminex_data.csv")

## create control vs disease datasets
#create_all_datasets()

#get_specific_metabo()
get_treatment()


