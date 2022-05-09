def squareRoot(n, l):

    og = n

    count = 0

    while (1):
        count += 1

        root = 0.5 * (og + (n / og))

        if (abs(root - og) < l):
            break

        og = root

    return root

n =int(input("Enter the number: "))
l = 0.00001
print(squareRoot(n, l))