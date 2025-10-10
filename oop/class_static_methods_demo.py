class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: adds two numbers (no access to class or instance data)"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: multiplies two numbers and prints class attribute"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
