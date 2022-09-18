function [A] = chebyPolyAppx_20091235(f, N, TOL, intTOL, depth)
A = zeros(N+1,1);
for i = 1:N+1
    if i == 1
        fun = @(x) (f(x)*power(1-x*x,-1/2));
        A(i) = adaptSimpsonInt_20091235(fun,-1+TOL,1-TOL,intTOL,depth);
        A(i) = A(i) / pi;
    else
        fun = @(x) (f(x)*(cos((i-1)*acos(x)))*power(1-x*x,-1/2));
        A(i) = adaptSimpsonInt_20091235(fun,-1+TOL,1-TOL,intTOL,depth);
        A(i) = 2 * A(i) / pi;
    end
end
end