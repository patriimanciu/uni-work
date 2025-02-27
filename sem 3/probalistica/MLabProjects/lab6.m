clc
clear all

X = [7,7,4,5,9,9,4,12,8,1,8,7,3,13,2,1,17,7,12,5,6,2,1,13,14,10,2,4,9,11,3,5,12,6,10,7];

alpha = input("significance level = ");
% RR = norminv(alpha,0,1);
% 
% [H,P,CI,ZVAL] = ztest(X,8.5,5,alpha,-1)

% if H==1 
%     fprintf("The efficiency standard is not met");
% else
%     fprintf("The efficiency standard is met");
% end

RR1 = tinv(1-alpha, 35)

[H,P,CI,STATS] = ttest(X,5.5,alpha,1)

STATS.tstat