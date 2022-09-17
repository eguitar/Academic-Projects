// server.c

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <string.h>
#define PORT 9999

void ServerOne(int socketfd)
{
    char buf[256];
    memset(buf, 0, 256);
    int bytes_received = recv(socketfd, buf, 256, 0);
    int count = 0;
    const char * delims = " \t\n\r";
    char * word = strtok(buf, delims);
    while(word != NULL)
    {
        count++;
        word = strtok(NULL, delims);
    }
    memset(buf, 0, 256);
    sprintf(buf, "%d", count);
    int bytes_sent = send(socketfd, buf, strlen(buf), 0);
    close(socketfd);
}

void ServerTwo(int socketfd)
{
    char buf[256];
    memset(buf, 0, 256);
    int bytes_received = recv(socketfd, buf, 256, 0);
    int count = 0;
    const char * delims = " \t\n\r";
    char * word = strtok(buf, delims);
    int total = 0;
    while(word != NULL)
    {
        count++;
        total += atoi(word);
        word = strtok(NULL, delims);
    }
    memset(buf, 0, 256);
    double avg = total/count;
    sprintf(buf, "%f", avg);
    int bytes_sent = send(socketfd, buf, strlen(buf), 0);
    close(socketfd);
}

void ServerThree(int socketfd)
{
    
    char buf [20];
    memset(buf, 0, 20);
    int bytes_recieved = recv(socketfd, buf, 20, 0);
    int temp = atoi(buf);
    while(temp > 0)
    {
        temp = temp -7;
        if (temp <= 0)
        {
            close(socketfd);
        }
        else
        {
            memset(buf, 0, 20);
            sprintf(buf, "%i", temp);
            int bytes_sent = send(socketfd, buf, 20, 0);
        }
        bytes_recieved = recv(socketfd, buf, 20, 0);
        if(bytes_recieved == 0)
        {
            close(socketfd);
            return;
        }
    }
}

void receiver_function(int socketfd)
{
    ServerThree(socketfd);
}

int main()
{
    int client_socket, server_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    setsockopt(server_socket, SOL_SOCKET, SO_REUSEADDR , &opt, sizeof(opt));
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = inet_addr("127.0.0.1");
    address.sin_port = htons(PORT);
    bind(server_socket, (struct sockaddr*)&address, sizeof(address));
    listen(server_socket, 1);
    client_socket = accept(server_socket, (struct sockaddr*)&address, (socklen_t*)&addrlen);
    receiver_function(client_socket);
    close(server_socket);
    return 0;
}
