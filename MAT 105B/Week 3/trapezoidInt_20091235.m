%% Eric Trinh (20091235)
function [XI] = trapezoidInt_20091235(f, a, b, n)
    h = (b - a)/n;  
    temp = 0;
    for i = 1:n-1
        X = a + (i*h);
        temp = temp + f(X); 
    end
    XI = h*(f(a)+f(b)+2*temp)/2;
end