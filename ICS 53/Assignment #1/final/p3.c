#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main()
{
    char input[256];
    
    printf("> ");
    fgets(input,256,stdin);
    
    char string[252];
    unsigned n;
    
    for (unsigned i = 0; i < 256; ++i)
    {
        if (input[i] == ',')
        {
            string[i] = '\0';
            n = i + 1;
            break;
        }
        string[i] = input[i];
    }
    
    char num1[252];
    char num2[252];

    int a = 0;
    for (unsigned j = n; j < 256; ++j)
    {
        if (input[j] == ',')
        {
            n = j + 1;
            break;
        }
        if (isdigit(input[j]))
        {
            num1[a] = input[j];
            a++;
        }
    }
    
    int n1 = atoi(num1);
    
    a = 0;
    for (unsigned k = n; k< 256; ++k)
    {
        if (input[k] == '\0')
        {
            n = k + 1;
            break;
        }
        if (isdigit(input[k]))
        {
            num2[a] = input[k];
            a++;
        }
    }
    
    int n2 = atoi(num2);
    
    for (unsigned x = n1; x < n1 + n2; ++x)
    {
        if (string[x] == '\0')
            break;
        printf("%c",string[x]);
    }
    return 0;
}