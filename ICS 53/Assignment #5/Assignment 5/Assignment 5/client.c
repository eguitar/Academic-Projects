// client.c

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#define PORT 9999

void ClientOne(int socketfd);
void ClientTwo(int socketfd);
void ClientThree(int socketfd);

void ServerOne(int socketfd);
void ServerTwo(int socketfd);
void ServerThree(int socketfd);

void sender_function(int socketfd);

int main()
{
    int client_socket;
    struct sockaddr_in serv_addr;
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
    client_socket = socket(AF_INET, SOCK_STREAM, IPPROTO_IP);
    inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);
    connect(client_socket, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
    sender_function(client_socket);
    return 0;
}

void sender_function(int socketfd)
{
    ClientThree(socketfd);
}

void ClientOne(int socketfd)
{
    const char * array = "This is a basic example of client server interface";
    char buf [20];
    memset(buf, 0, 20);
    int len = strlen(array);
    int bytes_sent = send(socketfd, array, len, 0);
    int bytes_recieved = recv(socketfd, buf, 20, 0);
    printf("%s\n", buf);
    close(socketfd);
}

void ClientTwo(int socketfd)
{
    const char * array = "10 20 30 40 50";
    char buf [20];
    memset(buf, 0, 20);
    int bytes_sent = send(socketfd, array, 8, 0);
    int bytes_recieved = recv(socketfd, buf, 20, 0);
    printf("%s\n", buf);
    close(socketfd);
}
void ClientThree(int socketfd)
{
    int temp = 53;
    char buf [20];
    memset(buf, 0, 20);
    sprintf(buf, "%i", temp);
    int bytes_sent = send(socketfd, buf, 20, 0);
    while(temp > 0)
    {
        int bytes_recieved = recv(socketfd, buf, 20, 0);
        temp = atoi(buf);
        memset(buf, 0, 20);
        if (bytes_recieved == 0)
        {
            printf("Variable Zeroed on Server.\n");
            close(socketfd);
            return;
        }
        temp = temp -7;
        if(temp <=0 )
        {
            temp = -1;
            printf("Variable Zeroed on Client\n");
            close(socketfd);
        }
        else
        {
            memset(buf, 0, 20);
            sprintf(buf, "%i", temp);
            bytes_sent = send(socketfd, buf, 20, 0);
        }
        
    }
}
