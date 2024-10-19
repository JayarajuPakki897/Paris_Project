clc;clear; clear all
cd F:\Ph.D\Project_PAH\Data
df=xlsread('SIRTA_long term_2015_Max Planck_complete_vf02.xlsx','PM_SOA_markers');
excelFile = 'SIRTA_long term_2015_Max Planck_complete_vf02.xlsx';
sheetName = 'PM_SOA_markers';

% Read the specified sheet into a table
dataTable = readtable(excelFile, 'Sheet', sheetName);
time=dataTable.Var1
months = month(time)
dataTable.Month = month(dataTable.Var1);
Latitude Longitude
winterData = dataTable(dataTable.Month == 12 | dataTable.Month == 1 | dataTable.Month == 2, :); % Dec, Jan, Feb
springData = dataTable(dataTable.Month == 3 | dataTable.Month == 4 | dataTable.Month == 5, :);   % Mar, Apr, May
summerData = dataTable(dataTable.Month == 6 | dataTable.Month == 7 | dataTable.Month == 8, :);   % Jun, Jul, Aug
autumnData = dataTable(dataTable.Month == 9 | dataTable.Month == 10 | dataTable.Month == 11, :); % Sep, Oct, Nov
winterDatasum = sum(winterData{:, 2:26}, 2);
springDatasum = sum(springData{:, 2:26}, 2);
summerDatasum = sum(summerData{:, 2:26}, 2);
autumnDatasum = sum(autumnData{:, 2:26}, 2);
positions=1:4
% Assuming you have already defined winterDatasum, springDatasum, summerDatasum, autumnDatasum, and positions

% Data in a cell array for easier handling in a loop
seasonalData = {winterDatasum, springDatasum, summerDatasum, autumnDatasum};
seasonNames = {'Winter', 'Spring', 'Summer', 'Autumn'};

% Create side-by-side box plots using a loop
figure;
for i = 1:length(seasonalData)
    boxplot(seasonalData{i}, 'positions', positions(i));
    hold on;
end
hold off;
set(gca, 'FontName', 'Times New Roman');
% Add season names to the x-axis
xticks(positions);
xticklabels(seasonNames);

title('Seasonal Box Plots');
xlabel('Seasons');
ylabel('PM SOA markers (ng/m^3)');
% saveas(gcf, 'F:\Ph.D\Project_PAH\Data\Seasonal_Box_Plots.png', 'png');

%%%%%%OUTLIER REMOVED%%%%%
cd C:\Users\hp\Downloads
filen='CH0001G.20110101000500.20180208000000.online_gc..air.6y.2h.CH01L_Agilent_GC-MS-MEDUSA_Medusa-12_JFJ.CH01L_VOC_AIR_MEDUSA-12.lev2.nc'
info = ncinfo(filen);
numeric_dates=ncread(filen,'time')

date_strings = num2str(numeric_dates);

% Step 3: Convert strings to datetime format
dates = datetime(date_strings, 'InputFormat', 'yyyyMMddHHmmss');

% Display the converted dates
disp(dates);


% Extract variable names
variables = {info.Variables.Name};

% Display variable names
disp('Variable Names:');
numeric_dates=ncread(filen,'time')
reference_date = datetime(2011, 1, 1); % replace with your reference date if different

% Step 3: Convert numeric dates to datetime format
dates = reference_date + days(numeric_dates);

% Display the converted dates
disp(dates);

reference_date = datetime(1900, 1, 1); % replace with your reference date if different

% Step 3: Convert numeric dates to datetime by adding the numeric values to the reference date
dates = reference_date + days(numeric_dates);
disp(dates);


% Step 2: Convert numeric dates to strings ensuring proper format
date_strings = arrayfun(@(x) sprintf('%014.0f', x), numeric_dates, 'UniformOutput', false);

% Step 3: Convert cell array of strings to datetime format
dates = datetime(date_strings, 'InputFormat', 'yyyyMMddHHmmss');

% Display the converted dates
disp(dates);