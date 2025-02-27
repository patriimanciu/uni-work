clear all
clc

S=input("the number of simulations=");
p=input("probability of success=");
n=input("the number of successes=");

X=zeros(1,S);

for i=1:S
    %%the i-th simulation
    nofailures=0;
    nosuccesses=0;
    while rand>=p
        nofailures=nofailures+1;
    end
    X(i)=nofailures;
end
%%binostat
U_X=unique(X);
n_X=hist(X,length(U_X));
rel_freq=n_X/S;

%[U_X;rel_freq]

plot(U_X,rel_freq,'x');
hold on;
plot(0:max(U_X),nbinpdf(0:max(U_X),n,p),'o');
hold off;
title('pascal');
legend("sim","theoretical");