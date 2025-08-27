//  WAP to find whether given number is Automorphic or not.
// An automorphic number is a number whose square ends with the same digits as the number itself.
// For example, 5 is automorphic because 5² = 25, which ends in 5.
// Similarly, 76 is automorphic because 76² = 5776, which ends in 76.

#include<stdio.h>

int isAutomorphic(int n)
{
    int sq = n * n;
    int temp = n;


    while(temp > 0){
        if(sq % 10 != temp % 10){
            return 0;
        }
        
        sq = sq / 10;
        temp = temp / 10;
    }
    return 1;
}

void main(){

    int num;

    printf("Enter the number: ");
    scanf("%d",&num);

    if(isAutomorphic(num)){
        printf("Number is AUTOMORPHIC : %d \n",num);
    }
    else{
        printf("Number is not  AUTOMORPHIC : %d \n",num);
    }

    //return 0;
}