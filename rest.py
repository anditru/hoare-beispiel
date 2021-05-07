def rest(x, y):
    q = 0
    r = x
    while r >= y:
        r = r - y
        q = q + 1
    return r

def main():
    print(rest(12, 4))
    print(rest(10, 3))

if __name__ == '__main__':
    main()
