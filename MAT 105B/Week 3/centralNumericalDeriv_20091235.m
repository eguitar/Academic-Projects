%% Eric Trinh (20091235)
function [YPrime] = centralNumericalDeriv_20091235(f, X)
    n = length(X);
    YPrime = zeros(n - 2,1);
    for i = 2:n-1
        YPrime(i-1) = (f(X(i+1)) - f(X(i-1))) / (X(i+1) - X(i-1));
    end
end