def rest(x, y):
    # Eingabespezifikation: x >= 0 ^ y > 0
    
    '''
    x = 0 * y + x <=> x = x  passt
    Kein Widerspruch zu Eingabespezifikation
    '''

    # x = 0 * y + x  ^  x >= 0
    q = 0
    # x = q * y + x  ^  x >= 0
    r = x
    # SI: x = q * y + r  ^  r >= 0
    while r >= y:
        # SI ^ B: x = q * y + r  ^  r >= 0  ^  r >= y

        '''
        Von Vorbedingung der nächten Anweisung zu I ^ B:
        x = (q + 1) * y + (r - y) = q * y + y + r - y = q * y + r  passt

        r - y >= 0 <=> r >= y  passt

        wegen y >= 0 gilt r >= y => r >= 0  passt

        => alle drei Bedingungen erfüllt  passt
        '''

        # x = (q + 1) * y + (r - y)  ^  r - y >= 0
        r = r - y
        # x = (q + 1) * y + r  ^  r >= 0
        q = q + 1
        # SI: x = q * y + r  ^  r >= 0

    # SI ^ ¬B: x = q * y + r  ^  r < y 
    return r

def main():
    print(rest(12, 4))
    print(rest(10, 3))

if __name__ == '__main__':
    main()
