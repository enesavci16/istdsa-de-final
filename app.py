import streamlit as st 
import numpy as np
import pandas as pd
#import time
import plotly.express as px
import matplotlib
import os
# Google bigquery
from google.cloud import bigquery

# change project name
#change json file
def bigquery_get_df(query="SELECT * FROM intrepid-decker-383607.analiz_air.analiz_table"):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='streamlit-folder/intrepid-decker-383607-466e94005135.json'
    client=bigquery.Client()
    
    QUERY=(query)
    query_job=client.query(QUERY) #API request
    
    rows=query_job.result() # waits for query 
    row_list=[]
    for row in rows:
        value=[row[0],row[1],row[2],row[3],row[4],row[5]]
        row_list.append(value)
    df=pd.DataFrame(row_list,columns=["City","Local Time","aqius","aqicn","tp","hu"])
    return df

a=bigquery_get_df()

print(a)


