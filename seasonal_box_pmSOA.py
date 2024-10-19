import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame, skipping the first row
excel_file = r'F:\Ph.D\Project_PAH\Data\SIRTA_long term_2015_Max Planck_complete_vf02.xlsx'
sheet_name = 'PM_SOA_markers'
dataTable = pd.read_excel(excel_file, sheet_name=sheet_name, skiprows=1)

# Convert the "Sampling date" column to datetime format
dataTable['Sampling date'] = pd.to_datetime(dataTable['Sampling date'], errors='coerce')

# Drop rows with missing datetime values
dataTable.dropna(subset=['Sampling date'], inplace=True)

# Extract time and month information
time = dataTable['Sampling date']
months = time.dt.month

# Divide data into seasons
winterData = dataTable[(months == 12) | (months == 1) | (months == 2)]  # Dec, Jan, Feb
springData = dataTable[(months == 3) | (months == 4) | (months == 5)]    # Mar, Apr, May
summerData = dataTable[(months == 6) | (months == 7) | (months == 8)]    # Jun, Jul, Aug
autumnData = dataTable[(months == 9) | (months == 10) | (months == 11)]  # Sep, Oct, Nov

# Calculate the sum of PM SOA markers for each season
winterDatasum = winterData.iloc[:, 1:].sum(axis=1)
springDatasum = springData.iloc[:, 1:].sum(axis=1)
summerDatasum = summerData.iloc[:, 1:].sum(axis=1)
autumnDatasum = autumnData.iloc[:, 1:].sum(axis=1)

positions = np.arange(1, 5)

# Data in a list for easier handling in a loop
seasonalData = [winterDatasum, springDatasum, summerDatasum, autumnDatasum]
seasonNames = ['Winter', 'Spring', 'Summer', 'Autumn']

# Create side-by-side box plots using a loop
plt.figure()
for i in range(len(seasonalData)):
    plt.boxplot(seasonalData[i], positions=[positions[i]], widths=0.6, showmeans=True, showfliers=False)

plt.gca().set_facecolor('white')
plt.xticks(positions, seasonNames)
plt.title('Seasonal Box Plots')
plt.xlabel('Seasons')
plt.ylabel('PM SOA markers (ng/m^3)')
plt.grid(False)  # Remove the grids
plt.savefig('seasonal_box_plots_pmSoa.png', dpi=300)  # Set dpi for high-resolution

plt.show()
