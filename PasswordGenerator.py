import string
import random
import sys
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4="@#%&!$"
st=s1+s2+s3+s4
try:
    plen=int(input("Enter the password length:"))
except:
    sys.exit("please type only Number")

print("Your Random Password is: "+"".join(random.sample(list(st),plen)))