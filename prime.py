import math

def is_prime(number):
    """Devuelve True si el número es primo, False de lo contrario."""
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def main():
    """Función principal que imprime los números primos menores de 100."""
    for num in range(100):
        if is_prime(num):
            print(num, end=' ')
    print()

if __name__ == '__main__':
    main()
