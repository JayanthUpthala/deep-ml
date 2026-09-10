def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	res = [None]*len(a)
	if(len(a)!=len(b)):
		return -1
	elif(len(a)==len(b)):
		for i in range(len(a)):
			res[i] = a[i]+b[i]
	if(res[0]!=None): return res
	# pass