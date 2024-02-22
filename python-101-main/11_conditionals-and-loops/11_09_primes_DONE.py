# Print out every prime number between 1 and 1000.

prime_list = "The prime list: "

for number in range(1001):
    # para cada numero analizar si es divisible entre 1, 1 num adicional, y sí mismo: number%1 number%counter number%number
    # 1 num adicional = contador de 1 a number
    # break: cuando número adicional = number
    # Condición: Necesito un contador de los divisores comunes, si es diferente a 2 (1 y a sí mismo) no es un numero primo.
    counter_adicional = 1
    counter_checker = 0
    while number >= counter_adicional:
        if number%counter_adicional == 0:
            counter_checker += 1
        counter_adicional += 1
    if counter_checker ==2 and number != 2:
        prime_list += str(number)+" "
        counter_checker = 0 

print(prime_list)