clear all
clc

S=input("the number of simulations=");
p=input("probability of success=");

U=rand(1,S);
X=U<p;

U_X=unique(X);
n_X=hist(X,length(U_X));
rel_freq=n_X/S;

[U_X;rel_freq]