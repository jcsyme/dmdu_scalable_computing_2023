import pandas as pd
import numpy as np

##  GET ANNUAL INCREASES IN MULTIPLICATIVE SCALAR TO GET CORRECT DELTAS
def get_annual_increase(
    delta: float, 
    mean_base: float, 
    mean_fut: float, 
    yr_base: int, 
    range_delta_fut: list,
    df_fut: pd.DataFrame,
    field_apply: str,
    field_year: str = "year"
):
    """
    calculate an annual increase to apply baseed on a delta factor
    
    - delta: the climate delta to apply (factor)
    - mean_base:  mean value of input time series during base time range used to estimate delta
    - mean_fut:  mean value of input time series during future time range used to estimate delta
    - range_delta_fut: list of years defining the time period for future delta
    - df_fut: data frame giving input time series
    - field_apply: field in df_fut to apply delta to
    - field_year: field in df_fut denoting the year
    """
    
    n = len(range_delta_fut)
    num = n*(mean_base*(1 + delta) - mean_fut)
    den = np.dot((np.array(df_fut[field_year]) - yr_base), np.array(df_fut[field_apply]))
    
    return num/den



def apply_delta_factor(
    df_climate_projection: pd.DataFrame, 
    delta: float,
    range_years_delta_base: set, 
    range_years_delta_fut: set, 
    year_cur: int,
    field_apply: str,
    field_delta_scale: str = "delta_scale",
    field_year: str = "year",
    scale_delta_for_inflection: bool = False
):

    ##  AGGREGATE BY YEAR
    
    # setup aggregation for annual totals
    dict_agg = {field_year: "first", field_apply: "sum"}
    flds_agg = list(dict_agg.keys())
    # get annual totals
    df_annual_totals_delta_base = df_climate_projection[
        df_climate_projection[field_year].isin(range_years_delta_base)
    ][[field_year, field_apply]].copy().groupby([field_year]).aggregate(dict_agg).reset_index(drop = True)
    df_annual_totals_delta_mid = df_climate_projection[
        df_climate_projection[field_year].isin(range_years_delta_fut)
    ][[field_year, field_apply]].copy().groupby([field_year]).aggregate(dict_agg).reset_index(drop = True)
    
    
    ##  SETUP DELTAS
    
    # get current observed difference
    mean_base = np.mean(np.array(df_annual_totals_delta_base[field_apply]))
    mean_fut = np.mean(np.array(df_annual_totals_delta_mid[field_apply]))
    # get appropriate annual increases to applly
    annual_increase = get_annual_increase(
        delta, 
        mean_base, 
        mean_fut, 
        year_cur,
        range_years_delta_fut,
        df_annual_totals_delta_mid, 
        field_apply
    )
    
    yr_delta_0 = int(np.floor(np.mean(np.array(range_years_delta_base))))
    yr_delta_1 = int(np.floor(np.mean(np.array(range_years_delta_fut))))
    delta_apply = annual_increase*(yr_delta_1 - year_cur)
    print(delta_apply)
    #add shifts from deltas
    df_out = df_climate_projection.copy()
    df_out[field_delta_scale] = [1 + int(x > year_cur)*(x - year_cur)*delta_apply/(yr_delta_1 - year_cur) for x in list(df_out[field_year])]
    df_out[f"{field_apply}_w_delta"] = np.array(df_out[field_apply])*np.array(df_out[field_delta_scale])

    return df_out
