from collections import Counter
n=int(input())
for i in range(n):
	socks, pairs = Counter(map(int,input().strip().split())), 0
	for s in socks: 
		pairs += socks[s]//2
	print(pairs)