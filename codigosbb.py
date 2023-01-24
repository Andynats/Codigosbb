while True:

    INITIALNUMBER = int(input("\nEscribe el número inicial: \n>"))

    DAYS = input("\nDías: \n>")
    amountTickets = int(input("\nCuantos archivos? \n"))

    for i in range(amountTickets):
        with open(f'BB_{DAYS}D_{i+1}.csv', "w") as f:
             for j in range(i * 100, (i+1) * 100):
                numero = INITIALNUMBER + j
                f.write(f'BB_{DAYS}D_{numero}\n')

