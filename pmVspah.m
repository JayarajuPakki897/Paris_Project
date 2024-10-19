 cd F:\Ph.D\Project_PAH\Data
SD=xlsread('SIRTA_long term_2015_Max Planck_complete_vf02.xlsx','Database');
pm10=SD(:,1)
pgsoamarkers=xlsread('SIRTA_long term_2015_Max Planck_complete_vf02.xlsx','p+g PAHs')
pandg=sum(pgsoamarkers,2)
ppahdata=xlsread('SIRTA_long term_2015_Max Planck_complete_vf02.xlsx','Particulatephase_PAHs')
ppah=sum(ppahdata,2)
pbypg=ppah./pandg
pbypg(isnan(pbypg))=0;
pm10(isnan(pm10))=0;

set(0, 'DefaultAxesFontName', 'Times', 'DefaultAxesFontWeight', 'bold');
 
scatter(pm10/1000,pbypg)
%scatter(pm10/1000,ppah)
%xlim([0, 40]); % Set x-axis limits to -3 and 3
%ylim([0, 0.03]);
xlabel('PM_{10} (µg/m^3)');
ylabel('P/P+G');

%ylabel('PAHs (ng/m^3)');

% % Perform linear fit using polyfit
% degree = 1;  % Degree of the polynomial (1 for linear)
% coefficients = polyfit(pm10, ppah, degree);
% 
% % Evaluate the linear fit over a range of x values
% x_fit = linspace(min(pm10), max(pm10), 100);
% y_fit = polyval(coefficients, x_fit);
% 
% % Plot the linear fit
% hold on;
% plot(x_fit, y_fit, 'r-', 'LineWidth', 2);  % Red line for the fit
% hold off;
