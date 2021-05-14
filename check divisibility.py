# input the maximum number to 
# which you want to send 
max_num= 20

# starting numbers from 0 
n = 1

# run until it reaches maximum number 
print("Numbers not divisible by 2 and 3") 
while n <= max_num: 
	
	# check if number is divisible by 2 and 3 
	if n % 2 != 0 and n % 3 != 0: 
		print(n) 
	
	# incrementing the counter 
	n = n+1