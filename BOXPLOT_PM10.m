cd F:\Ph.D\Project_PAH\Data
df=xlsread('SIRTA_long term_2015_Max Planck_complete_vf02.xlsx','Database');
data=df(:,1)/1000


% Define edges for histogram bins
edges = 0:10:100;

% Use histcounts to classify data into 10 groups
[counts, binEdges] = histcounts(data, edges);


% Group data into cell array based on discretized values
groupedData = accumarray(discretize(data, edges), data, [], @(x) {x});
numGroups = sum(~cellfun('isempty', groupedData));

% Create side-by-side box plots
positions = 1:numGroups;
for i=1:length(groupedData)
    boxplot(groupedData{i}, 'positions', positions(i));
    hold on;
end
hold off;
xticks(1:numGroups);
xticklabels(arrayfun(@(x) sprintf('%d-%d', edges(x), edges(x+1)), 1:numel(edges)-1, 'UniformOutput', false));

title('Box Plot of PM10 Data Classified into 10 Groups');
xlabel('Groups');
ylabel('PM_{10} Concentration (µg/m^3)', 'FontName', 'Times New Roman');















% Specify the path to the shapefile
shapefilePath = 'F:\Ph.D\Project_Covid\Data\Delhi\NCR_Districts\NCR_Districts.shp';

% Read the shapefile using shaperead
shapefileData = shaperead(shapefilePath);

% Display information about the shapefile
disp('Shapefile Information:');
disp(shapefileData);
% for i=1:25
% Plot all polygons with a light gray color
figure;
mapshow(shapefileData, 'DisplayType', 'polygon', 'FaceColor', [0.9, 0.9, 0.9]);

hold on;

% Plot the 15th polygon with red color
polygon15 = shapefileData(2);
mapshow(polygon15, 'DisplayType', 'polygon', 'FaceColor', 'red');
% end
hold off;

% Customize the plot if needed
title('NCR Districts');
xlabel('Longitude');
ylabel('Latitude');

