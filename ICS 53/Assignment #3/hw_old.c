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


void tokenize(char* input, char** args)
{
	const char delim[] = "\t\n ";
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
	{
		if (p_table[i].valid_bit == 1)
		{
			p_table[i].time_stamp++;
		}
	}
}


int is_full()    // 0 is not full, 1 is full
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


int get_first_index()
{
	extern struct PageTable p_table[16];
	
	int max_index, i;
	int max_time = 0;
	for (i = 0; i < 16; i++)
	{
		if (p_table[i].valid_bit == 1)
		{
			if (p_table[i].time_stamp > max_time)
			{
				max_index = i;
				max_time = p_table[i].time_stamp;
			}
		}
	}
	
	return max_index;
}


int get_least_index()
{
	extern struct PageTable p_table[16];
	
	int min_index, i;
	int min_time = INT_MAX;
	for (i = 0; i < 16; i++)
	{
		if (p_table[i].valid_bit == 1)
		{
			if (p_table[i].time_stamp < min_time)
			{
				min_index = i;
				min_time = p_table[i].time_stamp;
			}
		}
	}
	
	return min_index;
}


void loop() 
{
	char input[100];
	char** args;

	extern struct Memory main_memory[32];
	extern struct Memory virtual_memory[128];
	extern struct PageTable p_table[16];
	extern int page_index;
	
	extern int fifo,lru;

	int index;
	int virtual_index;
	int temp;
	int temp_index;
	int temp_index2;
	int start_add;
	
	while (1)
	{
		printf("> ");
		fgets(input, 80, stdin);
		tokenize(input, args);

		if (strcmp(args[0], "quit") == 0)
		{
			exit(0);
		}
		else if (strcmp(args[0], "read") == 0)
		{
			
			index = atoi(args[1]);
			virtual_index = (int) index / 8;

			if (p_table[virtual_index].valid_bit == 0)
			{
				printf("A Page Fault Has Occurred\n");

				virtual_index = ((int) atoi(args[1]) / 8) * 8;
				
				temp_index = virtual_index;

				if (is_full() && fifo == 1)
				{
					virtual_index = get_first_index();
					page_index = p_table[virtual_index].page_num;

					p_table[virtual_index].valid_bit = 0;
					p_table[virtual_index].time_stamp = 0;
					p_table[virtual_index].page_num = virtual_index;
				}
				else if (is_full() && lru == 1)
				{
					
					virtual_index = get_least_index();
					page_index = p_table[virtual_index].page_num;

					p_table[virtual_index].valid_bit = 0;
					p_table[virtual_index].time_stamp = 0;
					p_table[virtual_index].page_num = virtual_index;
				}

				p_table[(int) atoi(args[1]) / 8].valid_bit = 1;
				p_table[(int) atoi(args[1]) / 8].page_num = page_index;

				for (temp = page_index * 8; temp < (page_index + 1) * 8; ++temp)
				{
					
					main_memory[temp].address = virtual_memory[temp_index].address;
					main_memory[temp].data = virtual_memory[temp_index].data;
					if (main_memory[temp].address == index)
					{
						printf("%d\n", main_memory[temp].data);
					}	
					temp_index++;
				}
				page_index++;
			}
			
			else
			{
				temp = p_table[virtual_index].page_num * 8;
				temp += atoi(args[1]) % 8;
				printf("%d\n", main_memory[temp].data);
			}
			

			if (lru == 1)
				p_table[virtual_index].time_stamp++;
		}
		else if (strcmp(args[0], "write") == 0)
		{
			int virtual_add = atoi(args[1]);
			virtual_index = (int) virtual_add / 8;
			int num = atoi(args[2]);

			temp_index = virtual_index;
			// temp_index2 = virtual_index;

			if (p_table[virtual_index].valid_bit == 0)
			{
				printf("A Page Fault Has Occurred\n");

				start_add = virtual_index * 8;
 
				if (is_full() && fifo == 1)
				{
					printf("yay");
					// virtual_index = get_first_index();

					// int temp;
					// for (temp = p_table[index].page_num * 8; temp < (p_table[index].page_num + 1) * 8; ++temp)
					// {
					// 	virtual_memory[temp_index2].data = main_memory[temp].data;
					// 	temp_index2++;
					// }
					
					// page_index = p_table[virtual_index].page_num;

					// p_table[virtual_index].valid_bit = 0;
					// p_table[virtual_index].time_stamp = 0;
					// p_table[virtual_index].page_num = virtual_index;
				}
				else if (is_full() && lru == 1)
				{
					printf("nay");
					// virtual_index = get_least_index();
					// page_index = p_table[virtual_index].page_num;

					// p_table[virtual_index].valid_bit = 0;
					// p_table[virtual_index].time_stamp = 0;
					// p_table[virtual_index].page_num = virtual_index;
				}


				p_table[virtual_index].valid_bit = 1;
				p_table[virtual_index].dirty_bit = 1;
				p_table[virtual_index].page_num = page_index;

				for (temp = page_index * 8; temp < (page_index + 1) * 8; ++temp)
				{
					printf("%d  -  ",temp);
					printf("%d\n",start_add);
					main_memory[temp].address = virtual_memory[start_add].address;
					main_memory[temp].data = virtual_memory[start_add].data;
					start_add++;
				}
				page_index++;

			}
			else
			{
				p_table[virtual_index].dirty_bit = 1;
				temp = p_table[virtual_index].page_num * 8;
				temp += atoi(args[1]) % 8;
				main_memory[temp].data = num;
			}

			if (lru == 1)
				p_table[virtual_index].time_stamp++;
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
		if (fifo == 1)
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