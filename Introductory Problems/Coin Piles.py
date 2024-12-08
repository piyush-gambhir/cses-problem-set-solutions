def coin_piles(a: int, b: int) -> bool:
    if(a+b)%3 != 0:
        return False
    
    if(a > 2*b or b > 2*a):
        return False
    
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print("YES" if coin_piles(a, b) else "NO")

