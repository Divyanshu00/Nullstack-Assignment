n=int(input())
for i in range(n):
    marks = map(int,input().split())
    for i in marks:
    	if i>37 and i%5>2:
    		i+=5-(i%5)
    	print(i)