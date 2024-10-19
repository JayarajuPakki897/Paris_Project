import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes

# Replace 'your_file_path' with the actual path to your Excel file
file_path = r'F:\Ph.D\Project_PAH\Data\SIRTA_long term_2015_Max Planck_complete_vf02.xlsx'

# Specify the sheet name
sheet_name = 'Database'

# Read the Excel file
df = pd.read_excel(file_path, sheet_name)

time=['Sampling date']
df=pd.read_excel(file_path,'p+g_SOA_markers')
df2=pd.read_excel(file_path,'Database')

time_period=df[time].iloc[1:]
time_period = pd.DataFrame({'Sampling date':time_period})
print(time_period)
time_period['Timestamp'] = pd.to_datetime(time_period['Timestamp'], format='%d/%m/%Y %H:%M:%S')
time_period['Month'] = df['Timestamp'].dt.month
time_period['Season'] = df['Month'].apply(lambda x: 'Spring' if 3 <= x <= 5 else ('Summer' if 6 <= x <= 8 
                                                                                  else ('Autumn' if 9 <= x <= 11 else 'Winter')))
time_period = time_period.drop(columns=['Month'])
