temp = int(input('How is temperature, today?'))

#if temp >= 20 and temp <= 35:
#    print('The temperature is good today, go outside!')

#elif temp < 20 or temp > 35:
#    print('The temperature is bad today, stay Home!')

if not(temp >= 20 and temp <= 35):
    print('The temperature is bad today, stay Home!')

elif not(temp < 20 or temp > 35):
    print('The temperature is good today, go outside!')
