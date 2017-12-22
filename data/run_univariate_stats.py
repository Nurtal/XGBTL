##
## Check univariate stuff in
## Luminex data, only for SjS patients
##

from scipy import stats


## Stat part
"""
rvs1 = stats.norm.rvs(loc=5,scale=10,size=500)
rvs2 = stats.norm.rvs(loc=5,scale=10,size=500)
machin = [0,1,1,0,0,1,0,1]
truc = [2,15,19,1,5,19,3,12]
print stats.ttest_ind(machin,truc)
"""

##------------------------##
## open file and get data ##
##------------------------##
variable_to_value = {}
index_to_variable = {}

input_data = open("Luminex_data.csv")
cmpt = 0
for line in input_data:
	if(cmpt ==0):
		line_in_array = line.split(",")
		index = 0
		for variable in line_in_array:
			index_to_variable[index] = variable
			variable_to_value[variable] = []
			index += 1
	else:
		line_in_array = line.split(",")
		index = 0
		for scalar in line_in_array:
			variable_to_value[index_to_variable[index]].append(scalar)
			index +=1
	cmpt +=1
input_data.close()



##------------------------------##
## Compute Stat part for each 	##
## luminex variables associated ##
## with Disease					##
##------------------------------##

## get only the SjS and Control patient
patients_to_save = []
disease_vector = []
index = 0
for disease in variable_to_value["Disease"]:
	if(disease == "control"):
		patients_to_save.append(index)
		disease_vector.append(disease)
	elif(disease == "SjS"):
		patients_to_save.append(index)
		disease_vector.append(disease)
	index += 1

## Build all pair of variables
## to be analysed
patients_to_remove = []

for variable in variable_to_value.keys():
	
	if(variable != "Disease"):

		## Get variables to test
		## Flag patients to remove (NA values)
		variable_vector = []
		index = 0
		for scalar in variable_to_value[variable]:
			if(index in patients_to_save):
				variable_vector.append(scalar)
				if(scalar == ""):
					patients_to_remove.append(index)
			index +=1

		## Remove Flag patients from disease and
		## variables vector
		disease_vector_clean = []
		variable_vector_clean = []

		index = 0
		for patient in patients_to_save:
			if(patient not in patients_to_remove):
				if(disease_vector[index] == "control"):
					disease_vector_clean.append(0)
				elif(disease_vector[index] == "SjS"):
					disease_vector_clean.append(1)
				variable_vector_clean.append(float(variable_vector[index]))
			index += 1	

		##----------##
		## Analysis ##
		##----------##

		## Perfrom the analysis on all pair of variables
		## TODO : check optimal test
		print stats.ttest_ind(disease_vector_clean,variable_vector_clean)

		##--------------------------------##
		## if p-value is good draw a plot ##
		## save variable in an output     ##
		## data file					  ##
		##--------------------------------##


		##--------------------------------##
		## Store everything in a log file ##
		##--------------------------------##