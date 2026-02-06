import complejos 

def leer_complejo():
    real = float(input("Parte real: "))
    imag = float(input("Parte imaginaria: "))
    return (real, imag)

def menu():
    print("\n=== MENÚ DE NÚMEROS COMPLEJOS ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Producto")
    print("4. División")
    print("5. Módulo")
    print("6. Conjugado")
    print("7. Cartesiano → Polar")
    print("8. Polar → Cartesiano")
    print("9. Fase")
    print("0. Salir")


if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo del programa 👋")
            break

        try:
            if opcion in ["1", "2", "3", "4"]:
                print("Ingrese el primer número complejo")
                z1 = leer_complejo()
                print("Ingrese el segundo número complejo")
                z2 = leer_complejo()

                if opcion == "1":
                    print("Resultado:", complejos.suma(z1, z2))
                elif opcion == "2":
                    print("Resultado:", complejos.resta(z1, z2))
                elif opcion == "3":
                    print("Resultado:", complejos.producto(z1, z2))
                elif opcion == "4":
                    print("Resultado:", complejos.division(z1, z2))

            elif opcion == "5":
                z = leer_complejo()
                print("Módulo:", complejos.modulo(z))

            elif opcion == "6":
                z = leer_complejo()
                print("Conjugado:", complejos.conjugado(z))

            elif opcion == "7":
                z = leer_complejo()
                print("Polar (r, θ):", complejos.cartesiano_a_polar(z))

            elif opcion == "8":
                r = float(input("Magnitud (r): "))
                theta = float(input("Ángulo (θ en radianes): "))
                print("Cartesiano:", complejos.polar_a_cartesiano((r, theta)))

            elif opcion == "9":
                z = leer_complejo()
                print("Fase (rad):", complejos.fase(z))

            else:
                print("Opción inválida ❌")

        except Exception as e:
            print("Error:", e)