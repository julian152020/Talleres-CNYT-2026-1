import unittest
import math
import complejos


class TestNumerosComplejos(unittest.TestCase):

    # ---------- SUMA ----------
    def test_suma_positivos(self):
        self.assertEqual(complejos.suma((1, 2), (3, 4)), (4, 6))

    def test_suma_negativos(self):
        self.assertEqual(complejos.suma((-1, -2), (1, 2)), (0, 0))

    # ---------- RESTA ----------
    def test_resta_basica(self):
        self.assertEqual(complejos.resta((5, 3), (2, 1)), (3, 2))

    def test_resta_negativos(self):
        self.assertEqual(complejos.resta((1, 1), (3, 5)), (-2, -4))

    # ---------- PRODUCTO ----------
    def test_producto_normal(self):
        self.assertEqual(complejos.producto((1, 2), (3, 4)), (-5, 10))

    def test_producto_con_cero(self):
        self.assertEqual(complejos.producto((0, 0), (5, 7)), (0, 0))

    # ---------- DIVISIÓN ----------
    def test_division_normal(self):
        r = complejos.division((1, 2), (3, 4))
        self.assertAlmostEqual(r[0], 0.44, places=2)
        self.assertAlmostEqual(r[1], 0.08, places=2)

    def test_division_identidad(self):
        r = complejos.division((5, 3), (1, 0))
        self.assertEqual(r, (5, 3))

    # ---------- MÓDULO ----------
    def test_modulo_3_4(self):
        self.assertEqual(complejos.modulo((3, 4)), 5)

    def test_modulo_cero(self):
        self.assertEqual(complejos.modulo((0, 0)), 0)

    # ---------- CONJUGADO ----------
    def test_conjugado_positivo(self):
        self.assertEqual(complejos.conjugado((5, -6)), (5, 6))

    def test_conjugado_cero(self):
        self.assertEqual(complejos.conjugado((0, 0)), (0, 0))

    # ---------- FASE ----------
    def test_fase_45_grados(self):
        self.assertAlmostEqual(
            complejos.fase((1, 1)),
            math.pi / 4,
            places=5
        )

    def test_fase_eje_x(self):
        self.assertAlmostEqual(
            complejos.fase((1, 0)),
            0,
            places=5
        )

    # ---------- CARTESIANO → POLAR ----------
    def test_cartesiano_a_polar(self):
        r, theta = complejos.cartesiano_a_polar((3, 4))
        self.assertAlmostEqual(r, 5)
        self.assertAlmostEqual(theta, math.atan2(4, 3))

    def test_cartesiano_a_polar_cero(self):
        r, theta = complejos.cartesiano_a_polar((0, 0))
        self.assertEqual(r, 0)
        self.assertEqual(theta, 0)

    # ---------- POLAR → CARTESIANO ----------
    def test_polar_a_cartesiano(self):
        z = complejos.polar_a_cartesiano((5, math.atan2(4, 3)))
        self.assertAlmostEqual(z[0], 3, places=5)
        self.assertAlmostEqual(z[1], 4, places=5)

    def test_polar_a_cartesiano_cero(self):
        z = complejos.polar_a_cartesiano((0, 1))
        self.assertEqual(z, (0, 0))


if __name__ == "__main__":
    unittest.main()
