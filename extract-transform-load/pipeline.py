import pandas as pd

def extract_data(path):
    df = pd.read_excel(path)
    return df

def transform_data(df):
    # Remove nulls
    df = df.dropna()

    # Remove negative quantity
    df = df[df['quantity']>=0]

    # Calculate revenue
    df['revenue'] = df['quantity'] * df['price']

    return df

path = r'L:\Data Engineer\Python\Functions\raw_sales.xlsx'


def validate_date(df):
    if df.empty:
        raise ValueError("Dataset is empty after transformation")

    if (df['quantity'] < 0).any():
        raise ValueError("Negative quantity detected")

    print('Validation is ok')
    return True

def data_load(df,output_path):
    df.to_csv(output_path,index=False)
    print(f'Data saved to {output_path}')


def run_etl():
    try:
        
        df = extract_data(path)
        df = transform_data(df)
        validate_date(df)
        data_load(df,"L:\Data Engineer\Python\Functions\sales_output.csv")
        print('ETL completed successfully')
    
    except:

        print('Pipeline execution failed \n Please check')
        


run_etl()
