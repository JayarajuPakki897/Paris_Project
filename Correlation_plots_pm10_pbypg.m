cd F:\Ph.D\Project_PAH\Data
filen='SIRTA_long term_2015_Max Planck_complete_vf02.xlsx'
df=xlsread(filen,'Database');
pm10data=df(:,1)/1000
pg_pahs=xlsread(filen,'p+g PAHs')
pandg_pahs=sum(pg_pahs,2)
ppahdata=xlsread(filen,'Particulatephase_PAHs')
ppah=sum(ppahdata,2)
pbypg=ppah./pandg_pahs
pbypg(isnan(pbypg))=0;

% Define edges for histogram bins
edges = 0:10:100;

% Use histcounts to classify data into 10 groups
[counts, binEdges] = histcounts(pm10data, edges);


% Group data into cell array based on discretized values
groupedData = accumarray(discretize(pm10data, edges), pm10data, [], @(x) {x});
numGroups = sum(~cellfun('isempty', groupedData));

% Create side-by-side box plots
positions = 1:numGroups;
for i=1:length(groupedData)
    boxplot(groupedData{i}, 'positions', positions(i));
    hold on;
end
hold off;
groupedData = accumarray(discretize(data, edges), 1:numel(pm10data), [], @(x) {x});
groupIndices = cellfun(@(x) x(:), groupedData, 'UniformOutput', false);
for i = 1:numGroups
    boxplot(pbypg(groupedData{i}), 'positions', positions(i));
    hold on;
    fprintf('Group %d: Rows %s\n', i, mat2str(groupedData{i}'));
end
hold off;



xticks(1:numGroups);
xticklabels(arrayfun(@(x) sprintf('%d-%d', edges(x), edges(x+1)), 1:numel(edges)-1, 'UniformOutput', false));

title('Box Plot of PM10 Data Classified into 10 Groups');
xlabel('Groups');
ylabel('PM_{10} Concentration (µg/m^3)', 'FontName', 'Times New Roman');


