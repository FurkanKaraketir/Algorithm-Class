firstElement = 1
secondElement = 1
counter = 3
while True:
    firstElement = firstElement + secondElement
    if firstElement > 1000:
        print("The first element in the Fibonacci sequence to exceed 1000 is: ", firstElement)
        break
    counter += 1
    secondElement = firstElement + secondElement
    if secondElement > 1000:
        print("The first element in the Fibonacci sequence to exceed 1000 is: ", secondElement)
        break
    counter += 1