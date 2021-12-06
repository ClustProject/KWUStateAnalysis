%% Statistical Analysis of Dispersion Entropy
% Wilcox
for i=1:scale
    pAF_CHF(i)  = ranksum(mdeAF(:,i), mdeCHF(:,i)); 
    pCHF_HT(i) = ranksum(mdeCHF(:,i), mdeHEALTHY(:,i));   
    pAF_HT(i) = ranksum(mdeAF(:,i), mdeHEALTHY(:,i));
end

significant = find(pAF_CHF < 0.05 & pAF_HT <0.05 & pCHF_HT < 0.05);
x=1:scale;
figure
errorbar(x,avg_mde_chf,err_mde_chf,'o-','MarkerSize',7, 'MarkerEdgeColor','blue')
hold
errorbar(x,avg_mde_af,err_mde_af, '-s','MarkerSize',8, 'MarkerEdgeColor','red')
errorbar(x,avg_mde_healthy, err_mde_healthy,'-d','MarkerSize',7, 'MarkerEdgeColor','black')

% title('MDE - CHF / AF/ Healthy, (m:3, c:6)');
title('MDE of RR Interval data constituted with N=1000');
xlabel('Scale factor')
ylabel('Value')

hold on
plot(significant,err_mde_chf(significant)+avg_mde_chf(significant)+0.7,'*k')
legend('CHF patients','AF patients','HEALHTY group', 'Location', 'northeast')

%% Statistical Analysis of Cumulative Residual Dispersion Entropy
% Wilcox
for i=1:scale
    pAF_CHF(i)  = ranksum(mcrdeAF(:,i), mcrdeCHF(:,i)); 
    pCHF_HT(i) = ranksum(mcrdeCHF(:,i), mcrdeHEALTHY(:,i));   
    pAF_HT(i) = ranksum(mcrdeAF(:,i), mcrdeHEALTHY(:,i));
end
significant = find(pAF_CHF < 0.05 & pAF_HT <0.05 & pCHF_HT < 0.05);
x=1:scale;
figure
errorbar(x,avg_mcrde_chf,err_mcrde_chf,'o-','MarkerSize',7, 'MarkerEdgeColor','blue')
hold
errorbar(x,avg_mcrde_af,err_mcrde_af, '-s','MarkerSize',8, 'MarkerEdgeColor','red')
errorbar(x,avg_mcrde_healthy, err_mcrde_healthy,'-d','MarkerSize',7, 'MarkerEdgeColor','black')

% title('MCRDE - CHF / AF/ Healthy, (m:3, c:6)');
title('MCRDE of RR Interval data constituted with N=1000');
xlabel('Scale factor')
ylabel('Value')
hold on
plot(significant,err_mcrde_chf(significant)+avg_mcrde_chf(significant)+0.7,'*k')
legend('CHF patients','AF patients','HEALHTY group', 'Location', 'southwest')

%% Statistical Analysis of Sample Entropy
% Wilcox
for i=1:scale
    pAF_CHF(i)  = ranksum(mseAF(:,i), mseCHF(:,i)); 
    pCHF_HT(i) = ranksum(mseCHF(:,i), mseHEALTHY(:,i));   
    pAF_HT(i) = ranksum(mseAF(:,i), mseHEALTHY(:,i));
end
significant = find(pAF_CHF < 0.05 & pAF_HT <0.05 & pCHF_HT < 0.05);
x=1:scale;
figure
errorbar(x,avg_mse_chf,err_mse_chf,'o-','MarkerSize',7, 'MarkerEdgeColor','blue')
hold
errorbar(x,avg_mse_af,err_mse_af, '-s','MarkerSize',8, 'MarkerEdgeColor','red')
errorbar(x,avg_mse_healthy, err_mse_healthy,'-d','MarkerSize',7, 'MarkerEdgeColor','black')

% title('MSE - CHF /  AF/ Healthy, (Embed Dim : 2, Threshold : 0.03)');
title('MSE of RR Interval data constituted with N=1000');
xlabel('Scale factor')
ylabel('Value')
hold on
plot(significant,err_mse_chf(significant)+avg_mse_chf(significant)+0.9,'*k')
legend('CHF patients','AF patients','HEALHTY group', 'Location', 'northeast')

%% Statistical Analysis of Sample Entropy
% % Wilcox
% for i=1:scale
%     pAF_CHF(i)  = ranksum(mpeAF(:,i), mpeCHF(:,i)); 
%     pCHF_HT(i) = ranksum(mpeCHF(:,i), mpeHEALTHY(:,i));   
%     pAF_HT(i) = ranksum(mpeAF(:,i), mpeHEALTHY(:,i));
% end
% significant = find(pAF_CHF < 0.05 & pAF_HT <0.05 & pCHF_HT < 0.05);
% x=1:scale;
% figure
% errorbar(x,avg_mpe_chf,err_mpe_chf,'o-','MarkerSize',7, 'MarkerEdgeColor','blue')
% hold
% errorbar(x,avg_mpe_af,err_mpe_af, '-s','MarkerSize',8, 'MarkerEdgeColor','red')
% errorbar(x,avg_mpe_healthy, err_mpe_healthy,'-d','MarkerSize',7, 'MarkerEdgeColor','black')
% 
% % title('MPE - CHF /  AF/ Healthy, (Embed Dim : 3, tau : 1)');
% title('MPE of RR Interval data constituted with N=1000');
% xlabel('Scale factor')
% ylabel('Value')
% hold on
% plot(significant,err_mpe_chf(significant)+avg_mpe_chf(significant)+0.7,'*k')
% legend('CHF patients','AF patients','HEALHTY group', 'Location', 'northeast')
