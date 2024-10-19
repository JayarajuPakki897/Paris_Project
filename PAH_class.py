import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



file_path= r'F:\Ph.D\Project_PAH\Data\SIRTA_long term_2015_Max Planck_complete_vf02.xlsx'
oxy_PAH=['SUCCINIC ACID','ALPHA-METHYLGLYCERIC ACID','DHOPA', '3-HYDROXYGLUTARIC ACID','3-(2-HYDROXY-ETHYL)-2,2-DIMETHYLCYCLOBUT',
         '3-HYDROX-4,4--DIMETHYLGLUTARIC ACID','3-ACETYLPENTANEDIOIC ACID','PHTHALIC ACID','3-ACETYL HEXANEDIOIC ACID',
         '3-ISOPROPYLPENTANEDIOIC ACID','TERPENYLIC ACID','2-METHYL ERYTHRITOL']
        # DHOPA =Dihydroxyphenylacetic acid
nitro_PAH=['2-NITROPHENOL','4-NITROPHENOL','2-METHYL-4-NITROPHENOL','4-NITROGUAIACOL','5-NITROGUAIACOL',
           '4-METHYL-5-NITROCATHECOL','3-METHYL-6-NITROCATHECOL','3-METHYL-5-NITROCATHECOL']
phenolic_compounds=['2-NITROPHENOL','4-NITROPHENOL','2-METHYL-4-NITROPHENOL','4-NITROGUAIACOL','5-NITROGUAIACOL','4-METHYL-5-NITROCATHECOL',
                    '3-METHYL-6-NITROCATHECOL','3-METHYL-5-NITROCATHECOL']
low_mw_compounds=['SUCCINIC ACID','ALPHA-METHYLGLYCERIC ACID','DHOPA',
                  '3-HYDROXYGLUTARIC ACID','3-(2-HYDROXY-ETHYL)-2,2-DIMETHYLCYCLOBUT',
                  '3-HYDROX-4,4--DIMETHYLGLUTARIC ACID','3-ACETYLPENTANEDIOIC ACID','2-METHYL ERYTHRITOL']
high_mw_compounds=['PHTHALIC ACID','3-ACETYL HEXANEDIOIC ACID','3-ISOPROPYLPENTANEDIOIC ACID','TERPENYLIC ACID']
time=['Sampling date']
df=pd.read_excel(file_path,'p+g_SOA_markers')
df2=pd.read_excel(file_path,'Database')
Temperature='Temp ©'
Temperatures=df2[Temperature].iloc[1:]

time_period=df[time].iloc[1:]
time_period = pd.DataFrame({'Sampling date':time_period})
print(time_period)
# time_period['Timestamp'] = pd.to_datetime(time_period['Timestamp'], format='%d/%m/%Y %H:%M:%S')
# time_period['Month'] = df['Timestamp'].dt.month
# time_period['Season'] = df['Month'].apply(lambda x: 'Spring' if 3 <= x <= 5 else ('Summer' if 6 <= x <= 8 
#                                                                                   else ('Autumn' if 9 <= x <= 11 else 'Winter')))
# time_period = time_period.drop(columns=['Month'])

# Print the DataFrame with the added 'Season' column
# print(time_period)
# oxy_PAHs=df[oxy_PAH].iloc[1:].sum(axis=1)
# nitro_PAHs=df[nitro_PAH].iloc[1:].sum(axis=1)
# phenolic_compoundss=df[phenolic_compounds].iloc[1:].sum(axis=1)
# # data={Temperatures,nitro_PAHs}
# print(nitro_PAHs)
# plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})

# # Create a regression plot
# #sns.regplot(x=nitro_PAHs, y=Temperatures)
# Temperatures = Temperatures.astype(float)
# oxy_PAHs = oxy_PAHs.astype(float)

# slope, intercept = np.polyfit(Temperatures, oxy_PAHs, 1)
# regression_line = slope * Temperatures + intercept
# plt.scatter(Temperatures, oxy_PAHs, label='Data Points')
# plt.plot(Temperatures, regression_line, color='red', label='Regression Line')

# # Add labels and title
# plt.xlabel('Temperature')
# plt.ylabel('oxy_PAHs')
# plt.title('Regression Plot')

# # Show legend
# plt.legend()

# # Show the plot
# plt.show()