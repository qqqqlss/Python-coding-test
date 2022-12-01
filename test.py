<<<<<<< HEAD
T = int(input())

for test_case in range(1, T + 1):
	n, change = input().split()
	n=list(n)
	change= int(change)
	idx=0
	for _ in range(change):
		print(n)
		while True:
			if idx>=len(n):
				n[-1],n[-2]=n[-2],n[-1]
				break
			m=max(n[idx:])
			if n[idx]==m:
				idx+=1
				continue
			else:
				for i in range(len(n)-1,-1):
					if m==n[i]:
						print(n[idx],n[i])
						n[idx],n[i]=n[i],n[idx]
						idx+=1
						break
				else:
					break
	print('#'+str(test_case), ''.join(map(str,n)))
=======



print(solution())
>>>>>>> 82af5a3f9637718e4ac0a62229687ec41e87f8dd
