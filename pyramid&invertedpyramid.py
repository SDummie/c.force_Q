def pyramid(n):
    for i in range(n,-1,-1):
        spaces = n-i
        stars = 2 * i +1
        print(" " * spaces + "*" * stars)
    
    for i in range(1 , n+1):
        spaces = n-i
        stars = 2 * i +1
        print(" " * spaces + "*" * stars)

if __name__ == "__main__":
    n = int(input("enter").strip())
    pyramid(n)
