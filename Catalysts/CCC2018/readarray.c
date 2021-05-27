
#include <stdio.h>
#include <string.h>

 char enteredSequence[40];
 int i, count,number,check[7];

 F(char n)
{
    printf("Use the %c\n",n);

 }

int main()
{
     printf("Input Name:\n");
     gets(enteredSequence);
    i = strlen(enteredSequence);
puts(enteredSequence);
    for(count=0; count<i; count++)
    {
       /* check[1] = strcmp(&enteredSequence[count],"F");
        check[2] = strcmp(&enteredSequence[count],"T");*/
    if(enteredSequence[count]=='F')
    {
        printf("F found\n");
        printf("%c\n",enteredSequence[count+1]);
        number=enteredSequence[count+1];
        F(number);

    }
    if(enteredSequence[count]=='T')
    {
        printf("T found\n");
        printf("%c\n",enteredSequence[count+1]);
        number=enteredSequence[count+1];
        F(number);
    }
  /*if(enteredSequence[count]>0)
    {
        printf("NUMBER found");
           }
*/
    //check[3] = strcmp(enteredCoursecode,storedCourseName);
    }

}

