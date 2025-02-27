X = [20, 20, 21, 22*ones(1,3), 23*ones(1,6), 24*ones(1,5), 25*ones(1,9), 26, 26, 27, 27];
Y = [75*ones(1,3), 76, 76, 77, 77, 78*ones(1,5), 79*ones(1,8), 80*ones(1,8), 81, 82];

fprintf('mean X = %f\n', mean(X));
fprintf('mean Y = %f\n', mean(Y));
fprintf('var X = %f\n', var(X,1));
fprintf('var Y = %f\n', var(Y,1));
fprintf('std X= %f\n', sqrt(var(Y,1)));
fprintf('std Y = %f\n', sqrt(var(Y,1)));