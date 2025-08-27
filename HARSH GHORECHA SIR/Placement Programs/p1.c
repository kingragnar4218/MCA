// WAP to find whether given number is Ugly or not.
// An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
// Input: n = 6 Output: true Explanation: 6 = 2 × 3

#include<stdio.h>

int ugly(int n)
{
    if(n <= 0 ){
        return 0;
    }
    if(n == 1){
        return 1;
    }

    while(n % 2 ==0){
        n = n / 2;
    }

    while(n % 3 == 0){
        n = n / 3;
    }

    while(n % 5 == 0){
        n = n /5;
    }

    return(n == 1);

}


int main()
{
    int num;

    printf("Enter the number: ");
    scanf("%d",&num);

    if(ugly(num))
    {
        printf("Number is UGLY : %d",num);
    }
    else
    {
        printf("Number is Not UGLY : %d",num);
    }

    return 0;
}