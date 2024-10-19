clc; clear; clear all
cd F:\Ph.D\Project_PAH\Data
%% EC/OC
filen='SIRTA_long term_2015_Max Planck_complete_vf02.xlsx'
data=readmatrix(filen)
EC=data(:,4)
OC=data(:,3)
ecocratio=EC./OC
tabledata=readtable(filen)
date=tabledata.Var1
plot(date, ecocratio);
xticks(date(5:4:end));
ylabel('EC/OC')
xlabel('Time')
%% NO2 Vs O3
NO2=data(:,63)
O3=data(:,64)
O3(isnan(O3)) =0;
yyaxis left
plot(date,NO2)
ylabel ('NO_2 (ppb)')
yyaxis right
plot(date,O3)
xlabel('Time')
ylabel ('O_3 (ppb)')
xticks(date(5:4:end));
% plot(NO2./O3)


%% pm SOA markers
PM_SOA_markers=xlsread('SIRTA_long term_2015_Max Planck_complete_vf02.xlsx','PM_SOA_markers')
Totalpmsoa=sum(PM_SOA_markers)
pmsoatable = readtable('SIRTA_long term_2015_Max Planck_complete_vf02.xlsx', 'Sheet', 2, 'VariableNamingRule', 'preserve');
pmsoanames=pmsoatable.Properties.VariableNames
pmsoanames(1)=[]
gstringArray=string(pmsoanames)
bar(Totalpmsoa)
xticklabels(gstringArray)
set(gca,'xtick',1:25,'FontWeight', 'bold');
ylabel('Concentration (ng/m^3)')
%% gas SOA markers
gas_SOA_markers=xlsread('SIRTA_long term_2015_Max Planck_complete_vf02.xlsx','gas_SOA_markers')
gas_SOA_markers(isnan(gas_SOA_markers))=0
Totalgassoa=sum(gas_SOA_markers)
gassoatable = readtable('SIRTA_long term_2015_Max Planck_complete_vf02.xlsx', 'Sheet', 3, 'VariableNamingRule', 'preserve');
gassoanames=gassoatable.Properties.VariableNames
gassoanames(1)=[]
gasgstringArray=string(gassoanames)
bar(Totalgassoa)
xticklabels(gasgstringArray)
set(gca,'xtick',1:25,'FontWeight', 'bold');
ylabel('Concentration (ng/m^3)')
%% SIA in PM10
no3=data(:,11)
so42=data(:,12)
nh4=data(:,14)
pm10=data(:,2)
plot(no3+so42+nh4)
hold on
plot(pm10)
hold off
legend('no3+so42','pm10')
%% BC 
BC=data(:,5)
