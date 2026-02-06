import math

def suma(z1, z2):
    return (z1[0] + z2[0], z1[1] + z2[1])


def resta(z1, z2):
    return (z1[0] - z2[0], z1[1] - z2[1])


def producto(z1, z2):
    a, b = z1
    c, d = z2
    return (a*c - b*d, a*d + b*c)


def division(z1, z2):
    a, b = z1
    c, d = z2
    denominador = c**2 + d**2
    if denominador == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return (
        (a*c + b*d) / denominador,
        (b*c - a*d) / denominador
    )


def modulo(z):
    return math.sqrt(z[0]**2 + z[1]**2)


def conjugado(z):
    return (z[0], -z[1])


def fase(z):
    return math.atan2(z[1], z[0])


def cartesiano_a_polar(z):
    return (modulo(z), fase(z))


def polar_a_cartesiano(p):
    r, theta = p
    return (r * math.cos(theta), r * math.sin(theta))

