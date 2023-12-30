#include<stdio.h>
#include<math.h>

  
// a ^ b mod P

long long int power(long long int a, long long int b,

                                     long long int P)

{ 

    if (b == 1)

        return a;

  

    else

        return (((long long int)pow(a, b)) % P);

}

  


int main()

{

    long long int P, G, x, a, y, b, ka, kb; 

      

#Алиса выберет закрытый ключ
    P = 23; 

    printf("The value of P : %lld\n", P); 

  
# Sasha выберет закрытый ключ
    G = 9; 

    printf("The value of G : %lld\n\n", G); 

  

 
# Алиса выберет закрытый ключ a
    a = 4; 

    printf("The private key a for Alice : %lld\n", a);

    x = power(G, a, P); 

      

# Sasha выберет закрытый ключ b

    b = 3; 

    printf("The private key b for Sasha : %lld\n\n", b);

    y = power(G, b, P); 

  

   

        
 # gets the generated key
    ka = power(y, a, P); 
    kb = power(x, b, P); 

      

    printf("Secret key for the Alice is : %lld\n", ka);

    printf("Secret Key for the Sasha is : %lld\n", kb);

      

    return 0;

}
