def a():
    spam = "Antelope"
    print("spam is " + spam)
    b()
    print("spam is " + spam)


def b():
    spam = "Badger"
    print("spam is " + spam)
    c()
    print("spam is " + spam)


def c():
    spam = "Camel"
    print("spam is " + spam)

a()
