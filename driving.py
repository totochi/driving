country = input("請問你是哪國人? ")
age = input("請輸入年齡: ")
age = int(age)
if country == "台灣":
	if age >= 18:
		print("你可以考駕照了喔!恭喜")
	else:
		print("你還不能考駕照喔!")
else:
	print("你不是本國人")