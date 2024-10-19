import pandas as pd
import plotly.express as px
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
# Specify the Excel file path and sheet name
excel_file_path = r'F:\Ph.D\Project_PAH\Data\SIRTA_long term_2015_Max Planck_complete_vf02.xlsx'
sheet_name = 'p+g_SOA_markers'

# Define the column names with additional information
bsoa_columns = ['SUCCINIC ACID', 'ALPHA-METHYLGLYCERIC ACID', 'PINONIC ACID', '3-HYDROXYGLUTARIC ACID',
                '3-(2-HYDROXY-ETHYL)-2,2-DIMETHYLCYCLOBUT', '3-HYDROX-4,4--DIMETHYLGLUTARIC ACID',
                '3-ACETYLPENTANEDIOIC ACID', 'PINIC ACID', '3-ACETYL HEXANEDIOIC ACID', '3-ISOPROPYLPENTANEDIOIC ACID',
                'TERPENYLIC ACID', '2-METHYLTHREITOL', '2-METHYL ERYTHRITOL', 'MBTCA', 'BETA-CARYOPHYLLINIC ACID']

asoa_columns = ['DHOPA', 'PHTHALIC ACID', '2-NITROPHENOL', '4-NITROPHENOL', '2-METHYL-4-NITROPHENOL',
                '4-NITROGUAIACOL', '5-NITROGUAIACOL', '4-METHYL-5-NITROCATHECOL', '3-METHYL-6-NITROCATHECOL',
                '3-METHYL-5-NITROCATHECOL']

# Read the specified sheet into a DataFrame
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Extract the ASOA and BSOA data, drop NaN values
asoa_data = df[asoa_columns][1:].dropna()
bsoa_data = df[bsoa_columns][1:].dropna()

# Calculate the sum of all elements in each column for ASOA and BSOA
sum_asoa = asoa_data.sum().sum()
sum_bsoa = bsoa_data.sum().sum()

# Calculate the mean of all elements in each column for ASOA and BSOA
mean_asoa = (asoa_data.sum() / sum_asoa * 100)
mean_bsoa = (bsoa_data.sum() / sum_bsoa * 100)

# Create a DataFrame with mean values and column names
mean_df = pd.DataFrame({
    'Component': mean_asoa.index.tolist() + mean_bsoa.index.tolist(),
'Mean Percentage': mean_asoa.apply(lambda x: f'{x:.2f}').tolist() + mean_bsoa.apply(lambda x: f'{x:.2f}').tolist(),
    'Mean Absolute Value (µg/m³)': [f'{val:.1f}' for val in mean_asoa / 100 * sum_asoa] +
                                     [f'{val:.1f}' for val in mean_bsoa / 100 * sum_bsoa],
    'Group': ['ASOA'] * len(mean_asoa) + ['BSOA'] * len(mean_bsoa)
})

# Filter the DataFrame for BSOA and ASOA
bsoa_df = mean_df[mean_df['Group'] == 'BSOA']
asoa_df = mean_df[mean_df['Group'] == 'ASOA']

# Create separate circular plots for BSOA and ASOA
fig_bsoa = px.sunburst(bsoa_df, path=['Group', 'Component'], values='Mean Percentage',
                       title='Circular Plot of Mean Percentage for BSOA (µg/m³)')
fig_asoa = px.sunburst(asoa_df, path=['Group', 'Component'], values='Mean Percentage',
                       title='Circular Plot of Mean Percentage for ASOA (µg/m³)')

# Update the text labels to show names, percentages, and absolute values
fig_bsoa.update_traces(textinfo='label+percent entry+value')
fig_asoa.update_traces(textinfo='label+percent entry+value')

# Show the plots
fig_bsoa.show()
fig_asoa.show()

output_directory = r'F:\Ph.D\Project_PAH\Data'

# Create a circular plot using plotly for ASOA
fig_asoa = px.sunburst(mean_df[mean_df['Group'] == 'ASOA'], path=['Component'], values='Mean Percentage',
                       title='Circular Plot of Mean Percentage for ASOA')
fig_asoa.update_traces(textinfo='label+percent entry+value')

# Save ASOA circular plot as image in the specified directory with high quality
fig_asoa.write_image(f'{output_directory}\\circular_plot_asoa.png', engine='kaleido', scale=4)

# Create a circular plot using plotly for BSOA
fig_bsoa = px.sunburst(mean_df[mean_df['Group'] == 'BSOA'], path=['Component'], values='Mean Percentage',
                       title='Circular Plot of Mean Percentage for BSOA')
fig_bsoa.update_traces(textinfo='label+percent entry+value')

# Save BSOA circular plot as image in the specified directory with high quality
fig_bsoa.write_image(f'{output_directory}\\circular_plot_bsoa.png', engine='kaleido', scale=4)

# Create a DataFrame with mean values and column names
mean_df = pd.DataFrame({
    'Component': mean_asoa.index.tolist() + mean_bsoa.index.tolist(),
    'ASOA_Mean_Percentage': mean_asoa.tolist() + [0] * len(mean_bsoa),
    'BSOA_Mean_Percentage': [0] * len(mean_asoa) + mean_bsoa.tolist(),
    'ASOA_Mean_Absolute_Value (µg/m³)': [f'{val:.2f}' for val in mean_asoa / 100 * sum_asoa],
    'BSOA_Mean_Absolute_Value (µg/m³)': [f'{val:.2f}' for val in mean_bsoa / 100 * sum_bsoa]
})

# Display the DataFrame
print(mean_df[['Component', 'ASOA_Mean_Percentage', 'BSOA_Mean_Percentage', 'ASOA_Mean_Absolute_Value (µg/m³)', 'BSOA_Mean_Absolute_Value (µg/m³)']])