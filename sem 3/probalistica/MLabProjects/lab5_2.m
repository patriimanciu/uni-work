X = [7,7,4,5,9,9,4,12,8,1,8,7,3,13,2,1,17,7,12,5,6,2,1,13,14,10,2,4,9,11,3,5,12,6,10,7];

clev = input("Confidence level: ");
alpha = 1-clev;
meanX = mean(X);
sigma = 5;
n = length(X);
z1 = norminv(1-alpha/2,0,1);
z2 = norminv(alpha/2,0,1);
thetaL = meanX - (sigma/sqrt(n))*z1
thetaU = meanX - (sigma/sqrt(n))*z2