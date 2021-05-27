//a program to list all the integers between two integers L and R (including L and R). L and R can be any integer between 1 and 100 inclusive.

#include <stdio.h>
 
int main(void) {
 
	// Define the two integer variables
	int L,R;
	int i;
 
	// Get L and R from the user
	scanf("%d", &L);
	scanf("%d", &R);
    
	// Write here the logic to print all integers between L and R
 
 for(i=0;i<((R-L)+1);i++)
 {
     printf("%d ",L+i);
 }
 
 
    
	return 0;
}