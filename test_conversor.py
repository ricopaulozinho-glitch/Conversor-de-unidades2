import unittest

from conversor import convert


class ConvertTests(unittest.TestCase):
    def test_all_conversions(self):
        cases = (
            ("a", 1500, 1.5),
            ("b", 2.5, 250),
            ("c", 250, 2.5),
            ("d", 1609.344, 1),
            ("e", 2, 3218.688),
            ("f", 250, 2.5),
            ("g", 3, 300),
            ("h", 25000, 2.5),
            ("i", 1.5, 15000),
        )

        for option, value, expected in cases:
            with self.subTest(option=option):
                self.assertAlmostEqual(convert(option, value), expected)

    def test_unknown_option_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Opção inválida"):
            convert("z", 1)


if __name__ == "__main__":
    unittest.main()