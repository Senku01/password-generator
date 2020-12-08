import random 
import string

letters= string.ascii_letters

numbs = '0123456789'

spe ='-+#$%!&_'

symbols = letters+numbs+spe

len =int(input("Enter Pass.length:"))

password = ''.join(random.sample(
    
    symbols,len)
)
print(password)