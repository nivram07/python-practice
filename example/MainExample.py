from problem_set import findGCD
from model.Car import Car


def checkParity(n):
    if n % 2 == 0:
        return 0
    return 1


def inRange(x, y):
    return x < 1 / 3 < y


def tripleChars(s):
    ans = ''
    for c in s:
        temp = c * 3
        ans += temp
    s = ans
    strlen = len(s)
    return [s, strlen]


def main():
    print("Hello World")
    print('2: ' + str(checkParity(2)))
    print(inRange(0, 4))
    print(inRange(0, 0))
    [result, length] = tripleChars("Hello")
    print(result)
    print(findGCD(12, 8))
    print(findGCD(8, 12))

    print(findGCD(54, 12))
    print(findGCD(12, 54))

    car = Car("Acura", "Integra", 1989)
    print(car.get_type())

if __name__ == "__main__":
    main()
