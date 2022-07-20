import time
import math

# example approahc
def example_do(df_in, fp_out, primary_key = "primary_id"):
    
    # open the file and write a header
    file = open(fp_out, "w+")
    file.write("%s,result_do\n"%(primary_key))
    
    # iterate over data frame
    for i in range(len(df_in)):
        
        # generate the main id
        id_main = int(df_in[primary_key].iloc[i])
        
        # get inputs
        input_1 = float(df_in["input_1"].iloc[i])
        input_2 = float(df_in["input_2"].iloc[i])
        
        # waste time, pretend it's a model
        time.sleep(input_2/3)
        
        # create an output value
        val_return = math.e**input_1 
        
        str_out = ",".join([str(x) for x in [id_main, val_return]]) + "\n"
        # write output
        file.write(str_out)
        
        print("Iteration %s for %s = %s complete."%(i, primary_key, id_main))
        
    file.close()
    
    return(0)



# EXAMPLE OF WHAT TO AVOID—NOTE THAT THE SCENARIO IS INDEXED BY ROW NUMBER
def example_dont(df_in, fp_out, primary_key = "primary_id"):
    
    # open the file and write a header
    file = open(fp_out, "w+")
    file.write("%s,result_do\n"%(primary_key))
    
    # iterate over data frame
    
    for i in range(len(df_in)):
        
        # get inputs
        input_1 = float(df_in["input_1"].iloc[i])
        input_2 = float(df_in["input_2"].iloc[i])
         
        # waste time, pretend it's a model
        time.sleep(input_2/3)
        
        # create an output value
        val_return = math.e**input_1 
        
        str_out = ",".join([str(x) for x in [i, val_return]]) + "\n"
        # write output
        file.write(str_out)
        
        print("Iteration %s for %s = %s complete."%(i, primary_key, i))
        
    file.close()
    
    return(0)
    
        
        
        
        
        