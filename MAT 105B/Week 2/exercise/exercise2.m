close all;

data = [-2.4061 -0.3984
-1.0830 -0.7611
-0.6440 -0.9688
-0.4068 -0.9791
-0.2448 -0.7899
-0.1158 -0.4397
0 0
0.1158 0.4397
0.2448 0.7899
0.4068 0.9791
0.6440 0.9688
1.0830 0.7611
2.4061 0.3984];

n = length(data);

X = data(:,1);
Y = data(:,2);

x_output = linspace(-2,2,1000);
y_output = zeros(length(x_output),1);


for i = 1:length(x_output)
    y_output(i) = lagrangePoly_20091235(X,Y,x_output(i));
end

plot(x_output,y_output)
hold on

[a,b,c,d] = naturalCubicSpline_20091235(X,Y);

x_data = x_output;
y_data = zeros(length(x_data),1);
% disp(y_data)

for i = 1:length(y_data)
    
    j = 1;
    while true
        if x_data(i) < X(j)
%             disp('------------')
%             disp(x_data(i))
%             disp(X(j))
            j = j - 1;
            break;
        end
        j = j + 1;
    end
    y_data(i) = a(j) + b(j)*(x_data(i) - X(j)) + c(j)*((x_data(i) - X(j))^2) + d(j)*((x_data(i) - X(j))^3);

end

disp(x_data)
disp(y_data)

plot(x_data,y_data)
hold on

y_func = zeros(length(x_data),1);

for i = 1:length(x_data)
    y_func(i) = x_data(i) / ((1/4)+x_data(i)^2);
end

plot(x_data,y_func)

