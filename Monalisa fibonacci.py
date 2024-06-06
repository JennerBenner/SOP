import turtle

def fibonacci(n):
    fibonacci_sequence = [4, 3]
    while len(fibonacci_sequence) <= n:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)
    return fibonacci_sequence


turtle.setup(1200, 1600)
screen = turtle.Screen()
screen.bgpic("Mona_Lisa - Copy.gif")

t = turtle.Turtle()
t.speed(0)
t.goto(-60, 100)
t.pendown()

fibonacci_sequence = fibonacci(1000)
for x in range(len(fibonacci_sequence)):
    t.width((1 +2.2360679775) /2)
    t.forward(fibonacci_sequence[x])
    t.right(90)

turtle.done()

