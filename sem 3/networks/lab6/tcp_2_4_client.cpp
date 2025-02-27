#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/wait.h>

#define PORT 7777
#define BUFFER_SIZE 1024

int count_vowels(const char *word) {
    int count = 0;
    for (int i = 0; word[i] != '\0'; i++) {
        if (strchr("aeiouAEIOU", word[i]) != NULL) {
            count++;
        }
    }
    return count;
}

// Function to handle each client connection
void handle_client(int client_socket) {
    char buffer[BUFFER_SIZE];
    int n, max_vowels = 0;
    char word_with_max_vowels[BUFFER_SIZE] = {0};

    // Receive the number of words from the client
    recv(client_socket, buffer, sizeof(buffer) - 1, 0);
    n = atoi(buffer);
    printf("Number of words to process: %d\n", n);

    // Process each word
    for (int i = 0; i < n; i++) {
        memset(buffer, 0, sizeof(buffer));

        // Receive the word from the client
        recv(client_socket, buffer, sizeof(buffer) - 1, 0);
        buffer[strcspn(buffer, "\n")] = '\0'; // Remove newline character
        printf("Received word: %s\n", buffer);

        // Count vowels in the received word
        int vowels_count = count_vowels(buffer);
        if (vowels_count > max_vowels) {
            max_vowels = vowels_count;
            strcpy(word_with_max_vowels, buffer);
        }
    }

    send(client_socket, word_with_max_vowels, strlen(word_with_max_vowels), 0);
    printf("Sent word with most vowels: %s\n", word_with_max_vowels);
    close(client_socket);
    printf("Client disconnected.\n");
}

int main() {
    int server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_addr_len = sizeof(client_addr);

    // Create the server socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == -1) {
        perror("Failed to create socket");
        exit(EXIT_FAILURE);
    }

    // Bind the server socket to an IP and port
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    if (bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    // Listen for incoming connections
    if (listen(server_socket, 5) < 0) {
        perror("Listen failed");
        close(server_socket);
        exit(EXIT_FAILURE);
    }
    printf("Server listening on port %d...\n", PORT);

    while (1) {
        // Accept a new client connection
        client_socket = accept(server_socket, (struct sockaddr*)&client_addr, &client_addr_len);
        if (client_socket < 0) {
            perror("Accept failed");
            continue;
        }
        printf("Client connected.\n");

        // Fork a new process to handle the client
        pid_t pid = fork();
        if (pid == 0) { // Child process
            close(server_socket); // Child doesn't need the server socket
            handle_client(client_socket);
            exit(0); // Child process exits after handling client
        } else if (pid > 0) { // Parent process
            close(client_socket); // Parent doesn't need the client socket
            // Clean up child processes to avoid zombies
            signal(SIGCHLD, SIG_IGN);
        } else {
            perror("Fork failed");
        }
    }

    // Close the server socket
    close(server_socket);
    return 0;
}

