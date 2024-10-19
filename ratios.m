%% EC/OC ratio for March 2015
cd F:\Ph.D\Project_PAH\Data
filen='SIRTA_database_March_2015.xlsx'
Data=readmatrix(filen)
OC=Data(:,2)
EC=Data(:,3)
tabledata=readtable(filen)
date= tabledata.ng_m3
ecocratio=EC./OC
plot(date, ecocratio);
ylabel('EC/OC')
xlabel('Time')
% xticklabels(date)
% set(gca,'xtick',1:22,'FontWeight', 'bold');
xticks(date(1:5:end+1));
% xtickformat('yyyy-mm-dd')
set(gca, 'FontSize', 12, 'FontWeight', 'bold');
xtickangle(45);

