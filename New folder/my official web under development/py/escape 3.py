def intro():
    print('you come home feeling exhausted from your last adventure')
    print('what do you do now')
    print('1.you switch on the tv')
    print('2.you go take a shower')
    print('3.go to sleep')

    player = input('')
    if player == '1':
        print('you go switch on the tv')
    elif player == '2':
        print('you go take a shower')
    elif player == '3':
        print('you go to sleep') 
    else:
        print('invalid syntax')
        exit()      
intro()


    