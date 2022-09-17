#include <stdio.h>
#include <ctype.h>

struct Letter
{
    char c;
    unsigned count;
};


void sort_letters(struct Letter dict[], unsigned n)
{
    struct Letter temp;
    
    for (unsigned i = 0; i < n - 1; ++i)
    {
        for (unsigned j = i + 1; j < n; ++j)
        {
            if (dict[j].count < dict[i].count)
            {
                temp = dict[i];
                dict[i] = dict[j];
                dict[j] = temp;
            }   
        }
    }
}


void add_letter(char k, struct Letter *dict, unsigned *n)
{
    struct Letter *dict2 = dict;
    
    for (unsigned i = 0; i < *n; ++i)
    {
        if (dict->c == k)
        {
            dict->count++;
            return;
        }
        dict++;
    }
    
    for (unsigned i = 0; i < *n; ++i)
    {
        dict2++;
    }
    
    dict2->c = k;
    dict2->count = 1;
    
    (*n)++;
    return;
}


void print_diction(struct Letter dict[], unsigned n)
{
    for (unsigned i = 0; i < n; ++i)
    {
        printf("%c",dict[i].c);
        printf(": ");
        printf("%u\n",dict[i].count);
    }
}


void print_sort_string(char string[], unsigned n)
{
    char min, temp;
    unsigned x = 0;
    for (unsigned i = 0; i < n; ++i)
    {
        min = string[i];
        temp = string[i];
        x = i;
        for (unsigned j = i; j < n; ++j)
        {
            if (string[j] < min)
            {
                min = string[j];
                x = j;
            }
        }
        temp = string[i];
        string[i] = min;
        string[x] = temp;
    }
    
    for (unsigned k = 0; k < n; ++k)
        printf("%c",string[k]);
    printf("\n");
    return;
}


int main()
{
    char input[256];
    
    printf("> ");
    fgets(input,256,stdin);

    char string[256];
    unsigned j = 0;
    for (unsigned i = 0; i < 256; ++i)
    {
        if (input[i] == '\0')
            break;
        if (isalnum(input[i]))
        {
            string[j] = input[i];
            j++;
        }
    }
    string[j] = '\0';

    unsigned n = 0;
    while (1)
    {
        if (string[n] == '\0')
            break;
        n++;
    }

    struct Letter diction[n];
    unsigned size = 0;

    for (unsigned i = 0; i < n; ++i)
    {
        add_letter(string[i],diction,&size);
    }
    sort_letters(diction,size);
    print_diction(diction,size);
    print_sort_string(string,n);
    return 0;
}