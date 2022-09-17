// Brennen Wong, brennew, 63218897
// Eric Trinh, edtrinh, 20091235

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>

struct Memory 
{
	int address, data;
};

struct PageTable 
{
	int v_page_num, valid_bit, dirty_bit, page_num, time_stamp;
};

struct Memory main_memory[32];
struct Memory virtual_memory[128];
struct PageTable p_table[16];
int fifo = 0, lru = 0;
int page_index = 0;


void initialize()
{
    extern struct Memory main_memory[32];
    extern struct Memory virtual_memory[128];
    extern struct PageTable p_table[16];

	int i;
    for (i = 0; i < sizeof(main_memory)/sizeof(main_memory[0]); i++)
	{
        main_memory[i].data = -1;
        main_memory[i].address = i;
	}

	for (i = 0; i < sizeof(virtual_memory)/sizeof(virtual_memory[0]); i++) 
	{
        virtual_memory[i].data = -1;
        virtual_memory[i].address = i;
	}

	for (i = 0; i < sizeof(p_table)/sizeof(p_table[0]); i++) 
	{
        p_table[i].v_page_num = p_table[i].page_num = i;
        p_table[i].valid_bit = p_table[i].dirty_bit = 0;
        p_table[i].time_stamp = 0;
	}
}


void parseline(char* input, char** args)
{
    const char* delim = "\t\n ";
    char* token = strtok(input,delim);
    unsigned i = 0;
    while(token != NULL)
    {
        args[i] = token;
        token = strtok(NULL, delim);
        i++;
    }
}


void increment_time()
{
    extern struct PageTable p_table[16];
	int i;
	for (i = 0; i < sizeof(p_table)/sizeof(p_table[0]); i++) 
		if (p_table[i].valid_bit == 1)
			p_table[i].time_stamp++;
}


int is_full()
{
    extern struct PageTable p_table[16];
    int count = 0;
	int i;
	for (i = 0; i < 16; ++i)
		if (p_table[i].valid_bit == 1)
			count++;

	if (count >= 4)
		return 1;
	else
		return 0;
}


int get_virtual_index(int address)
{
    return (int) address / 8;
}


// int get_first_index()
// {
// 	extern struct PageTable p_table[16];
	
// 	int max_index, i;
// 	int max_time = 0;
// 	for (i = 0; i < 16; i++)
// 		if (p_table[i].valid_bit == 1)
// 			if (p_table[i].time_stamp > max_time)
// 			{
// 				max_index = i;
// 				max_time = p_table[i].time_stamp;
// 			}
// 	return max_index;
// }


int get_max_index()
{
	extern struct PageTable p_table[16];
	
	int max_index, i;
	int max_time = 0;
	for (i = 0; i < 16; i++)
		if (p_table[i].valid_bit == 1)
			if (p_table[i].time_stamp > max_time)
			{
				max_index = i;
				max_time = p_table[i].time_stamp;
			}
	return max_index;
}


void return_virtual(int main_start, int virtual_start)
{
    int j;
    for (j = 0; j < 8; ++j)
    {
        virtual_memory[virtual_start + j].address = main_memory[main_start + j].address;
        virtual_memory[virtual_start + j].data = main_memory[main_start + j].data;
    }
}


// ######################################################################
void loop()
{
    char input[100];
	char* args[3];

	extern struct Memory main_memory[32];
	extern struct Memory virtual_memory[128];
	extern struct PageTable p_table[16];
    extern int page_index;
    extern int fifo,lru;

    int main_add;          // index of main_mem
    int virtual_add;       // index of virtual_mem
    int start_add;         // start index of virtual_mem

    int main_index;        // page index of main_mem
    int virtual_index;     // index of p_table

    int temp_index;        // use of overwriting
    int num;               // set value

    while (1)
    {
        printf("> ");
		fgets(input, 80, stdin);
        parseline(input, args);

        if (strcmp(args[0], "quit") == 0)
        {
            break;
        }
        else if (strcmp(args[0], "read") == 0)
		{
            virtual_add = atoi(args[1]);
            virtual_index = get_virtual_index(virtual_add); 

            if (p_table[virtual_index].valid_bit == 0)
            {
                printf("A Page Fault Has Occurred\n");

                if (is_full() && (fifo == 1 || lru == 1))
                {
                    temp_index = get_max_index();
					page_index = p_table[temp_index].page_num;

					return_virtual(page_index * 8, main_memory[page_index * 8].address);

					p_table[temp_index].valid_bit = 0;
                    p_table[temp_index].dirty_bit = 0;
					p_table[temp_index].time_stamp = 0;
					p_table[temp_index].page_num = temp_index;
                }
                
                p_table[virtual_index].valid_bit = 1;
                p_table[virtual_index].page_num = page_index;

                main_index = p_table[virtual_index].page_num;
                main_add = (main_index * 8);
                start_add = ((int) virtual_add / 8) * 8;  

                int j;
                int a = main_add, b = start_add;
                for (j = 0; j < 8; ++j)
                {
                    main_memory[a + j].address = virtual_memory[b + j].address;
                    main_memory[a + j].data = virtual_memory[b + j].data;
                }
                page_index++;
            }
            
            main_index = p_table[virtual_index].page_num;
            main_add = (main_index * 8) + (virtual_add % 8);
            printf("%d\n", main_memory[main_add].data);
            
            if (lru == 1)
		        p_table[virtual_index].time_stamp = 0;
        }
        else if (strcmp(args[0], "write") == 0)
		{
            virtual_add = atoi(args[1]);
            virtual_index = get_virtual_index(virtual_add); 

            if (p_table[virtual_index].valid_bit == 0)
            {
                printf("A Page Fault Has Occurred\n");

                if (is_full() && (fifo == 1 || lru == 1))
                {
                    temp_index = get_max_index();
					page_index = p_table[temp_index].page_num;

                    return_virtual(page_index * 8, main_memory[page_index * 8].address);

					p_table[temp_index].valid_bit = 0;
                    p_table[temp_index].dirty_bit = 0;
					p_table[temp_index].time_stamp = 0;
					p_table[temp_index].page_num = temp_index;
                }
                
                p_table[virtual_index].valid_bit = 1;
                p_table[virtual_index].dirty_bit = 1;
                p_table[virtual_index].page_num = page_index;

                main_index = p_table[virtual_index].page_num;
                main_add = (main_index * 8);
                start_add = ((int) virtual_add / 8) * 8;

                int j;
                int a = main_add, b = start_add;
                for (j = 0; j < 8; ++j)
                {
                    main_memory[a + j].address = virtual_memory[b + j].address;
                    main_memory[a + j].data = virtual_memory[b + j].data;
                }
                page_index++;
            }

            p_table[virtual_index].dirty_bit = 1;
            main_index = p_table[virtual_index].page_num;
            main_add = (main_index * 8) + (virtual_add % 8);
            num = atoi(args[2]);
            main_memory[main_add].data = num;

            if (lru == 1)
		        p_table[virtual_index].time_stamp = 0;
        }
		else if (strcmp(args[0], "showmain") == 0)
		{
            int i;
			for (i = atoi(args[1]) * 8; i < (atoi(args[1]) + 1) * 8; i++)
			{
				printf("%d: ", i);
				printf("%d\n", main_memory[i].data);
			}
        }
        else if (strcmp(args[0], "showptable") == 0)
		{
            int i;
			for (i = 0; i < 16; i++)
			{
				printf("%d:", p_table[i].v_page_num);
				printf("%d:", p_table[i].valid_bit);
				printf("%d:", p_table[i].dirty_bit);
				printf("%d\n", p_table[i].page_num);
			}
        }
        
		increment_time();
    }
}

int main(int argc, char** argv)
{
    extern int fifo;
	extern int lru;

	if (argv[1] == NULL || strcmp (argv[1], "FIFO") == 0)
		fifo = 1;
	else if (strcmp (argv[1], "LRU") == 0)
		lru = 1;
	initialize();
	loop();
	return 0;
}