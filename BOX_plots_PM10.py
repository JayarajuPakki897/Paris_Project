import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Change directory to the specified path
data_path = r'E:\Phd\Project_PAH\Data\SIRTA_long term_2015_Max Planck_complete_vf02.xlsx'
df = pd.read_excel(data_path, sheet_name='Database', skiprows=1)
#df = df.dropna()

df1 = pd.read_excel(data_path, sheet_name='Particulatephase_PAHs', skiprows=1)
df2 = pd.read_excel(data_path, sheet_name='p+g PAHs', skiprows=1)

# Convert the values in the first column to numeric and divide by 1000
data = pd.to_numeric(df.iloc[:, 1], errors='coerce').div(1000).values
ppah_sum = df1.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').sum(axis=1).div(1000).values
pg_pah_sum = df2.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').sum(axis=1).div(1000).values
ratio = ppah_sum / pg_pah_sum
print(ratio)
# Define edges for histogram bins
edges = np.arange(0, 101, 10)

# Use numpy.histogram to classify data into 10 groups
counts, bin_edges = np.histogram(data, bins=edges)

# Group data into a list based on discretized values
grouped_data = [df.iloc[(data >= edges[i]) & (data < edges[i+1])].index for i in range(len(edges)-1)]

# Create pairs of 'values' and 'ratio' for each group
value_ratio_pairs = [(pd.to_numeric(df.iloc[grouped_data[i], 1], errors='coerce').div(1000).values,
                      ratio[grouped_data[i]]) for i in range(len(grouped_data))]


for i, pair in enumerate(value_ratio_pairs):
    pm10_values = pair[0]  # PM10 values for the i-th group
    ratio_values = pair[1]  # Ratio values for the i-th group
    
    # Now you can work with pm10_values and ratio_values
    print(f"Group {i+1}:")
    print("PM10 values:", pm10_values)
    print("Ratio values:", ratio_values)
    print()
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Extract temperature values from the DataFrame
temperature_values = df.iloc[:, 65].values  # Assuming temperature is at column index 65

# Create pairs of 'PM10', 'ratio', and 'temperature' for each group
data_pairs = [(pd.to_numeric(df.iloc[grouped_data[i], 1], errors='coerce').div(1000).values,
               ratio[grouped_data[i]],
               temperature_values[grouped_data[i]]) for i in range(len(grouped_data))]

# Create a grid of correlation plots
num_groups = len(grouped_data)
num_columns = 3  # Number of columns for PM10, ratio, and temperature
num_rows = (num_groups + num_columns - 1) // num_columns

# Set up the subplots

# Flatten the axes array for easier iteration

# Iterate through the pairs and create correlation plots


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Extract temperature, RH, WS, SF, and O3 values from the DataFrame
temperature_values = df.iloc[:, 65].values  # Assuming temperature is at column index 65
rh_values = df.iloc[:, 64].values  # Assuming relative humidity is at column index 64
ws_values = df.iloc[:, 66].values  # Assuming wind speed is at column index 66
sf_values = df.iloc[:, 68].values  # Assuming solar flux is at column index 68
o3_values = df.iloc[:, 63].values  # Assuming O3 is at column index 63

# Create pairs of 'PM10', 'ratio', 'temperature', 'RH', 'WS', 'SF', and 'O3' for each group
data_pairs = [(pd.to_numeric(df.iloc[grouped_data[i], 1], errors='coerce').div(1000).values,
               ratio[grouped_data[i]],
               temperature_values[grouped_data[i]],
               rh_values[grouped_data[i]],
               ws_values[grouped_data[i]],
               sf_values[grouped_data[i]],
               o3_values[grouped_data[i]]) for i in range(len(grouped_data))]

# Iterate through the pairs and create correlation plots for each group in a separate figure
for i, (pm10_values, ratio_values, temperature_values, rh_values, ws_values, sf_values, o3_values) in enumerate(data_pairs):
    # Create a new figure
    plt.figure(figsize=(8, 6))
    
    # Create a DataFrame with the data
    df_corr = pd.DataFrame({'PM$_{10}$ (µg/m$^3$)': pm10_values,
                            'P/P+G': ratio_values,
                            'Temp': temperature_values,
                            'RH': rh_values,
                            'WS': ws_values,
                            'SF': sf_values,
                            'O3': o3_values})
    
    # Create the correlation plot
    sns.heatmap(df_corr.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title(f'Correlation Plot for Group {i+1}')
    plt.xlabel('Variables')
    plt.ylabel('Variables')
    # plt.savefig(f'correlation_plot_group_{i+1}.png')

    # Show the plot
    plt.show()


# # Create a grid of correlation plots
# num_groups = len(grouped_data)
# num_columns = 2  # You can adjust the number of columns based on your preference
# num_rows = (num_groups + num_columns - 1) // num_columns

# # Set up the subplots
# fig, axes = plt.subplots(num_rows, num_columns, figsize=(12, 6))

# # Flatten the axes array for easier iteration
# axes = axes.flatten()

# # Iterate through the pairs and create correlation plots
# for i, (values, ratio_values) in enumerate(value_ratio_pairs):
#     ax = axes[i]
#     sns.heatmap(pd.DataFrame({'PM$_{10}$ (µg/m$^3$)': values, "$\\frac{P}{P+G}$": ratio_values}).corr(),
#                 annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
#     ax.set_title(f'Group {i+1}')

# # Remove any empty subplots
# for i in range(num_groups, len(axes)):
#     fig.delaxes(axes[i])

# # Adjust layout and show the figure
# plt.tight_layout()
# plt.show()



                                                                           ###Type2###
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Change directory to the specified path
# data_path = r'F:\Ph.D\Project_PAH\Data\SIRTA_long term_2015_Max Planck_complete_vf02.xlsx'
# df = pd.read_excel(data_path, sheet_name='Database', skiprows=1)
# df1 = pd.read_excel(data_path, sheet_name='Particulatephase_PAHs', skiprows=1)
# df2 = pd.read_excel(data_path, sheet_name='p+g PAHs', skiprows=1)

# # Convert the values in the first column to numeric and divide by 1000
# data = pd.to_numeric(df.iloc[:, 1], errors='coerce').div(1000).values
# ppah_sum = df1.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').sum(axis=1).div(1000).values
# pg_pah_sum = df2.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').sum(axis=1).div(1000).values
# ratio = ppah_sum / pg_pah_sum

# # Define edges for histogram bins
# edges = np.arange(0, 101, 10)

# # Use numpy.histogram to classify data into 10 groups
# counts, bin_edges = np.histogram(data, bins=edges)

# # Group data into a list based on discretized values
# grouped_data = [df.iloc[(data >= edges[i]) & (data < edges[i+1])].index for i in range(len(edges)-1)]

# # Create pairs of 'values' and 'ratio' for each group
# value_ratio_pairs = [(pd.to_numeric(df.iloc[grouped_data[i], 1], errors='coerce').div(1000).values,
#                       ratio[grouped_data[i]]) for i in range(len(grouped_data))]

# # Create a single figure for all scatter plots
# fig, axes = plt.subplots(figsize=(12, 8))

# # Iterate through the pairs and create scatter plots
# for i, (values, ratio_values) in enumerate(value_ratio_pairs):
#     sns.scatterplot(x=values, y=ratio_values, label=f'Group {i+1}')
    
#     # Calculate correlation coefficient
#     corr_coefficient = np.corrcoef(values, ratio_values)[0, 1]
    
#     # Display correlation coefficient value
#     plt.text(0.95, 0.1 + i * 0.1, f'Corr: {corr_coefficient:.2f}', transform=axes.transAxes, color='black')

# # Set labels and title
# plt.xlabel('PM$_{10}$ (µg/m$^3$)')
# plt.ylabel("$\\frac{P}{P+G}$")
# plt.title('Scatter Plots for Different Groups')

# # Add legend
# plt.legend()

# # Show the figure
# plt.show()
