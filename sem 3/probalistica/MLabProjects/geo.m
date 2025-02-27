clear all
clc

S=input("the number of simulations=");
p=input("probability of success=");

X=zeros(1,S);

for i=1:S
    %%the i-th simulation
    nofailures=0;
    while rand>=p
        nofailures=nofailures+1;
    end
    X(i)=nofailures;
end

U_X=unique(X);
n_X=hist(X,length(U_X));
rel_freq=n_X/S;

%[U_X;rel_freq]

plot(U_X,rel_freq,'x');
hold on;
plot(0:max(U_X),geopdf(0:max(U_X),p),'o');
hold off;
title('geo');
legend("sim","theoretical");