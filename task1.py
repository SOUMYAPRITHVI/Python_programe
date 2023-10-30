def fizzbizz(n):
    for i in range(1,n+1):
        if i%15==0:
            print("Fizzbizz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Bizz")
        else:
            print(i)
n=int(input("Enter a number:"))
fizzbizz(n)


def palindrome(n):
    if n==n[::-1]:
        print("True")
    else:
        print("False")

n=input("Enter a String:")
palindrome(n)
