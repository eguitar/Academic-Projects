function [APP] = adaptSimpsonInt_20091235(f, a, b, TOL, N)
    APP = 0;
    i = 1;

    temp = TOL;
    A = a;
    
    TOL = zeros(N,1);
    a = zeros(N,1);
    h = zeros(N,1);
    FA = zeros(N,1);
    FC = zeros(N,1);
    FB = zeros(N,1);
    S = zeros(N,1);
    L = zeros(N,1);

    TOL(1) = 10*temp;
    a(1) = A;
    h(1) = (b - a(1))/2;
    FA(1) = f(a(1));
    FC(1) = f(a(1) + h(1));
    FB(1) = f(b);
    S(1) = h(1)*(FA(1)+4*FC(1)+FB(1))/3;
    L(1) = 1;

    while (i > 0)
        FD = f(a(i) + h(i)/2);
        FE = f(a(i) + 3*h(i)/2);
        S1 = h(i)*(FA(i) + 4*FD + FC(i))/6;
        S2 = h(i)*(FC(i) + 4*FE + FB(i))/6;
        v1 = a(i);
        v2 = FA(i);
        v3 = FC(i);
        v4 = FB(i);
        v5 = h(i);
        v6 = TOL(i);
        v7 = S(i);
        v8 = L(i);
        
        i = i - 1;
        
        if abs(S1 + S2 - v7) < v6
            APP = APP + (S1 + S2);
        else
            if  v8 >= N
                disp('LEVEL EXCEEDED')
                return
            else
                i = i + 1;
                a(i) = v1 + v5;
                FA(i) = v3;
                FC(i) = FE;
                FB(i) = v4;
                h(i) = v5/2;
                TOL(i) = v6/2;
                S(i) = S2;
                L(i) = v8 + 1;

                i = i + 1;
                a(i) = v1;
                FA(i) = v2;
                FC(i) = FD;
                FB(i) = v3;
                h(i) = h(i - 1);
                TOL(i) = TOL(i - 1);
                S(i) = S1;
                L(i) = L(i - 1);
            end
        end
    end
end