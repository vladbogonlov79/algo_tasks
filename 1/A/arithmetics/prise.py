rubles = int(input())
kopecks = int(input())
quantity = int(input())

rubles = rubles * quantity
kopecks = kopecks * quantity

if kopecks > 100:
    rubles =  rubles + (kopecks // 100)
    kopecks = kopecks % 100

    print(rubles, kopecks)


else:
    print(rubles,kopecks)










