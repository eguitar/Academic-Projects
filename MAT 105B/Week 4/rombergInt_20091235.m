function [Rout] = rombergInt_20091235(f, a, b, N)
    temp = zeros(N);
    Rout = zeros(N);
    h = b - a;
    temp(1,1) = (h/2)*(f(a) + f(b));
    Rout(1,:) = temp(1,:);
    for i = 2:N
        sum = 0;
        for k = 1:power(2,i-2)
            sum = sum + f(a + (k - 0.5)*h);
        end
        temp(2,1) = (1/2)*(temp(1,1) + h*sum);
        for j = 2:i
            temp(2,j) = temp(2,j-1) + ((temp(2,j-1)-temp(1,j-1))/(power(4,j-1)-1));
        end
        Rout(i,:) = temp(2,:);
        h = h/2;
        for j = 1:i 
            temp(1,j) = temp(2,j);
        end
    end
end