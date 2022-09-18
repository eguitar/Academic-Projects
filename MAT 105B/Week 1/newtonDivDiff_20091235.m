%% Eric Trinh (20091235)
function [F] = newtonDivDiff_20091235(X, Y)
    n = length(X);
    A = zeros(n);
    B = zeros(n);
    for i = 1:n
        A(i,1) = Y(i);
        B(i,1) = X(i);
    end
    for col = 2:n
        for row = col:n
            B(row,col) = (B(row,1)) - B(row-col+1,1);
        end
    end
    for col = 2:n
        for row = col:n
            A(row,col) = (A(row,col-1) - A(row-1,col-1))/B(row,col);
        end
    end
    F = diag(A);
end