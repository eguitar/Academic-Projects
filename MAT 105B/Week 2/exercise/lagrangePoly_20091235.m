%% Eric Trinh (20091235)
function [z] = lagrangePoly_20091235(X, Y, p)
    z = 0;
    n = length(X);
    for k = 1:n
        temp = 1;
        for i = 1:n
            if i == k
                continue;
            end
            temp = temp * ((p - X(i))/(X(k) - X(i)));
        end   
        z = z + (Y(k)*temp);    
    end
end