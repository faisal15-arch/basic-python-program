import random
import string

charvalues=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation

pass_len=12

password=""

for i in range(pass_len):
    st=random.choice(charvalues)
    
    password+=st
    
print(password)
    