clear all
clc

alpha=input("alpha=");
beta=input("beta=");
option = input("Enter the model name (Normal, Student, Chi2, Fisher): ",'s');
switch option
    case 'Normal'
        fprintf("Normal distribution model\n")
        mu=input("mu=");
        sigma=input("sigma=");
        fprintf("a)\nP(X<=0)=%f\n", normcdf(0,mu,sigma));
        fprintf("P(X>=0)=%f\n", 1-normcdf(0,mu,sigma));
        fprintf("b)\nP(-1<=X<=1)=%f\n", normcdf(1,mu,sigma)-normcdf(-1,mu,sigma));
        fprintf("P(X<=-1 or X>=1)=%f\n", 1-(normcdf(1,mu,sigma)-normcdf(-1,mu,sigma)));
        fprintf("c)\nP(X<xalpha)=%f\n", norminv(alpha,mu,sigma));
        fprintf("d)\nP(X>xbeta)=%f\n", norminv(1-beta,mu,sigma));

    case 'Student'
        fprintf("Student (T) distribution model\n")
        n=input("n=");
        fprintf("a)\nP(X<=0)=%f\n", tcdf(0,n));
        fprintf("P(X<=0)=%f\n", 1-tcdf(0,n));
        fprintf("b)\nP(-1<=X<=1)=%f\n", tcdf(1,n) - tcdf(-1,n));
        fprintf("P(X<=-1 or X>=1)=%f\n", 1-(tcdf(1,n) - tcdf(-1,n)));
        fprintf("c)\nP(X<xalpha)=%f\n", tinv(alpha,0,n));

    case 'Chi2'
        fprintf("Chi2 distribution model\n")
        n=input("n=");
        fprintf("a)\nP(X<=0)=%f\n", chi2cdf(0,n));
        fprintf("P(X<=0)=%f\n", 1-chi2cdf(0,n));
        fprintf("b)\nP(-1<=X<=1)=%f\n", chi2cdf(1,n) - chi2cdf(-1,n));
        fprintf("P(X<=-1 or X>=1)=%f\n", 1-(chi2cdf(1,n) - chi2cdf(-1,n)));
        fprintf("c)\nP(X<xalpha)=%f\n", chi2inv(alpha,0,n));

    case 'Fisher'
        fprintf("Fisher distribution model\n")
        m=input("m=");
        n=input("n=");
        fprintf("a)\nP(X<=0)=%f\n", fcdf(0,n,m));
        fprintf("P(X<=0)=%f\n", 1-fcdf(0,n,m));
        fprintf("b)\nP(-1<=X<=1)=%f\n", fcdf(1,n,m) - fcdf(-1,n,m));
        fprintf("P(X<=-1 or X>=1)=%f\n", 1-(fcdf(1,n,m) - fcdf(-1,n,m)));
        fprintf("c)\nP(X<xalpha)=%f\n", finv(alpha,0,n,m));

    otherwise
        fprintf("Wrong option\n")
end