clc;clear;

data = [302    45
   325    72
   285    54
   304    62
   334    79
   322    65
   331    99
   279    63
   316    65
   347    99
   343    83
   290    74
   326    76
   233    57
   254    45
   323    83
   337    99
   337    70
   339    54
   319    66
   234    51
   337    53
   351   100
   339    67
   343    83
   314    42
   344    79
   185    59
   340    75
   316    45];


x = data(:,1);
y = data(:,2);

plot(x,y, '.')
hold on

a = leastSqrs_20091235(x,y);

f = @(x) (a(1) + x*a(2));

xmin = min(x);
xmax = max(x);

plot([xmin xmax],[f(xmin) f(xmax)],'-')

disp((90-a(1))/a(2))
disp((60-a(1))/a(2))
