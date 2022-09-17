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
    // ###################################################################################

	char const* const fileName = argv[1];
    FILE* file = fopen(fileName, "r");

    char input[500];      // original input
    char cmdline[500];    // copy of input
	char* args[2];        // argument vector

	printf("Welcome to ICS53 Online Cloud Storage.\n");

	int i = 1;
	while(i)
	{
		printf("> ");

        fgets(input, sizeof(input), file);
		// fgets(input, 500, stdin);

        strcpy(cmdline, input);
		parseline(input, args);

		if (strcmp(args[0], "quit") == 0)
		{
			printf("%s\n",cmdline);
			break;
		}
		else if (strcmp(args[0], "pause") == 0)
		{
            printf("%s",cmdline);
			sleep(atoi(args[1]));
        }
		else if (strcmp(args[0], "append") == 0)
		{
            printf("%s",cmdline);
			send(sock, cmdline, sizeof(cmdline), 0);  
			
            char stat[500] = {0};
            char empt[500] = {0};

            valread = read(sock, stat, sizeof(stat));
			
            if (memcmp(stat, empt, 500) != 0)
			{
				while (1)
				{

					char text[500];
					char text_copy[500];
					char* text_argv[2];
					printf("Appending> ");

					fgets(text, sizeof(text), file);
                    // fgets(text, 500, stdin);

                    strcpy(text_copy,text);
					printf("%s",text_copy);
					// printf("%s\n", text);
					// printf("text: %s", text);
					parseline(text, text_argv);

					if (strcmp(text_argv[0], "close") == 0)
					{
						// printf("CLOSED\n");
						send(sock, text_argv[0], sizeof(text_argv[0]), 0); 
						break;
					}
					else if (strcmp(text_argv[0], "close\n") == 0)
					{
						// printf("CLOSED\n");
						send(sock, text_argv[0], sizeof(text_argv[0]), 0); 
						break;
					}
					else if (strcmp(text_argv[0], "pause") == 0)
					{
						sleep(atoi(text_argv[1]));
					}
					else
					{
						send(sock, text_copy, sizeof(text_copy), 0);
					}
                    fflush(stdout);
				}
			}
			else
			{
				printf("File [%s] could not be found in remote directory.\n", args[1]);
			}
            fflush(stdout);
        }
		else if (strcmp(args[0], "upload") == 0)
		{
            printf("%s",cmdline);
			chdir("Local Directory");

            if (access(args[1], F_OK) == 0) 
            {
				send(sock, cmdline, strlen(cmdline), 0);
				FILE *fptr;
                
				int chunk_size = 1000;
				char file_chunk[chunk_size];

				fptr = fopen(args[1],"rb");   // Open a file in read-binary mode.
				fseek(fptr, 0L, SEEK_END);    // Sets the pointer at the end of the file.
				int file_size = ftell(fptr);  // Get file size.
				fseek(fptr, 0L, SEEK_SET);    // Sets the pointer back to the beginning of the file.

                // printf("FILE SIZE -------------------- %d\n", file_size);
				int total_bytes = 0;     // Keep track of how many bytes we read so far.
				int current_chunk_size;  // Keep track of how many bytes we were able to read from file (helpful for the last chunk).
				ssize_t sent_bytes;

				// send over an integer
				int converted_number = htonl(file_size);
                // printf("CONVERT -------------------- %d\n", converted_number);

				// // Write the number to the opened socket
				send(sock, &converted_number, sizeof(converted_number), 0);

				while (total_bytes < file_size)
				{
					// Clean the memory of previous bytes.
					bzero(file_chunk, chunk_size);
			
					// Read file bytes from file.
					current_chunk_size = fread(&file_chunk, sizeof(char), chunk_size, fptr);

					// printf("current_chunk_size: %d", current_chunk_size);

					// Sending a chunk of file to the socket.
					// sent_bytes = send(sock, &file_chunk, current_chunk_size, 0);
                    sent_bytes = send(sock, &file_chunk, strlen(file_chunk), 0);

					// Keep track of how many bytes we read/sent so far.
					total_bytes = total_bytes + sent_bytes;
                    // printf("--------%zd\n",sent_bytes);
                    // printf("+++%d\n",total_bytes);
                    // printf("/%d\n", file_size);
				}

                

				printf("%i bytes uploaded successfully.\n", total_bytes);
				fflush(stdout);
				fclose(fptr);
			}
			else 
			{
				printf("File [%s] could not be found in local directory.\n", args[1]);
			}
				
            chdir("..");
			sleep(1);
        }
		else if (strcmp(args[0], "download") == 0)
		{
			printf("%s",cmdline);
			send(sock, cmdline, sizeof(cmdline), 0);

			char stat[500] = {0};
			char empt[500] = {0};
            bzero(stat, 500);
            bzero(empt, 500);

			valread = read(sock, stat, sizeof(stat));

			if (memcmp(stat, empt, 500) == 0)
			{
				chdir("Local Directory");
				int received_int = 0;

				valread = read(sock, &received_int, sizeof(received_int));

				// printf("RECV INT -------------------- %d\n", received_int);

				int received_size;
				int chunk_size = 1000;
				char file_chunk[chunk_size];
				int chunk_counter = 0;
				int total_bytes = 0;

				FILE *fptr;
				fptr = fopen(args[1],"wb");

				// printf("RECV INT -------------------- %d\n", ntohl(received_int));



				// Keep receiving bytes until we receive the whole file.
				while (total_bytes < ntohl(received_int))
				{
					bzero(file_chunk, chunk_size);

					// Receiving bytes from the socket.
					received_size = recv(sock, file_chunk, chunk_size, 0);
					
					// printf("--------%d\n",received_size);
					// printf("+++%d\n",total_bytes);
					// printf("/%d", ntohl(received_int));

					int x = fwrite(&file_chunk, sizeof(char), received_size, fptr);
					total_bytes = total_bytes + received_size;
					
				}

				printf("%i bytes downloaded successfully.\n", total_bytes);
				fflush(stdout);
				// printf("EXIT\n");
				fclose(fptr);
				chdir("..");
			}	
			else
			{
				printf("File [%s] could not be found in remote directory.\n", args[1]);
			}

			fflush(stdout);
			sleep(1);
		}
		else if (strcmp(args[0], "delete") == 0)
		{
			printf("%s",cmdline);
            send(sock, cmdline, sizeof(cmdline), 0);
			char stat[500] = {0};
			char empt[500] = {0};
            bzero(stat, 500);
            bzero(empt, 500);
			valread = read(sock, stat, sizeof(stat));
			if (memcmp(stat, empt, 500) == 0)
				printf("File deleted successfully.\n");
			else
				printf("File [%s] could not be found in remote directory.\n", args[1]);

			fflush(stdout);
        }
		else if (strcmp(args[0], "syncheck") == 0)
		{
			printf("%s",cmdline);
			printf("Sync Check Report:\n");

			int local_flag = 0;

			chdir("Local Directory");
			if (access(args[1], F_OK) == 0) 
			{
				local_flag = 1;
				FILE *fptr = fopen(args[1], "r");
				fseek(fptr, 0, SEEK_END); // seek to end of file
				long int size = ftell(fptr); // get current file pointer
				fseek(fptr, 0, SEEK_SET);
				printf("- Local Directory:\n");
				printf("-- File Size: %ld bytes.\n", size);
				fclose(fptr);
				fflush(stdout);
			}
			

			send(sock, cmdline, strlen(cmdline), 0);

			char stat[4] = {0};
			char empt[4] = {0};
			valread = read(sock, stat, sizeof(stat));

			if (!local_flag)
			{ // only remote
				printf("- Remote Directory:\n");

				int received_int = 0;

				valread = read(sock, &received_int, sizeof(received_int));
				printf("-- File Size: %d bytes.\n", ntohl(received_int));

				unsigned char hash1[16] = {0};
				unsigned char hash2[16] = {0};

				MDFile(args[1],hash1);
				valread = read(sock, hash2, 1);

				printf("-- Sync Status: unsynced.\n");
			}
			else if (memcmp(stat, empt, 4) == 0)
			{
				printf("- Remote Directory:\n");

				int received_int = 0;

				valread = read(sock, &received_int, sizeof(received_int));

				printf("-- File Size: %d bytes.\n", ntohl(received_int));

				unsigned char hash1[16] = {0};
				unsigned char hash2[16] = {0};

				MDFile(args[1],hash1);
				valread = read(sock, hash2, sizeof(hash2));

				if (memcmp(hash1, hash2, 16) == 0)
					printf("-- Sync Status: synced.\n");
				else
					printf("-- Sync Status: unsynced.\n");
			}

			chdir("..");
			fflush(stdout);
		}
		else
		{
            printf("Command [%s] is not recognized.\n", args[0]);
        }
        i++;
	}

	close(client_fd);
	
	return 0;
}