#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct Car
{
    unsigned id;
    double miles;
};


int contains_car(unsigned i, struct Car *c, unsigned n)
{
    for (unsigned k = 0; k < n; ++k)
    {
        if ((*c).id == i)
            return 1;
        c++;
    }
    return 0;
}


void add_car(unsigned i, struct Car *c, unsigned *n)
{
    
    if (contains_car(i,c,*n))
    {
        printf("Error! Car with ID %u already exists in the database.\n", i);
        return;
    }
    if (*n == 10)
    {
        printf("Error! Max number of cars stored in the database.\n");
        return;
    }
    for (unsigned k = 0; k < *n; ++k)
    {
        c++;
    }
    
    c->id = i;
    c->miles = 0;

    (*n)++;
    return;
}


void add_trip(unsigned i, double mi, struct Car *c, unsigned n)
{
    if (!(contains_car(i,c,n)))
    {
        printf("Error! Car with ID %u does not exist in the database.\n", i);
        return;
    }
    for (unsigned k = 0; k < n; ++k)
    {
        if ((*c).id == i)
        {
            (*c).miles += mi;
            return;
        }
        c++;
    }
}


void reset_car(unsigned i, struct Car *c, unsigned n)
{
    for (unsigned k = 0; k < n; ++k)
    {
        if ((*c).id == i)
        {
            (*c).miles = 0.0;
            return;
        }
        c++;
    }
    printf("Error! Car with ID %u does not exist in the database.\n", i);
}


void print_cars(struct Car *c, unsigned n)
{
    for (unsigned i = 0; i < n; ++i)
    {
        printf("%u",(*c).id);
        printf("\t");
        printf("%f",(*c).miles);
        printf("\n");
        c++;
    }
    return;
}


int main()
{
    struct Car data[10];     // array of struct car
    unsigned size = 0;       // number of cars
    char input[256];         // repeating input

    char *command;           // parsed command
    char *val1;              // variable 1
    char *val2;              // variable 2

    unsigned num1;           // variable 1
    double num2;              // variable 2
    
    while (1)
    {
        printf("> ");
        fgets(input,256,stdin);
        command = strtok(input," ");

        if (!(strcmp(input,"quit\n")))           // quit
            break;
        else if (!strcmp(command, "AddCar"))                               // add car
        {
            val1 = strtok(NULL," ");
            num1 = atoi(val1);

            add_car(num1,data,&size);
        }
        else if (!strcmp(command, "AddTrip"))                               // add trip
        {
            val1 = strtok(NULL," ");
            num1 = atoi(val1);
            
            val2 = strtok(NULL," ");
            num2 = atof(val2);

            add_trip(num1,num2,data,size);
        }
        else if (!strcmp(command, "Reset"))                               // reset car
        {
            val1 = strtok(NULL," ");
            num1 = atoi(val1);
            
            reset_car(num1,data,size);
        }
        else if (!strcmp(input, "Display\n"))                               // display cars
        {
            print_cars(data, size);
        }
        // else
        // {
        //     printf("HELP! USER INPUT ERROR\n");
        // }
    }
    return 0;
}