#TEMPERATURE SCALE CONVERSION

# (°F – 32) × 5/9 = °C <=> F = 9/5 * C + 32
# K − 273.15 = °C <=> 

scaleCheck = False
tempCheck = False

values = ['C','c','F','f','K','k']
    
# Checking the validity of the scale to be selected
while not(scaleCheck):
    print ('Please select the temperature scale: ')
    tempSc = input('C = Celsius  F = Fahrehneit  K = Kelvin : ' ) #temperature Scale
    for x in values:
        if tempSc == x:
            scaleCheck = True
    if not(scaleCheck):
        print('Invalid input')

print('\n')       
C = -290   #Absolute zero in Celsius = -273.15   \\
F = -500  #Absolute zero in Fahrenheit = -459.67  initialization below absolute 0 for each temperature scale
K = -1     #Absolute zero in Kelvin = 0          // 

while not(tempCheck):
    try:
        temp = float(input('Please insert a temperature : '))
        if (tempSc == values[0] or tempSc == values[1]):   # if the temperature is in Celsius
            if temp > -273.15:
                C = temp
                tempCheck = True
        elif (tempSc == values[2] or tempSc == values[3]): # if the temperature is in Fahrehneit
            if temp > -459.67:
                F = temp
                tempCheck = True 
        else:
            if temp > 0:                                   # if the temperature is in Kelvin
                K = temp
                tempCheck = True
        
        if not(tempCheck):
            print('Invalid input')  
    except:
        print('Invalid input')
     
# calculating values in other scales
if C > - 273.15:      # if Celsius is the primary scale
    K = C + 273.15
    F = 9/5 * C + 32
elif F > -459.67:     # if Fahrenheit is the primary scale
    C = 5/9 * (F - 32)
    K = C + 273.15
else:                 # if Kelvin is the primary scale
    C = K - 273.15
    F = 9/5 * C + 32  
    
print('\n')

if C > 30:
    print ('It\'s really hot')
elif C > 13:
    print ('The weather is nice')
elif C > 5:
    print ('It\'s cold')
else:
    print ('It\'s very cold')

print ('Temperature in Celsius: ', "{:.2f}".format(C),'°C')
print ('Temperature in Fahrenheit: ', "{:.2f}".format(F),'°F')
print ('Temperature in Kelvin: ', "{:.2f}".format(K),'K')
print()
input ('Press Enter to exit...')




