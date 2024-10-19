# import pandas as pd
# import matplotlib.pyplot as plt
# from windrose import WindroseAxes

# # Replace 'your_file_path' with the actual path to your Excel file
# file_path = r'F:\Ph.D\Project_PAH\Data\SIRTA_long term_2015_Max Planck_complete_vf02.xlsx'

# # Specify the sheet name
# sheet_name = 'Database'

# # Read the Excel file
# df = pd.read_excel(file_path, sheet_name)

# # Convert 'Wd' and 'Ws' columns to numeric, coercing errors
# df['Wd'] = pd.to_numeric(df['Wd'], errors='coerce')
# df['Ws'] = pd.to_numeric(df['Ws'], errors='coerce')

# # Drop rows with NaN values (non-convertible entries)
# df = df.dropna(subset=['Wd', 'Ws'])

# # Add a new column for wind speed categories
# bins = [0, 0.5, 1.5, 3.3, 5.5, 7.9, 10.8, float('inf')]
# labels = ['Calm', 'Light Air', 'Light Breeze', 'Gentle Breeze', 'Moderate Breeze', 'Strong Breeze', 'Very Strong Breeze']
# df['WindSpeedCategory'] = pd.cut(df['Ws'], bins=bins, labels=labels)

# # Create a WindroseAxes
# ax = WindroseAxes.from_ax()
# ax.bar(df['Wd'], df['Ws'], normed=True, opening=0.8, edgecolor='white', nsector=8, bins=bins)

# # Set the direction labels
# ax.set_thetagrids(range(0, 360, 45), labels=["N", "NE", "E", "SE", "S", "SW", "W", "NW"])

# # Add a legend with wind speed categories
# ax.legend(title='Wind Speed Category', loc='upper right')

# # Add a title
# plt.title("Wind Rose Plot")

# # Show the plot
# plt.show()


                                        #$#Seasonal Wind plots
                                        
                                        
import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes

# Replace 'your_file_path' with the actual path to your Excel file
file_path = r'F:\Ph.D\Project_PAH\Data\SIRTA_long term_2015_Max Planck_complete_vf02.xlsx'

# Specify the sheet name
sheet_name = 'Database'

# Read the Excel file
df = pd.read_excel(file_path, sheet_name)

# Convert 'Wd' and 'Ws' columns to numeric, coercing errors
df['Wd'] = pd.to_numeric(df['Wd'], errors='coerce')
df['Ws'] = pd.to_numeric(df['Ws'], errors='coerce')

# Drop rows with NaN values (non-convertible entries)
df = df.dropna(subset=['Wd', 'Ws'])

# Add a new column for wind speed categories
bins = [0, 0.5, 1.5, 3.3, 5.5, 7.9, 10.8, float('inf')]
labels = ['Calm', 'Light Air', 'Light Breeze', 'Gentle Breeze', 'Moderate Breeze', 'Strong Breeze', 'Very Strong Breeze']
df['WindSpeedCategory'] = pd.cut(df['Ws'], bins=bins, labels=labels)

# Extract month information from the date column
df['Month'] = pd.to_datetime(df.iloc[:, 0]).dt.month

# Define seasons based on months
spring = df[(df['Month'] >= 3) & (df['Month'] <= 5)]
summer = df[(df['Month'] >= 6) & (df['Month'] <= 8)]
fall = df[(df['Month'] >= 9) & (df['Month'] <= 11)]
winter = df[df['Month'].isin([12, 1, 2])]

# Create separate wind rose plots for each season
seasons = [('Spring', spring), ('Summer', summer), ('Monsoon', fall), ('Winter', winter)]

for season_name, season_df in seasons:
    # Create a WindroseAxes
    ax = WindroseAxes.from_ax()
    ax.bar(season_df['Wd'], season_df['Ws'], normed=True, opening=0.8, edgecolor='white', nsector=8, bins=bins)

    # Set the direction labels
    ax.set_thetagrids(range(0, 360, 45), labels=["N", "NE", "E", "SE", "S", "SW", "W", "NW"])

    # Add a legend with wind speed categories
    ax.legend(title='Wind Speed Category', loc='upper right')

    # Add a title for each season
    plt.title(f"Wind Rose Plot - {season_name}")

    # Show the plot for each season
    plt.show()




