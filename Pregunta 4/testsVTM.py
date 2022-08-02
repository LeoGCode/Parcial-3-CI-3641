import unittest
from unittest.mock import patch
from VirtualTableManager import VirtualTableManager

class TestVirtualTableManager(unittest.TestCase):
    def setUp(self):
        self.manager = VirtualTableManager()

    def test_create_class_correct(self):
        self.manager.create_class(["Base", "f", "g"])
        self.assertEqual(self.manager.classes, {"Base": [("Base", "f"), ("Base", "g")]})

    def test_create_class_repeated_methods(self):
        self.manager.create_class(["Base", "f", "f"])
        self.assertEqual(self.manager.classes, {})

    def test_create_class_repeated_methods_super(self):
        self.manager.create_class(["Base", "f", "f"])
        self.manager.create_class(["Base", "g", "g"])
        self.assertEqual(self.manager.classes, {})

    def test_create_class_invalid_parameters(self):
        self.manager.create_class([])
        self.assertEqual(self.manager.classes, {})

    def test_create_class_already_exists(self):
        self.manager.create_class(["Base", "f", "g"])
        self.manager.create_class(["Base", "f", "g"])
        self.assertEqual(self.manager.classes, {"Base": [("Base", "f"), ("Base", "g")]})

    def test_create_class_super_class_not_exists(self):
        self.manager.create_class(["Base", "f", "g"])
        self.manager.create_class(["Base", ":", "NoExist", "h", "i"])
        self.assertEqual(self.manager.classes, {"Base": [("Base", "f"), ("Base", "g")]})

    def test_create_class_inherited_methods_correct(self):
        self.manager.create_class(["Base", "f", "g"])
        self.manager.create_class(["A", ":", "Base", "h", "i"])
        self.assertEqual(self.manager.classes, {"Base": [("Base", "f"), ("Base", "g")], 
                                                "A": [("Base", "f"), ("Base", "g"), ("A", "h"), ("A", "i")]})

    def test_create_class_inherited_methods_repeated_methods(self):
        self.manager.create_class(["Base", "f", "g"])
        self.manager.create_class(["A", ":", "Base", "f", "h", "h"])
        self.assertEqual(self.manager.classes, {"Base": [("Base", "f"), ("Base", "g")]})

    def test_describe_class_correct(self):
        self.manager.create_class(["Base", "f", "g"])
        self.manager.describe_class(["Base"])
        self.assertEqual(self.manager.classes, {"Base": [("Base", "f"), ("Base", "g")]})

    def test_describe_class_not_exists(self):
        self.manager.describe_class(["Base"])
        self.assertEqual(self.manager.classes, {})

    def test_describe_class_invalid_parameters(self):
        self.manager.describe_class([])
        self.assertEqual(self.manager.classes, {})

    def test_inherited_methods_correct(self):
        self.manager.create_class(["Base", "f", "g"])
        result = self.manager.inherited_methods("A", ["f", "h"], [("Base", "f"), ("Base", "g")])
        self.assertEqual(result, [('A', 'f'), ('Base', 'g'), ('A', 'h')])

    def test_begin_program(self):
        test_cases = [
            "class Base f g",
            "describe Base",
            "invalid action",
            "exit"
        ]
        with patch('builtins.input', side_effect=test_cases):
            self.manager.begin_program()
            self.assertEqual(self.manager.classes, {"Base": [("Base", "f"), ("Base", "g")]})

if __name__ == '__main__':
    unittest.main()

        