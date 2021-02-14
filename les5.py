a = (1,1.3,33,44,2.1,6)
def my_square(num):
    while(int(num)):
        return num ** 2
squared_numbers = list(map(my_square, a))
print(squared_numbers)
