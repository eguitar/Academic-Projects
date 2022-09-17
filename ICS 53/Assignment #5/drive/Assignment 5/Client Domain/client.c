// Brennen Wong, brennew, 63218897
// Eric Trinh, edtrinh, 20091235
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include "Md5.c"
#define PORT 9999


void parseline(char* input, char** args)
{
    const char* delim = "\t\n ";
    char* token = strtok(input,delim);
    unsigned i = 0;
    while(token != NULL && i < 2)
    {
        args[i] = token;
        token = strtok(NULL, delim);
        i++;
    }
}


int main(int argc, char *argv[])
{
	int sock = 0, valread, client_fd;
    struct sockaddr_in serv_addr;
    char buffer[1024] = { 0 };

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        printf("\n Socket creation error \n");
        return -1;
    }

	serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Convert IPv4 and IPv6 addresses from text to binary form
    if (inet_pton(AF_INET, argv[2], &serv_addr.sin_addr) <= 0)
    {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }
 
    if ((client_fd = connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr))) < 0)
    {
        printf("\nConnection Failed \n");
        return -1;
    }

	// ###################################################################################

	char const* const fileName = argv[1];
    FILE* file = fopen(fileName, "r");

    char input[500];      // original input
    char cmdline[500];    // copy of input
	char* args[2];

	printf("Welcome to ICS53 Online Cloud Storage.\n");

	while(1)
	{
		printf("> ");


		parseline(input, args);


		if (strcmp(args[0], "quit") == 0)
		{
			break;
		}
		else if (strcmp(args[0], "pause") == 0)
		{}
		else if (strcmp(args[0], "append") == 0)
		{}
		else if (strcmp(args[0], "upload") == 0)
		{}
		else if (strcmp(args[0], "download") == 0)
		{}
		else if (strcmp(args[0], "delete") == 0)
		{}
		else if (strcmp(args[0], "syncheck") == 0)
		{}
		else
		{}
	}

	close(client_fd);
	
	return 0;
}