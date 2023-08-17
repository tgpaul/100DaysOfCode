def test(var1, var2):
	print(var1, " ", var2)
	var1 += 1
	var2 = 'b'
	print(var1, " ", var2)
	return var1, var2

var1 =  10
var2 = "a"
print(var1, " ", var2)
var1, var2 = test(var1, var2)
print(var1, " ", var2)
    