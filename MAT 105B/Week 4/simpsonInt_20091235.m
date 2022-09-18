%% Eric Trinh (20091235)
function [XI] = simpsonInt_20091235(f, a, b, n)
    h = (b - a)/n;
    XI1 = 0;
    XI2 = 0;
    for i = 1:n-1
        X = a + (i*h);
        if rem(i,2) == 0
            XI2 = XI2 + f(X);
        else
            XI1 = XI1 + f(X);
        end 
    end
    XI = h*(f(a)+f(b)+2*XI2+4*XI1)/3;
end