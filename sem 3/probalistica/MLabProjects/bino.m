clear all
clc

S=input("the number of simulations=");
n=input("the number of trials=");
p=input("probability of success=");

U=rand(n,S);
X=sum(U<p);

U_X=unique(X);
n_X=hist(X,length(U_X));
rel_freq=n_X/S;

%[U_X;rel_freq]

plot(U_X,rel_freq,'x');
hold on;
plot(0:n,binopdf(0:n,n,p),'o');
hold off;
title('bino');
legend("sim","theoretical");