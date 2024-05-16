import pandas as pd
import json
import math

def scale_up(value):
    if isinstance(value, str) and value.strip().replace(".", "").isdigit():
        return str(int(float(value) * 10**18))
    elif isinstance(value, (int, float)):
        return str(int(value * 10**18))
    return str(value)

def add_zero_to_last_digit(value):
    if isinstance(value, int) and value > 0:
        str_value = str(value)
        last_digit = str_value[-1]
        return int(str_value[:-1] + '0' + last_digit)
    return value

def process_dataframe(df, num_rows=100):
    processed_df = df.copy()  
    for column in processed_df.columns:
        processed_df[column] = processed_df[column].apply(scale_up).apply(add_zero_to_last_digit)
    return processed_df.values.tolist()[:num_rows]

def save_as_json(data, output_file):
    with open(output_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def import_and_process_csv(input_file, output_file, num_rows=100):
    df = pd.read_csv(input_file)
    processed_data = process_dataframe(df, num_rows)
    save_as_json(processed_data, output_file)

if __name__ == "__main__":
    input_file = r"C:/Users/krish/Desktop/prepped_data.csv"  
    output_file = "output22.json" 
    import_and_process_csv(input_file, output_file)
