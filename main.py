x = [int(input("Введите числа: ")) for i in range(5)] #вводятся числа с клавиатуры
x = [x[i] ** 2 for i in range(0, 5)] #каждому значению приравнивается изначальное^2
print(x) #выводится список x
