import os, os.path

##  analytical staging - these might be shared across files

# set a name for this run (good for a configuration file)
analysis_name = "crdm_project_2021091"
# export images (good for a configuration file)?
export_image_q = False
# model years
model_historical_years = list(range(2011, 2021))
model_projection_years = list(range(2021, 2056))
# set some climate info
range_delta_base = list(range(2011, 2021))
range_delta_fut = list(range(2046, 2056))
# number of lhs samples (good for a configuration file)?
n_lhs = 1000


##  some directory stuff
dir_py = os.path.dirname(os.path.realpath(__file__)) # this finds the current directory and identifies dir_py as the python directory containing setup_analysis.py when it is imported
dir_proj = os.path.dirname(dir_py)

dir_ed = os.path.join(dir_proj, "experimental_design")
dir_out = os.path.join(dir_proj, "out")
dir_ref = os.path.join(dir_proj, "ref")

# make directories if they don't exist 
if not os.path.exists(dir_ed):
    os.makedirs(dir_ed, exist_ok = True)
if not os.path.exists(dir_out):
    os.makedirs(dir_out, exist_ok = True)
if not os.path.exists(dir_ref):
    print(f"WARNING: path {dir_ref} not found.")

    

##  set some file paths
fp_csv_attribute_climate_id = os.path.join(dir_ref, "ri_attribute_climate_id.csv")
fp_csv_baseline_trajectory_model_input_data = os.path.join(dir_ref, "ri_baseline_trajectory_model_input_data.csv")
fp_csv_climate_deltas = os.path.join(dir_ref, "ri_climate_deltas.csv")
fp_csv_climate_deltas_annual = os.path.join(dir_ref, "ri_climate_deltas_annual.csv")
fp_xlsx_strategy_inputs = os.path.join(dir_ref, "strategy_table_inputs.xlsx")

##  some functions
def build_dict(df_in):
    return dict([x for x in zip(df_in.iloc[:, 0], df_in.iloc[:, 1])])
    