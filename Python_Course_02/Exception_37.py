try:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    result = a / b
except ZeroDivisionError:
    print('Do not divide to 0...')
# except Exception:
#     print('I excepted all exceptions!')
else:
    print(result)
finally:
    print('Done!')
