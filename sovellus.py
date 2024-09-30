#sovellus -jonip

print("hello World")

def hello(n):
    if n == 1:
        print("!!!")
        return 1
    else:
        print("hello", end=" ")
        return hello(n - 1)

hello(4)