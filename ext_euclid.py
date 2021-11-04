def ext_euclid(a, b):
	if b == 0:
		return a, 0, 1
	else:
		gcd, x, y = ext_euclid(b, a % b)
		return gcd, y - (a // b) * x, x


if __name__ == '__main__':
	i = int(input("i: "))
	j = int(input("j: "))
	print(ext_euclid(i, j))
