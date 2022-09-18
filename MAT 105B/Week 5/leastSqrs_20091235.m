function [a] = leastSqrs_20091235(x, y)
a = zeros(1,2);
m = length(x);
x2_sum = 0;
y_sum = 0;
xy_sum = 0;
x_sum = 0;
for i = 1:m
    x2_sum = x2_sum + (x(i)*x(i));
    y_sum = y_sum + y(i);
    xy_sum = xy_sum + (x(i)*y(i));
    x_sum = x_sum + x(i);
end
a(1) = (x2_sum*y_sum - xy_sum*x_sum)/(m*x2_sum - x_sum*x_sum);
a(2) = (m*xy_sum - x_sum*y_sum)/(m*x2_sum - x_sum*x_sum);
end