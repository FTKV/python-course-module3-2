import turtle

def fibonacci(n):
    if n in (1, 2):
        return 1
    if not n:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    turtle.setup(1000, 1000)

    t = turtle.Turtle()

    for i in range(16):
        f = fibonacci(i)
        for j in range(4):
            t.fd(f)
            t.lt(90)
        t.circle(f, 90)

    turtle.mainloop()

if __name__ == "__main__":
    main()