clear all
clc

n=3;

k=0:n;
p=0.5;
px=binopdf(k,n,p);
D=[k;px]

kreal=0:0.01:n;
fx=binocdf(kreal,n,p);

plot(k,px,'*');
hold on;
plot(kreal,fx);
hold off;
title("the binomial model");
legend("pdf", "cdf");