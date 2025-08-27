#include<stdio.h>

int main(){
	
	int n,flag=1;
	printf("Enter  any numbere:");
	scanf("%d",&n);

	for(int i=2;i<n;i++){
		if(n%i==0){
			flag=0;
			break;
		}	
	}
	if(flag==1)
	{
		printf("number is prime");
	}
	else
    {
		printf("number is not prime");
	}
	return 0;

}