import random

# PASSWORD GENERATOR : Generates a random password choosing from :
# letters, upper or lower case
# numbers
# symbols

# Definition and merge of libraries
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*#@/,_-"
all = lower + upper + numbers + symbols
length = 20

# Main program
print("### PASSWORD GENERATOR ###")
password = "".join(random.sample(all, length))
print("Le mot de passe généré est : ", password)
