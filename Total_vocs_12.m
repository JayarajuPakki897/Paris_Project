try
    % Define the file path
    file_path = 'F:\Ph.D\Project_PAH\Data\FR0020R.20150101100028.20170731000000.ads_tube..air.20mo.34h.FR01L_PerkinElmer.FR01L_NMHC_analysis.lev2.nc';

    % Open the NetCDF file
    ncid = netcdf.open(file_path, 'NC_NOWRITE');

    % Get the number of variables in the file
    [~, nvars, ~, ~] = netcdf.inq(ncid);

    % Initialize a cell array to hold variable names ending with 'ExpUnc2s'
    expunc2s_vars = {};

    % Loop through all variables and collect those ending with 'ExpUnc2s'
    for varid = 0:nvars-1
        try
            varname = netcdf.inqVar(ncid, varid);
            if endsWith(varname, 'ExpUnc2s', 'IgnoreCase', true)
                expunc2s_vars{end+1} = varname; %#ok<AGROW>
            end
        catch ME
            warning('Could not retrieve variable name for ID %d: %s', varid, ME.message);
        end
    end

    % Close the NetCDF file
    netcdf.close(ncid);

    % Print the collected variable names
    disp('Variables ending with ExpUnc2s:');
    disp(expunc2s_vars);

catch ME
    disp('An error occurred:');
    disp(ME.message);
end
