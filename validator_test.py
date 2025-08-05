import unittest
from validator import load_logic, validate_input

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.logic = load_logic("dcaa_audit_logic_engine_v0.1.yaml")

    def test_marketing_cost(self):
        result = validate_input(self.logic, "Employee claimed marketing cost")
        self.assertEqual(result, "Disallow: Marketing costs are unallowable.")

    def test_time_entry(self):
        result = validate_input(self.logic, "Hours were entered after deadline")
        self.assertEqual(result, "Flag: Late time entry detected.")

if __name__ == '__main__':
    unittest.main()
