// Brennen Wong, brennew, 63218897
// Eric Trinh, edtrinh, 20091235
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
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


int server_fd;
int new_socket;

int main(int argc, char *argv[])
{
	int valread;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[500];

	// Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
	{
        perror("socket failed");
        exit(EXIT_FAILURE);
    }
 
    // Forcefully attaching socket to the port 9999
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)))
	{
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
	
    address.sin_family = AF_INET;
    if ((inet_pton(AF_INET, argv[1], &address.sin_addr) <= 0))
	{
        printf("\nInvalid address/ Address not supported \n");
        return -1;
	}
    address.sin_port = htons(PORT);
 
    // Forcefully attaching socket to the port 9999
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) 
	{
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }
    if ((new_socket = accept(server_fd, (struct sockaddr*)&address, (socklen_t*)&addrlen)) < 0)
	{
        perror("accept");
        exit(EXIT_FAILURE);
    }

	// ###################################################################################
    // ###################################################################################

	int i = 1;
	while (i)
	{
		char* args[2];        // argument vector
		valread = read(new_socket, buffer, sizeof(buffer));

		if (valread <= 0)
			break;            // go back and look for new connections

		// printf("%d+++++++%s",i,buffer);
		// fflush(stdout);
		parseline(buffer,args);

		if (strcmp(args[0], "append") == 0)
		{
			chdir("Remote Directory");

            if (access(args[1], F_OK) == 0) 
			{
				char stat[500] = {1};
				send(new_socket, stat, sizeof(stat), 0);

				FILE *fp = fopen(args[1], "a");
				fprintf(fp, "\n");
				while(1)
				{
					char text[500] = {0};
					bzero(text, 500);

					// char appendBufferCopy[1024] = { 0 };
					// bzero(appendBufferCopy, 1024);
					valread = read(new_socket, text, sizeof(text));

					// strcpy(appendBufferCopy, appendBuffer);
					// appendBufferCopy[strlen(appendBufferCopy)] = '\0';

					// printf("%lu: %s\n",strlen(), appendBufferCopy);
					// printf("%lu: %s\n", strlen(text), text);

					
					if (strcmp(text, "close") == 0)
					{
						// printf("YAY");
						fflush(stdout);
						break;
					}
					else if (strcmp(text, "close\n") == 0)
					{
						// printf("NAY");
						fflush(stdout);
						break; 
					}
					else
					{
						
						fprintf(fp, "%s", text);
						fflush(fp);
					}
				}
				// printf("closed fp");
				fclose(fp);



			}
			else 
			{
				char stat[500] = {0};
				send(new_socket, stat, sizeof(stat), 0);
			}
			// printf("QUIT APPENDING MODE");
            chdir("..");
			fflush(stdout);
		}
		else if (strcmp(args[0], "upload") == 0)
		{
			chdir("Remote Directory");

			int received_int = 0;

			valread = read(new_socket, &received_int, sizeof(received_int));

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
				received_size = recv(new_socket, file_chunk, chunk_size, 0);
				
				// printf("--------%d\n",received_size);
				// printf("+++%d\n",total_bytes);
				// printf("/%d", ntohl(received_int));

				int x = fwrite(&file_chunk, sizeof(char), received_size, fptr);
				total_bytes = total_bytes + received_size;
				
			}


			// printf("EXIT\n");
			fclose(fptr);

			chdir("..");
		}
		else if (strcmp(args[0], "download") == 0)
		{
			chdir("Remote Directory");
			char success[500] = {0};
			char failure[500] = {1};
			if (access(args[1], F_OK) == 0)
			{
				send(new_socket, success, 500, 0);

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
				send(new_socket, &converted_number, sizeof(converted_number), 0);

				while (total_bytes < file_size)
				{
					// Clean the memory of previous bytes.
					bzero(file_chunk, chunk_size);
			
					// Read file bytes from file.
					current_chunk_size = fread(&file_chunk, sizeof(char), chunk_size, fptr);

					printf("current_chunk_size: %d", current_chunk_size);

					// Sending a chunk of file to the socket.
					// sent_bytes = send(sock, &file_chunk, current_chunk_size, 0);
                    sent_bytes = send(new_socket, &file_chunk, strlen(file_chunk), 0);

					// Keep track of how many bytes we read/sent so far.
					total_bytes = total_bytes + sent_bytes;
                    printf("--------%zd\n",sent_bytes);
                    printf("+++%d\n",total_bytes);
                    printf("/%d\n", file_size);
				}

                

				printf("%i bytes uploaded successfully.\n", total_bytes);
				fflush(stdout);
				fclose(fptr);
			}
			else
			{
				send(new_socket, failure, 500, 0);
			}
			chdir("..");
		}
		else if (strcmp(args[0], "delete") == 0)
		{
			// printf("DELETE\n");
			// printf("%s\n", args[1]);
			chdir("Remote Directory");
			char success[500] = {0};
			char failure[500] = {1};
			if (remove(args[1]) == 0)
			{
				send(new_socket, success, 500, 0);
				// printf("SUCCESS\n");
			}
			else
			{
				send(new_socket, failure, 500, 0);
				// printf("FAILURE\n");
			}
			chdir("..");
		}
		else if (strcmp(args[0], "syncheck") == 0)
		{
			chdir("Remote Directory");

			char stat[4] = {0};

            if (access(args[1], F_OK) != 0) 
				for (int i = 0; i < 4; ++i)
			        stat[i] = 1;
				
			send(new_socket, stat, sizeof(stat), 0);

			if (access(args[1], F_OK) == 0) 
			{
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

				// // Write the number to the opened socket
				send(new_socket, &converted_number, sizeof(converted_number), 0);

				unsigned char hash2[16] = {0};

				MDFile(args[1],hash2);
				send(new_socket, hash2, sizeof(hash2), 0);
			}

			chdir("..");
		}

		i++;
	}

	close(new_socket);

  	// closing the listening socket
    shutdown(server_fd, SHUT_RDWR);
	
	return 0;
}
