import time
import pandas as pd

def timing()->None:
    time.sleep(1)
    print("Hello World after 1 second")

def show_df():
    df = pd.DataFrame([1,2], columns=['numbers'])
    print(df)