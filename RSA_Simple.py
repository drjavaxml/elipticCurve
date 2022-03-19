print('start')

x = 13 #first prime
print('first prime x ' + str(x))
y =  11 #second prime
print('second prime y ' + str(y))
m = x*y #modulus
print('modulus ' + str(m))
e = 7 # coprime with p and q below
pk = 0 # will become private key
txt = 123 # must be less than modulus. This is the original text to be encrypted
phi = (x-1)*(y-1) # x-1 is p and y-1 are used to caclulate phi
print('phi ' + str(phi)) #needed to find the private key below

i: int
for i in range(1,m):
    v = e*i%phi
    if (v == 1): # at this point i will be the private key
        print('Private key ' + str(i)) #the private key
        pk = i # now set the private key
        break

print('Text ' + str(txt)) #original text

ct = txt**e%m # cypher text encode with public key e
print('Cypertext ' + str(ct))
dt = ct**pk%m # decode with private key
print('Decodetext ' + str(dt)) #expect this to be same as original text
print('stop')






