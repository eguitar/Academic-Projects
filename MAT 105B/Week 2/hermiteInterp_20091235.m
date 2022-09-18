%% Eric Trinh (20091235)
function [Q] = hermiteInterp_20091235(X, Y, YPrime)
    n = length(X) - 1;
    z = zeros(2*n+1,1);
    Q = zeros(2*n+1);
    for i = 0:n
        z(2*i+1) = X(i+1);
        z(2*i+2) = X(i+1);
        Q(2*i+1,1) = Y(i+1);
        Q(2*i+2,1) = Y(i+1);
        Q(2*i+2,2) = YPrime(i+1);
        if i ~= 0
            Q(2*i+1,2) = (Q(2*i+1,1)-Q(2*i,1))/(z(2*i+1)-z(2*i));
        end
    end
    for i = 2:2*n+1
        for j = 2:i
            Q(i+1,j+1) = (Q(i+1,j)-Q(i,j))/(z(i+1)-z(i-j+1));
        end
    end
    Q = diag(Q);
end



