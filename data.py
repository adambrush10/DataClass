import pandas as pd
import numpy as np
from pandas import *

file = 'Homeworks_HW11-Web_Instructions_Resources_cities.csv'
df = pd.read_csv(file)

html_df = df.to_html(df.html)
