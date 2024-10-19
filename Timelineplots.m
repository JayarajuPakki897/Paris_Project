%% Gas Phase PAHs 
gas_pah=SIRTAlongterm2015MaxPlanckcompletevf02S1
gas_pah{:,:};
GPPMatrix=gas_pah;
GPPMatrix=GPPMatrix{:,:};
GPPMatrix(isnan(GPPMatrix)) = 0;
GPP_sums = sum(GPPMatrix, 2);
Total_GPP=sum(GPPMatrix, 1)
%time=SIRTAlongterm2015MaxPlanckcompletevf02S5
%stackedplot(time,GPP_sums)
plot(GPP_sums)
gppnames=gas_pah.Properties.VariableNames
gstringArray=string(gppnames)
bar(Total_GPP)
xticklabels(gstringArray)
ylabel('Concentration (ng/m^3)')
set(gca,'xtick',1:22,'FontWeight', 'bold');
title('Gas Phase PAHs')

plot(GPP_sums)
time=SIRTAlongterm2015MaxPlanckcompletevf02S5
tc=table2cell(time)
dateStrings = cellfun(@datestr, tc, 'UniformOutput', false)
datetimeValue = datetime(dateStrings, 'InputFormat', 'dd-MMM-yyyy HH:mm:ss')
dateOnly = datestr(datetimeValue, 'yyyy-mm-dd');
xticklabels(dateOnly)
ylabel('Concentration (ng/m^3)')
title('Gas Phase PAHs')
set(gca,'xtick',1:127,'FontSize', 7,'FontWeight', 'bold');
%% Particle Phase PAHs 
par_pah=SIRTAlongterm2015MaxPlanckcompletevf02S7
par_pah{:,:};
PPPMatrix=table2array(par_pah);
PPPMatrix(isnan(PPPMatrix)) =0;
PPP_sums = sum(PPPMatrix, 2);
Total_PPP=sum(PPPMatrix, 1)
pppnames=par_pah.Properties.VariableNames
pstringArray=string(pppnames)

bar(Total_PPP)
title('Particle Phase PAHs')
xticklabels(pstringArray)
ylabel('Concentration (ng/m^3)')
set(gca,'xtick',1:58,'FontWeight', 'bold');

% yyaxis left
% plot(GPP_sums)
% yyaxis right
plot(PPP_sums)
tc=table2cell(time)
dateStrings = cellfun(@datestr, tc, 'UniformOutput', false)
datetimeValue = datetime(dateStrings, 'InputFormat', 'dd-MMM-yyyy HH:mm:ss')
dateOnly = datestr(datetimeValue, 'yyyy-mm-dd');
xticklabels(dateOnly)
ylabel('Concentration (ng/m^3)')
set(gca,'xtick',1:127,'FontSize', 7,'FontWeight', 'bold');
title('Particle Phase PAHs')

yyaxis left
plot(GPP_sums)
ylabel ('GPP (ng/m^3)')
yyaxis right
plot(PPP_sums)
xlabel('Time')
ylabel ('PPP (ng/m^3)')
xticklabels(dateOnly)
set(gca,'xtick',1:127,'FontSize', 7,'FontWeight', 'bold');
xlim([1,length(dateOnly)])

PM10_data=SIRTAlongterm2015MaxPlanckcompletevf02
% PM10_data(1,:)=[]
PM10_data(isnan(PM10_data)) =0;
plot(PM10_data./1000)
% plot(PM10_data)
xticklabels(dateOnly)
set(gca,'xtick',1:127,'FontSize', 7,'FontWeight', 'bold');
ylabel ('PM10 (μg/m^3)')
xlim([1,length(dateOnly)])
