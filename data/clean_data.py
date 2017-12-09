

from netabio import na_manager


data_files = ["data_control_RA.csv", "data_control_SLE.csv", "data_control_SjS.csv", "data_control_SSc.csv", "data_control_MCTD.csv", "data_control_PAPs.csv","data_control_UCTD.csv"]


for data_file in data_files:
	print "[NA MANAGER] => "+str(data_file)
	na_manager.filter_NA_values(data_file)

#data_file_name = "data_control_RA.csv"

#na_manager.check_NA_proportion_in_file(data_file_name)
#na_manager.display_NA_proportions(data_file_name)
#na_manager.filter_NA_values(data_file_name)
