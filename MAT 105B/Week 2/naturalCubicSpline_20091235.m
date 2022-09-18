%% Eric Trinh (20091235)
function [a, b, c, d] = naturalCubicSpline_20091235(X, Y)
    n = length(X) - 1;
    h = zeros(n,1);
    a = Y;
    q = zeros(n+1,1);
    b = zeros(n+1,1);
    c = zeros(n+1,1);
    d = zeros(n+1,1);   
    l = zeros(n+1,1);
    u = zeros(n+1,1);
    z = zeros(n+1,1);
    for i = 0:n-1
        h(i+1) = X(i+2) - X(i+1);
    end
    for i = 1:n-1
        q(i+1) = (3/h(i+1))*(a(i+2)-a(i+1))-(3/h(i))*(a(i+1)-a(i));
    end
    l(1) = 1;
    u(1) = 0;
    z(1) = 0;
    for i = 1:n-1
        l(i+1) = 2*(X(i+2)-X(i))-(h(i)*u(i));
        u(i+1) = h(i+1)/l(i+1);
        z(i+1) = (q(i+1) - (h(i)*z(i)))/l(i+1);
    end
    l(n+1) = 1;
    z(n+1) = 0;
    c(n+1) = 0;
    for j = n-1:-1:0
        c(j+1) = z(j+1) - (u(j+1)*c(j+2));
        b(j+1) = ((a(j+2)-a(j+1))/h(j+1))-(h(j+1)*(c(j+2)+2*c(j+1))/3);
        d(j+1) = (c(j+2) - c(j+1))/(3*h(j+1));
    end
    a = a([1:n]);
    b = b([1:n]);
    c = c([1:n]);
    d = d([1:n]);
end