#백준 3733번 Shares
while True:
    try:
        n, s = map(int, input().split())
        print(s//(n+1))
    except EOFError:
        break