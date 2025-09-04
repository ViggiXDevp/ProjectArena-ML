import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('Cleaned Crime Data Set.csv')
print(df)

# Generating Report
profile = ProfileReport(df)
profile.to_file(output_file="CrimeData.html")