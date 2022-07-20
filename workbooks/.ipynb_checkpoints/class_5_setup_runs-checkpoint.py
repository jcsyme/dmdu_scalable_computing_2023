import os, os.path
import pandas as pd
import numpy as np


###################################
#    START WITH INITIALIZATION    #
###################################

#set the working directory
dir_cur = os.path.dirname(os.path.realpath(__file__))
# initialize an output directory if it doesn't exist (in current directory)
dir_out = os.path.join(os.getcwd(), "out")

if not os.path.exists(dir_out):
    os.makedirs(dir_out, exist_ok = True)
    
# create an output file path template
fp_out_par_template = os.path.join(dir_out, "class_5_partemporary_csv-##PROC##.csv")
fp_out_par_final = os.path.join(dir_out, "class_5_paraggregate_csv.csv")
fp_out_serial = os.path.join(dir_out, "class_5_serial_csv.csv")



#############################################
#    GET INITIALIZATION FILE INFORMATION    #
#############################################

#get initialization files
fp_ini_session = os.path.join(dir_model, "class_5_initialize_session.ini")
#read in session initialization
if os.path.exists(fp_ini_session):
	#read in
	with open(fp_ini_session) as f:
		list_init_session = f.readlines()
else:
	list_init_session = []

#join
list_init = list_init_session
#remove unwanted blank characters
for char in ["\n", "\t"]:
	list_init = [l.replace(char, "") for l in list_init]
#remove instances of blank strings
list_init = list(filter(lambda x: (x != "") and ("#" in x) == False, list_init))
list_init = list(filter(lambda x: (x[0] != "["), list_init))
#split strings
dict_init = [l.split(":") for l in list_init]
#convert to dictionary
dict_init = dict(dict_init)
#convert numeric values
for key in dict_init.keys():
	if dict_init[key].isnumeric():
		num = float(dict_init[key])
		if num == int(num):
			dict_init[key] = int(num)
		else:
			dict_init[key] = num

