def extended_euclidean_algorithm(a, b):
    if b > a:
        temp = a
        b = temp
    u = 1
    g = a
    x = 0
    y = b
    while True:
        if y == 0:
            v = (g - (a * u)) / b
            break
        else:
            q = g / y
            t = g % y
            g = q * y + t
            s = u - q * x
            u = x
            g = y
            x = s
            y = t
    return g, u, v


def pollard_rho(ax, ay, bx, by, p, g, h):
    u = ax - ay
    v = by - bx
    print(v)
    d, s, b = extended_euclidean_algorithm(v, p-1)
    w = s * u
    print(d, s, b)
    for i in range(1, d-1):
        t = (w/d) + i * ((p-1)/d)
        if g**t == (h % p):
            print(t)


def collision(g, h, p):
    ax = 0
    bx = 0
    ay = 0
    by = 0
    x = 1
    y = 0
    while x != y:
        x, ax, bx = func(x, g, h, p, ax, bx)
        y, ay, by = func(x, g, h, p, ay, by)
        # if x % y == 0 or y % x == 0:
        #   break
    print("The collision is: ", x, "and", y)
    print(ax, bx, ay, by)
    pollard_rho(ax, ay, bx, by, p, g, h)


def func(s, g, h, p, a, b):
    if 1 <= s <= p/3:
        s = (g * s) % p
        a += 1 % (p-1)
    elif p/3 <= s < 2*p/3:
        s = (s**2) % p
        a *= 2 % (p-1)
        b *= 2 % (p-1)
    elif 2*p/3 <= s < p:
        s = (s * h) % p
        b += 1 % (p-1)
    return s, a, b


def run():
    g_val = int(input("Please enter the value g: "))
    h_val = int(input("Please enter the value h: "))
    p_val = int(input("Please enter the prime p: "))
    collision(g_val, h_val, p_val)


run()

