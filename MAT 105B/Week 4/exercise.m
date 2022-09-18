f = @(x) (cos(2*x).*exp(-x));

APP = adaptSimpsonInt_20091235(f, 0, 2*pi, 0.5e-4, 2)
APP = adaptSimpsonInt_20091235(f, 0, 2*pi, 0.5e-4, 3)
APP = adaptSimpsonInt_20091235(f, 0, 2*pi, 0.5e-4, 4)
APP = adaptSimpsonInt_20091235(f, 0, 2*pi, 0.5e-4, 5)
APP = adaptSimpsonInt_20091235(f, 0, 2*pi, 0.5e-4, 6)

result = integral(f,0,2*pi);

i = 1;
while (1)

    if abs(result - simpsonInt_20091235(f,0,2*pi,i)) < 0.5e-4
        disp(i)
        disp("---------------")
        index = i;
        break
    end
   
    i = i + 1;

end

