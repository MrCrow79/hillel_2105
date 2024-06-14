def division(a, b):

    # if b == 0:
    #     print('You cant division by 0')
    #     return

    print(f'You input 2 numbers {a}, {b}')

    try:  # код який може впасти
        # raise AttributeError
        result = a/b

    except ZeroDivisionError:  # помилка яку ви очікуєте
        print('You cant divide by 0')

    except TypeError:  # помилка яку ви очікуєте
        print('You have to put only numbers')

    except Exception:
        print('Something wend wrong')

    else:  # after finally if no errors in try block
        print('Eveything was correctly')
        return result

    finally:  # виконується завжди
        print('Done')



    # except (ZeroDivisionError, TypeError) as e: # помилка яку ви очікуєте
    #     print('Something wend wrong')





division(1,0)
print('-'*10)
# division('a',0)
print('-'*10)
print(division(1,2))