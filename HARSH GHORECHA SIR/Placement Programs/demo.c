#include <stdio.h>

int main() {
    int n = 4; // Or take input from the user: int n; printf("Enter the number of rows: "); scanf("%d", &n);
    int current_num = 1;

    for (int i = 1; i <= n; i++) { // Outer loop for rows
        int starting_num_in_row = i;
        int gap_increment = n - 1; // Initial gap for the first number after the starting_num

        for (int j = 1; j <= i; j++) { // Inner loop for columns in each row
            if (j == 1) {
                printf("%d ", starting_num_in_row); // Print the first number (row number)
            } else {
                starting_num_in_row += gap_increment; // Calculate subsequent numbers
                printf("%d ", starting_num_in_row);
                gap_increment--; // Decrement the gap for the next number
            }
        }
        printf("\n"); // Move to the next line after each row
    }

    return 0;
}
