def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
    try:
        num = int(input('Ingresa un número: '))
        assert num>0,"Por favor ingresa un número positivo"
        print(divisors(num))
        print("Terminó mi programa")

    except ValueError:
        print("Por favor ingresa un número ")

if __name__ == '__main__':
    main()