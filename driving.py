country = input("請問你是哪國人? ")
age = input("請輸入年齡: ")
age = int(age)
if country == "台灣":
	if age >= 18:
		print("你可以考駕照了喔!恭喜")
	else:
		print("你還不能考駕照喔!")
elif country == "美國":
	if age >=16:
		print("你可以考駕照了喔!")
	else:
		print("你還不能考駕照喔!")
else:
	print("喔喔!!你不是台灣人也不是米國人喔!!")