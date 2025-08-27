// WAP to find whether given number is Pronic or not.
// A Pronic Number is defined as a number that is the product of two consecutive non-negative integers. In
// other words, N is a Pronic Number if there exists a non-negative integer k such that N = k * (k + 1).
// E.g. 6 is a Pronic Number because 6=2*3

#include<stdio.h>

int isPronic(int n)
{
    if(n < 0)
    {
        return 0;
    }

    for(int i = 0; i <= n*n; i++)
    {
        if(i * (i + 1) == n)
        {
            return 1;
        }
    }
    
    return 0;
}

int main()
{
    int num;

    printf("Enter the number: ");
    scanf("%d",&num);

    if(isPronic(num)){
        printf("Number is Pronic : %d \n",num);
    }
    else{
        printf("Number is not  Pronic : %d \n",num);
    }

    return 0;

}