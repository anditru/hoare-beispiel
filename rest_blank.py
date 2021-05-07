def rest(x, y):
    # Eingabespezifikation: x >= 0 ^ y > 0

    '''
    
    
    '''

    #
    q = 0
    #
    r = x
    # SI:
    while r >= y:
        # SI ^ B:

        '''
        Von Vorbedingung der nächten Anweisung zu I ^ B:
        

        

        

        
        '''

        #
        r = r - y
        #
        q = q + 1
        # SI:

    # SI ^ ¬B:
    return r

def main():
    print(rest(12, 4))
    print(rest(10, 3))

if __name__ == '__main__':
    main()
