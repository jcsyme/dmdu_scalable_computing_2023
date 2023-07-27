import os, os.path


##  analytical staging - these might be shared across files

# set a name for this run (good for a configuration file)
analysis_name = "run_20220725_test"
# export images (good for a configuration file)?
export_image_q = False
# model years
model_historical_years = list(range(2018, 2021))
model_projection_years = list(range(2021, 2056))
# set some climate info
range_delta_base = list(range(2011, 2021))
range_delta_fut = list(range(2046, 2056))
# number of lhs samples (good for a configuration file)?
n_lhs = 1000


##  some directory stuff
dir_cur = os.getcwd()
dir_ed = os.path.join(dir_cur, "experimental_design")
dir_out = os.path.join(dir_cur, "out")

# make directories if they don't exist 
if not os.path.exists(dir_ed):
    os.makedirs(dir_ed, exist_ok = True)
if not os.path.exists(dir_out):
    os.makedirs(dir_out, exist_ok = True)

    

##  set some file paths
fp_csv_attribute_primary_id = os.path.join(dir_ed, "attribute_primary_id.csv")
fp_csv_model_input_ranges = os.path.join(dir_cur, "class_4_model_input_ranges.csv")
fp_csv_out_lhs_trials = os.path.join(dir_ed, f"class_4_lhs_trials_{analysis_name}.csv")
fp_csv_out_input_database = os.path.join(dir_ed, f"model_input_database_{analysis_name}.csv")

fp_jpg_template_lhs_fig = os.path.join(dir_out, f"lhs_dem_v%s-%s_{analysis_name}.jpg")
fp_jpg_template_variable_spread_fig = os.path.join(dir_out, f"futures_trajectories_%s_{analysis_name}.jpg")



##  some functions
def build_dict(df_in):
    return dict([x for x in zip(df_in.iloc[:, 0], df_in.iloc[:, 1])])
    