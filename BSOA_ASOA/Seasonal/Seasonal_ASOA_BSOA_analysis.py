import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame, skipping the first two rows
excel_file = r'F:\Ph.D\Project_PAH\Data\SIRTA_long term_2015_Max Planck_complete_vf02.xlsx'
sheet_name = 'PM_SOA_markers'
dataTable = pd.read_excel(excel_file, sheet_name=sheet_name, skiprows=[0, 1])

# Rename columns
dataTable.columns = ['Sampling date', 'SUCCINIC ACID', 'ALPHA-METHYLGLYCERIC ACID', 'DHOPA', 'PINONIC ACID',
                     '3-HYDROXYGLUTARIC ACID', '3-(2-HYDROXY-ETHYL)-2,2-DIMETHYLCYCLOBUT', '3-HYDROX-4,4--DIMETHYLGLUTARIC ACID',
                     '3-ACETYLPENTANEDIOIC ACID', 'PINIC ACID', 'PHTHALIC ACID', '3-ACETYL HEXANEDIOIC ACID',
                     '3-ISOPROPYLPENTANEDIOIC ACID', 'TERPENYLIC ACID', '2-NITROPHENOL', '4-NITROPHENOL',
                     '2-METHYL-4-NITROPHENOL', '4-NITROGUAIACOL', '5-NITROGUAIACOL', '4-METHYL-5-NITROCATHECOL',
                     '3-METHYL-6-NITROCATHECOL', '3-METHYL-5-NITROCATHECOL', '2-METHYLTHREITOL', '2-METHYL ERYTHRITOL',
                     'MBTCA', 'BETA-CARYOPHYLLINIC ACID']

# Convert the "Sampling date" column to datetime format
dataTable['Sampling date'] = pd.to_datetime(dataTable['Sampling date'], format='%d/%m/%Y %H:%M:%S', errors='coerce')

# Drop rows with missing datetime values
dataTable.dropna(subset=['Sampling date'], inplace=True)

# Define the column names for BSOA and ASOA
bsoa_columns = ['SUCCINIC ACID', 'ALPHA-METHYLGLYCERIC ACID', 'PINONIC ACID', '3-HYDROXYGLUTARIC ACID',
                '3-(2-HYDROXY-ETHYL)-2,2-DIMETHYLCYCLOBUT', '3-HYDROX-4,4--DIMETHYLGLUTARIC ACID',
                '3-ACETYLPENTANEDIOIC ACID', 'PINIC ACID', '3-ACETYL HEXANEDIOIC ACID', '3-ISOPROPYLPENTANEDIOIC ACID',
                'TERPENYLIC ACID', '2-METHYLTHREITOL', '2-METHYL ERYTHRITOL', 'MBTCA', 'BETA-CARYOPHYLLINIC ACID']

asoa_columns = ['DHOPA', 'PHTHALIC ACID', '2-NITROPHENOL', '4-NITROPHENOL', '2-METHYL-4-NITROPHENOL',
                '4-NITROGUAIACOL', '5-NITROGUAIACOL', '4-METHYL-5-NITROCATHECOL', '3-METHYL-6-NITROCATHECOL',
                '3-METHYL-5-NITROCATHECOL']

# Remove NaN values from BSOA and ASOA columns
dataTable.dropna(subset=bsoa_columns + asoa_columns, how='any', inplace=True)

# Extract time and month information
time = dataTable['Sampling date']
months = time.dt.month

# Divide data into seasons
winterData = dataTable[(months == 12) | (months == 1) | (months == 2)]  # Dec, Jan, Feb
springData = dataTable[(months == 3) | (months == 4) | (months == 5)]   # Mar, Apr, May
summerData = dataTable[(months == 6) | (months == 7) | (months == 8)]   # Jun, Jul, Aug
autumnData = dataTable[(months == 9) | (months == 10) | (months == 11)] # Sep, Oct, Nov

# Calculate the sum of BSOA and ASOA markers for each season
seasonal_data = {
    'Winter': {'BSOA': winterData[bsoa_columns].sum(axis=1), 'ASOA': winterData[asoa_columns].sum(axis=1)},
    'Spring': {'BSOA': springData[bsoa_columns].sum(axis=1), 'ASOA': springData[asoa_columns].sum(axis=1)},
    'Summer': {'BSOA': summerData[bsoa_columns].sum(axis=1), 'ASOA': summerData[asoa_columns].sum(axis=1)},
    'Autumn': {'BSOA': autumnData[bsoa_columns].sum(axis=1), 'ASOA': autumnData[asoa_columns].sum(axis=1)}
}

positions = np.arange(1, 5)

# Create side-by-side box plots
fig, ax = plt.subplots(figsize=(12, 6))

# Offset for ASOA positions
offset = 0.2

# Plot BSOA and ASOA side by side
for i, season in enumerate(seasonal_data.keys()):
    bsoa_data = seasonal_data[season]['BSOA']
    asoa_data = seasonal_data[season]['ASOA']
    
    # Plot BSOA
    ax.boxplot(bsoa_data, positions=[positions[i] - offset], widths=0.2, patch_artist=True,
               boxprops=dict(facecolor="C0"), medianprops=dict(color="C0"), showmeans=True, showfliers=False)
    
    # Plot ASOA
    ax.boxplot(asoa_data, positions=[positions[i] + offset], widths=0.2, patch_artist=True,
               boxprops=dict(facecolor="C1"), medianprops=dict(color="C1"), showmeans=True, showfliers=False)

# Customize the plot
ax.set_xticks(positions)
ax.set_xticklabels(seasonal_data.keys())
ax.set_xlabel('Seasons')
ax.set_ylabel('Concentration (ng/m³)')
ax.set_title('Seasonal Box Plots for BSOA and ASOA')

# Add a legend
handles = [plt.Line2D([0], [0], color='C0', label='BSOA', linewidth=3),
           plt.Line2D([0], [0], color='C1', label='ASOA', linewidth=3)]
ax.legend(handles=handles, loc='upper right')

# Set background color to white and remove grid
ax.set_facecolor('white')
plt.grid(False)

# Save and show the plot
plt.savefig('seasonal_box_plots_bsoa_asoa__.png', dpi=300)  # Set dpi for high-resolution
plt.show()
