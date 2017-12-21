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
index = 0
for disease in variable_to_value["Disease"]:
	if(disease == "control"):
		patients_to_save.append(index)
	elif(disease == "SjS"):
		patients_to_save.append(index)
	index += 1

## Build all pair of variables
## to be analysed


## Perfrom the analysis on all pair of variables






	##--------------------------------##
	## if p-value is good draw a plot ##
	## save variable in an output     ##
	## data file					  ##
	##--------------------------------##


	##--------------------------------##
	## Store everything in a log file ##
	##--------------------------------##