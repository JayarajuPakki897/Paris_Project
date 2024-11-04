% Define the file path
file_path = 'E:\Phd\Project_PAH\Data\FR0020R.20150101100028.20170731000000.ads_tube..air.20mo.34h.FR01L_PerkinElmer.FR01L_NMHC_analysis.lev2.nc';

% Open the NetCDF file
ncid = netcdf.open(file_path, 'NC_NOWRITE');

% Get the number of variables in the file
[~, nvars, ~, ~] = netcdf.inq(ncid);

% Initialize a cell array to hold variable names ending with 'amean'
expunc2s_vars = {};

% Loop through all variables and collect those ending with 'amean'
for varid = 0:nvars-1
    try
        varname = netcdf.inqVar(ncid, varid);
        if endsWith(varname, 'amean', 'IgnoreCase', true)
            expunc2s_vars{end+1} = varname; %#ok<AGROW>
        end
    catch ME
        warning('Could not retrieve variable name for ID %d: %s', varid, ME.message);
    end
end

% Close the NetCDF file
netcdf.close(ncid);

% Reopen the NetCDF file to read data
ncid = netcdf.open(file_path, 'NC_NOWRITE');

% Define the reference date for time conversion
ref_date = datetime(1900, 1, 1, 0, 0, 0, 'TimeZone', 'UTC');

% Create a figure for plotting
figure('Position', [100, 100, 800, 600]); % Set figure size
hold on; % Allow multiple plots on the same figure

% Loop through the variables and plot each
for i = 1:length(expunc2s_vars)
    varname = expunc2s_vars{i};
    try
        % Read the time variable
        time_varid = netcdf.inqVarID(ncid, 'time'); % Assume time variable name is 'time'
        time_data = netcdf.getVar(ncid, time_varid);
        time_units = netcdf.getAtt(ncid, time_varid, 'units');
        
        % Convert the numeric time data to datetime
        tokens = regexp(time_units, '(\w+)\s+since\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})', 'tokens');
        time_unit = tokens{1}{1};
        ref_date_str = tokens{1}{2};
        ref_date = datetime(ref_date_str, 'InputFormat', 'yyyy-MM-dd HH:mm:ss');
        
        switch time_unit
            case 'seconds'
                time_dates = ref_date + seconds(time_data);
            case 'minutes'
                time_dates = ref_date + minutes(time_data);
            case 'hours'
                time_dates = ref_date + hours(time_data);
            case 'days'
                time_dates = ref_date + days(time_data);
            otherwise
                error('Unknown time unit: %s', time_unit);
        end
        
        % Read the data for the current variable
        varid = netcdf.inqVarID(ncid, varname);
        data = netcdf.getVar(ncid, varid);
        
        % Remove the last 5 characters from the variable name for the legend
        legend_name = varname(1:end-6);  % Keep everything except the last 5 characters
        
        % Plot the data with increased line width
        plot(time_dates, data, 'DisplayName', legend_name, 'LineWidth', 2); % Set LineWidth to 2 or any desired value
        
    catch ME
        warning('Could not read or plot variable %s: %s', varname, ME.message);
    end
end

% Close the NetCDF file
netcdf.close(ncid);

% Add labels, title, legend, and grid
xlabel('Time', 'FontName', 'Times New Roman', 'FontWeight', 'bold', 'FontSize', 12);
ylabel('Concentration (pmol/mol)', 'FontName', 'Times New Roman', 'FontWeight', 'bold', 'FontSize', 12);
title('Time Series of Variables Ending with ExpUnc2s', 'FontName', 'Times New Roman', 'FontWeight', 'bold', 'FontSize', 14);
legend('show', 'FontName', 'Times New Roman', 'FontWeight', 'bold');
grid on;

% Set high DPI for the figure
set(gcf, 'PaperPosition', [0 0 8 6]); % Size in inches
set(gcf, 'PaperSize', [8 6]); % Paper size in inches
print(gcf, 'TimeSeriesPlot.png', '-dpng', '-r300'); % Save as PNG with 300 DPI

hold off;

% Display the plot
disp('Time series plot of ExpUnc2s variables:');
