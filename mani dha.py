def power (base,exp,mod):
    return(base**exp)%mod

p=int(input("Enter a prime number p:"))

q=int(input(f"Enter a primitive root q(q<{p}):"))
if q>=p:
    print("q must be less than p")
    exit()

x=int(input(f"Enter private key x for User A(x<{p}):"))
if x>=p:
    print("x must be less than p")
    exit()
A=power(q,x,p)

y=int(input(f"Enter private key of User B(y<{p}):"))
if y>=p:
    print("y must be less than p")
    exit()

B=power(q,y,p)

print("\n---User key Information---")
print(f"User A-> Private key:{x},Public Key (A):{A}")
print(f"User B-> Private key:{y},Public Key (B):{B}")

K1=power(B,x,p)
K2=power(A,y,p)

print("\n---Shared Secret Keys---")
print(f"User A computers K1=B^x mod p ={K1}")
print(f"User B computers K2=A^x mod p ={K2}")

if K1==K2:
    print("\nKey exchange successful.Shared secret key established")
else:
    print("\nkey exchange failed.keys do not match")

