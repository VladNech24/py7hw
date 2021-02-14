summ= int(input())
UAH10 =int()
UAH20 =int()
UAH50 = int()
UAH100 =int()
UAH500 = int()
if (summ%10==0):
	while(summ>=500):
		UAH500+=1
		summ=summ-500
	while(summ>=100):
		UAH100+=1
		summ=summ-100
	while(summ>=50):
		UAH50+=1
		summ=summ-50
	while(summ>=20):
		UAH20+=1
		summ=summ-20
	while(summ>=10):
		UAH10+=1
		summ=summ-10
	print("Купюры наминалом 500грн:", UAH500)
	print("Купюры наминалом 100грн:", UAH100)
	print("Купюры наминалом 50грн:", UAH50)
	print("Купюры наминалом 20грн:", UAH20)
	print("Купюры наминалом 10грн:", UAH10)

else:
	print("Введите другую сумму")
