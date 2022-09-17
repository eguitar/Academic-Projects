// Brennen Wong, brennew, 63218897
// Eric Trinh, edtrinh, 20091235

#include <stdlib.h>
#include <string.h>
#include <stdio.h>


unsigned char heap[64];

void initializeHeap()
{
	// initialize one single free block
	// 0x80 is 64 + 0 allocation status in hex
	heap[0] = 0x80;
	int i;
	for (i = 1; i < 63; i++)
		heap[i] = 0x0;
	heap[63] = 0x80;
}

// 0 = free, 1 = allocated
int get_block_status(unsigned char byte)
{
	if ((byte & 0x01) == 0x00)
		return 0;
	else
		return 1;
}

int get_block_size(unsigned char byte)
{
    return ((byte & 0xFE) >> 1);
}

unsigned char set_block_status(unsigned char byte, unsigned char status)
{// free status = 0, allocated status = 1
    byte = (byte) >> 1;
    byte = (byte) << 1;
    byte += status;
    return byte;
}

unsigned char set_block_size(unsigned char byte, unsigned int size)
{
    byte = (byte) << 7;
    byte = (byte) >> 7;
    char new_byte = (size) << 1;
    new_byte += byte;
    return new_byte;
}

// void print_heap()
// {
// 	int i;
// 	for (i = 0; i < 64; i++)
// 	{
// 		printf("heap index: %d \t hex: %x \n", i, heap[i]);
// 	}
// }

void allocate_block(int size)
{
    int i = 0;
    int found = 0;
	int block_size = -1;
    int block_status = -1;
    while (!found && i < 64)
	{
        block_size = get_block_size(heap[i]);
        block_status = get_block_status(heap[i]);
        
        if (!block_status && block_size - 2 >= size)
        {
            if (block_size - (size + 2) < 3)
                size = block_size - 2;

            found = 1;
            // allocated header
			// printf("allocated footer index : %d", i + size + 1);
            heap[i] = set_block_status(heap[i], 1);
            heap[i + size + 1] = set_block_status(heap[i + size + 1], 1);
            // allocate footer
            heap[i] = set_block_size(heap[i], size + 2);
            heap[i + size + 1] = set_block_size(heap[i + size + 1], size + 2);
            printf("%d\n", i + 1);
        }
        i += get_block_size(heap[i]);   // go to header of next block, 1);
    }

    if (!found)
    {
        return;
    }
                                        // splitting
	if (!get_block_status(heap[i]))		// check if the next block is not empty
	{
		int new_size = block_size - size - 2;
		// printf("free footer index : %d\n", i + new_size - 1);
		heap[i] = set_block_status(heap[i], 0);
        heap[i + new_size - 1] = set_block_status(heap[i + new_size - 1], 0);

        heap[i] = set_block_size(heap[i], new_size);
        heap[i + new_size - 1] = set_block_size(heap[i + new_size - 1], new_size);
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

void reset_block(int start, int end, int size)
{
    heap[start] = set_block_status(heap[start],0);
	heap[start] = set_block_size(heap[start], size);

    int i;
	for (i = start + 1; i < end; i++)
		heap[i] = 0x0;

	heap[end] = set_block_status(heap[end],0);
	heap[end] = set_block_size(heap[end], size);
}

int main()
{
	extern unsigned char heap[64];
	char input[100];
	char* args[3];

	initializeHeap();

    while (1)
	{
		printf("> ");
		fgets(input, 80, stdin);
		parseline(input, args);

        if (strcmp(args[0], "quit") == 0)
		{
			break;
		}
		else if (strcmp(args[0], "malloc") == 0)
		{
			allocate_block(atoi(args[1]));
		}
		else if (strcmp(args[0], "free") == 0)
		{
			int free_header = atoi(args[1]) - 1;									// free header index
            int free_footer = free_header + get_block_size(heap[free_header]) - 1;	// free footer index
            int free_size = get_block_size(heap[free_header]);
		
            // printf("%d  -  %d\n",free_header,free_footer);

            int left_header = -1;
            int left_footer = -1;
            int right_header = -1;
            int right_footer = -1;
            int new_size;
            
            if (!get_block_status(heap[free_header]))
                continue;

			if (free_header == 0)
            {
                right_header = free_footer + 1;
                right_footer = right_header + get_block_size(heap[right_header]) - 1;
                if (!get_block_status(heap[right_header]))         //  0 0
                {
					new_size = free_size + get_block_size(heap[right_header]);
					reset_block(free_header, right_footer, new_size);
                }
                else          //  0 1
                {
                    reset_block(free_header, free_footer, free_size);
                } 
            }
            else if (free_footer == 63)
            {
                left_footer = free_header - 1;
                left_header = left_footer - get_block_size(heap[left_footer]) + 1;
                // printf("%d  -  %d\n",left_header,left_footer);
                if (!get_block_status(heap[left_header]))         //  0 0
                {
                    
                    new_size = free_size + get_block_size(heap[left_header]);
					reset_block(left_header, free_footer, new_size);

                }
                else          //  1 0
                {
                    reset_block(free_header, free_footer, free_size);
                } 
            }
            else
            {
                right_header = free_footer + 1;
                right_footer = right_header + get_block_size(heap[right_header]) - 1;
                
                left_footer = free_header - 1;
                left_header = left_footer - get_block_size(heap[left_footer]) + 1;
                
                if (!get_block_status(heap[right_header]) && !get_block_status(heap[left_header]))         //  0 0 0
                {
                    new_size = free_size + get_block_size(heap[right_header]) + get_block_size(heap[left_header]);
					reset_block(left_header, right_footer, new_size);
                }
                else if (!get_block_status(heap[right_header]))    //  1 0 0
                {
                    new_size = free_size + get_block_size(heap[right_header]);
					reset_block(free_header, right_footer, new_size);
                }
                else if (!get_block_status(heap[left_header]))    //  0 0 1
                {
                    new_size = free_size + get_block_size(heap[left_header]);
					reset_block(left_header, free_footer, new_size);
                }
            }
		}
        else if (strcmp(args[0], "blocklist") == 0)
        {
            int i = 0;
            while (i < 64)
            {
                printf("%d, ", i + 1);
                printf("%d, ", get_block_size(heap[i]) - 2);
                if (get_block_status(heap[i]))
                    printf("allocated.\n");
                else
                    printf("free.\n");
                i += get_block_size(heap[i]);
            }
        }
		else if (strcmp(args[0], "writemem") == 0)
		{
			int size;  // count the size of the string to be added
			for (size = 1; args[2][size] != '\0'; size++){}

    		// printf("Length of the string: %d", i);
			int i;
			for (i = atoi(args[1]); i < atoi(args[1]) + size; i++)
			{
				heap[i] = args[2][i-atoi(args[1])];
				// printf("%x\n", heap[i]);
			}
		}
        else if (strcmp(args[0], "printmem") == 0)
		{
			int block_index = atoi(args[1]);
            int n = atoi(args[2]);
            int i;
            for (i = block_index; i < block_index + n; i++)
            {
                if (i == block_index + n - 1)
                    printf("%x\n", heap[i]);
                else
                    printf("%x ", heap[i]);   
            }	
		}
	}   
    return 0;
}