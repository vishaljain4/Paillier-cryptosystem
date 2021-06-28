import gmpy2
import random
from gmpy2  import mpz
random_state = gmpy2.random_state(42)
#def prime_generator(bits):
 #   temp = gmpy2.mpz_rrandomb(random_state, 1538)
  #  return gmpy2.next_prime(temp)



print("-----KEY GENERATION-----")
bit_size=1538
"""p=0 #Random p and q value generator
q=0
while(p==q):
    p= prime_generator(bit_size)
    q= prime_generator(bit_size)"""

#To input value of p and q
p= int(input("Enter value of p"))
q= int(input("Enter value of q"))

n= gmpy2.mul(p,q);
Lambda= gmpy2.mul(p-1,q-1);

print("\nThe first prime is p =  ",p)
print("\nThe second prime is q =  ", q)
print("\nThe composite module n =",n)

g=n+1;
print("\nThe encryption exponent g = ", g)

print("\nThe decryption exponent lambda =", Lambda)

print("\n-------------------------------------------------------------")

print("\nPlease Enter the options: ")
print("\n1 to Encrypt")
print("\n2 to Decrypt")
option= int(input("\nYour Option: "))

print("-------------------------------------------------------------")

if(option == 1):
    print("\nEncryption: ")
    m = random.randrange(1, 20, 3)
    r = random.randrange(1, n, 3)
    print("Plaintext to be encrypted is m = ",m)
    
    gm = gmpy2.powmod(g, m, n*n)
    rn = gmpy2.powmod(r, n, n*n)
    c= gmpy2.powmod(gm + rn, 1, n*n)
    print("\nCiphertext is c = ", c)
    
    
elif(option == 2):
    print("\nDecryption: ")
    c = int(input("\nCiphertext to be decrypted is c = "))
    x = gmpy2.powmod(c, Lambda, n*n) 
    l = gmpy2.powmod(gmpy2.mpz((x-1)/n), 1 , n)
    S = gmpy2.mpz(l)
    
    m = gmpy2.powmod(gmpy2.mpz(S/Lambda), 1 , n)
    print("\nDecrypted plaintext is m = ", m)
    
print("-------------------------------------------------------------")




