import datetime as dt
import os, os.path
import pandas as pd
from typing import *

##  analytical staging - these might be shared across files


    
#########################
#    BASIC FUNCTIONS    #
#########################

def build_dict(
    df_in: pd.DataFrame,
) -> Union[dict, None]:
    """
    Build a dictionary from two columns
    """
    
    # verify input type
    if not isinstance(df_in, pd.DataFrame):
        return None
    
    
    out = dict(
        x for x in zip(df_in.iloc[:, 0], df_in.iloc[:, 1])
    )
    
    return out



def get_time_stamp(
    time_now: Union[dt.datetime, None] = None,
) -> str:
    """
    Based on the current `time` (datetime obj), create a time stamp
        for use in analytical names.
    """
    
    # check time
    time_now = (
        time_now
        if isinstance(time_now, dt.datetime)
        else dt.datetime.now()
    )
    
    # convert to string and clean
    str_out = time_now.isoformat()
    str_out = (
        str_out
        .replace(":", "")
        .replace("-", "")
        .replace(".", "")
    )
    
    return str_out
    

    
    
#############################
#    SOME INITIALIZATION    #
#############################


# export images (good for a configuration file)?
export_image_q = False

# setup some shared fields
field_key_future = "future_id"
field_key_strategy = "strategy_id"
field_key_primary = "primary_id"
field_time_month = "month"
field_time_time_period = "time_period"
field_time_year = "year"

# model years
model_historical_years = list(range(2011, 2021))
model_projection_years = list(range(2021, 2056))

# number of lhs samples (good for a configuration file)?
n_lhs = 100

# set some climate info
range_delta_base = list(range(2011, 2021))
range_delta_fut = list(range(2046, 2056))

# strategies to run
strats_run = [0, 1, 2]


# set a name for this run (good for a configuration file) 
time_stamp = get_time_stamp()
analysis_name = f"crdm_project_{time_stamp}_{n_lhs}fut"


##  INIT DIRECTORIES

##  some directory stuff
dir_py = os.path.dirname(os.path.realpath(__file__)) # this finds the current directory and identifies dir_py as the python
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
    

##  SET SOME FILE PATHS

# names
fn_csv_attribute_future_id = "attribute_future_id.csv"
fn_csv_attribute_primary_id = "attribute_primary_id.csv"
fn_csv_attribute_strategy_id = "attribute_strategy_id.csv"
fn_csv_futures = "futures.csv"
fn_csv_metrics = "metrics_and_futures.csv"
fn_csv_strategies = "strategies.csv"

# paths
fp_csv_attribute_climate_id = os.path.join(dir_ref, "ri_attribute_climate_id.csv")
fp_csv_baseline_trajectory_model_input_data = os.path.join(dir_ref, "ri_baseline_trajectory_model_input_data.csv")
fp_csv_climate_deltas = os.path.join(dir_ref, "ri_climate_deltas.csv")
fp_csv_climate_deltas_annual = os.path.join(dir_ref, "ri_climate_deltas_annual.csv")
fp_xlsx_strategy_inputs = os.path.join(dir_ref, "strategy_table_inputs.xlsx")


