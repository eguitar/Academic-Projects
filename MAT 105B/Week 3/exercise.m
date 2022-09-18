clear;
clc;
close all;

f = @(x) (1/(1+x^2));
F = @(x) (-2*x/(1+x^2)^2);
FF = @(x)((6*x^2-2)/(x^2+1)^3);

f_list = zeros(4,1);
b_list = zeros(4,1);
c_list = zeros(4,1);

error_est = zeros(4,1);
error_list1 = zeros(4,1);
error_list2 = zeros(4,1);
error_list3 = zeros(4,1);

test = zeros(4,1);


%%
N = 11;
x = linspace(-5,5,N);

t1 = zeros(N-1,1);
t2 = zeros(N-1,1);
t3 = zeros(N-1,1);

f_yprime = forwardNumericalDeriv_20091235(f,x);
b_yprime = backwardNumericalDeriv_20091235(f,x);
c_yprime = centralNumericalDeriv_20091235(f,x);
yprime = zeros(N-1,1);

for i = 1:N-1
    yprime(i) = F(x(i));
end

error_est(1) = abs(FF(0)*5/(N));

for i = 1:N-1
    t1(i) = yprime(i) - f_yprime(i);
    t2(i) = yprime(i) - b_yprime(i);
    if i ~= N-1
        t3(i) = yprime(i+1) - c_yprime(i);
    end
end

error_list1(1) = max(abs(t1));
error_list2(1) = max(abs(t2));
error_list3(1) = max(abs(t3));
test(1) = 4.67*100/(N^2*6);
%%
N = 21;
x = linspace(-5,5,N);

t1 = zeros(N-1,1);
t2 = zeros(N-1,1);
t3 = zeros(N-1,1);

f_yprime = forwardNumericalDeriv_20091235(f,x);
b_yprime = backwardNumericalDeriv_20091235(f,x);
c_yprime = centralNumericalDeriv_20091235(f,x);
yprime = zeros(N-1,1);

for i = 1:N-1
    yprime(i) = F(x(i));
end

error_est(2) = abs(FF(0)*5/(N));

for i = 1:N-1
    t1(i) = yprime(i) - f_yprime(i);
    t2(i) = yprime(i) - b_yprime(i);
    if i ~= N-1
        t3(i) = yprime(i+1) - c_yprime(i);
    end
end

error_list1(2) = max(abs(t1));
error_list2(2) = max(abs(t2));
error_list3(2) = max(abs(t3));
test(2) = 4.67*100/(N^2*6);
%%
N = 51;
x = linspace(-5,5,N);

t1 = zeros(N-1,1);
t2 = zeros(N-1,1);
t3 = zeros(N-1,1);

f_yprime = forwardNumericalDeriv_20091235(f,x);
b_yprime = backwardNumericalDeriv_20091235(f,x);
c_yprime = centralNumericalDeriv_20091235(f,x);
yprime = zeros(N-1,1);

for i = 1:N-1
    yprime(i) = F(x(i));
end

error_est(3) = abs(FF(0)*5/(N));

for i = 1:N-1
    t1(i) = yprime(i) - f_yprime(i);
    t2(i) = yprime(i) - b_yprime(i);
    if i ~= N-1
        t3(i) = yprime(i+1) - c_yprime(i);
    end
end

error_list1(3) = max(abs(t1));
error_list2(3) = max(abs(t2));
error_list3(3) = max(abs(t3));
test(3) = 4.67*100/(N^2*6);
%%
N = 101;
x = linspace(-5,5,N);

t1 = zeros(N-1,1);
t2 = zeros(N-1,1);
t3 = zeros(N-1,1);

f_yprime = forwardNumericalDeriv_20091235(f,x);
b_yprime = backwardNumericalDeriv_20091235(f,x);
c_yprime = centralNumericalDeriv_20091235(f,x);
yprime = zeros(N-1,1);

for i = 1:N-1
    yprime(i) = F(x(i));
end

error_est(4) = abs(FF(0)*5/(N));

for i = 1:N-1
    t1(i) = yprime(i) - f_yprime(i);
    t2(i) = yprime(i) - b_yprime(i);
    if i ~= N-1
        t3(i) = yprime(i+1) - c_yprime(i);
    end
end

error_list1(4) = max(abs(t1));
error_list2(4) = max(abs(t2));
error_list3(4) = max(abs(t3));
test(4) = 4.67*100/(N^2*6);



figure(1)
plot([11 21 51 101],error_est)
hold on
plot([11 21 51 101],error_list1)
% hold on
plot([11 21 51 101],error_list2)
plot([11 21 51 101],error_list3)
plot([11 21 51 101],test)