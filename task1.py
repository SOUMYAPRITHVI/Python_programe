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


def palindrome(s):
    return s==s[::-1]
    

def panagram(n):
    alpha="abcdefghijklmnopqrstuvwxyz"
    # print(n)
    for i in alpha:
        if i not in n.lower():
            return False
    else:
        return True


def freq(n):
    d={}
    for i in n:
        if i.isalpha():
            i=i.lower()
            if i in d:
                d[i]+=1
            else:
                d[i]=1
    return d
                    

if __name__=="__main__":
    n=int(input("Enter a number:"))	 #import guard
    fizzbizz(n)
    s=input("Enter a String to check Palindrome:")
    print(palindrome(s))
    s=input("Enter a String to check Panagram:")
    print(panagram(s))
    s=input("Enter a String:")
    print(freq(s))
