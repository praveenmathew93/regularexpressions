#Using regex to check for a valid E-MAIL address.

import re
#uppercase, lowercase and numbers, 
exp = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|de|edu|net)"
user_input = input()
if(re.search(exp, user_input)):
	print("The E-mail is valid")
else:
	print("The E-mail is invalid")