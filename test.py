def largestNumber(array):
	if len(array)==1:
		return str(array[0])

	for i in range(len(array)):
		array[i]=str(array[i])

	for i in range(len(array)):
		for j in range(1+i,len(array)):
			if array[j]+array[i]>array[i]+array[j]:
				array[i],array[j]=array[j],array[i]

	result=''.join(array)
	
	if(result=='0'*len(result)):
		return '0'
	else:
		return result
#main
arr = [10, 68, 75, 7, 21, 12]
print(largestNumber(arr))