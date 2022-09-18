%% Eric Trinh (20091235)
function [YPrime] = backwardNumericalDeriv_20091235(f, X)
    n = length(X);
    YPrime = zeros(n - 1,1);
    for i = 1:n-1
        YPrime(i) = (f(X(i+1)) - f(X(i))) / (X(i+1) - X(i));
    end
end