while True:
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a/b
    except Exception as erro:
        print(erro.__class__)
    else:
        print(f'resultado da divisão {r}')
    finally:
        print('Arruma essa bagaça')
    '''except ZeroDivisionError:
        print('zero não divisível')
    except KeyboardInterrupt:
        print('alguma coisa errada')
        break'''
   