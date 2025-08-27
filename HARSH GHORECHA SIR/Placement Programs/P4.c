// C Program to print the Floyd's Triangle
// For n=4
// 1
// 2 5
// 3 6 8
// 4 7 9 10
#include <stdio.h>

int main()
{
    
    int rows;
    printf("Enter the N :");
    scanf("%d",&rows);

    int n = 1;
    
    for (int i = 0; i < rows; i++) {
        
        for (int j = 0; j <= i; j++) {
            printf("%d ", n++);
        }
    }
    return 0;
}