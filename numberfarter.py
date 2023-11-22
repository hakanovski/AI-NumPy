import random
import numpy as np

class ProfessionalRandomNumberGenerator:
    def __init__(self):
        self.range = (0, 100)  # Default range

    def set_range(self, start, end):
        self.range = (start, end)

    def generate(self):
        return random.uniform(*self.range)

    def generate_multiple(self, count, unique=False):
        if unique and (count > (self.range[1] - self.range[0])):
            raise ValueError("Range too small for the requested unique count")

        if unique:
            return random.sample(range(*self.range), count)
        else:
            return [self.generate() for _ in range(count)]

    def generate_normal_distribution(self, mean, std_dev, count=1):
        return np.random.normal(mean, std_dev, count)

# Example usage:
rng = ProfessionalRandomNumberGenerator()
rng.set_range(10, 50)
print("Single random number:", rng.generate())
print("Multiple random numbers:", rng.generate_multiple(5))
print("Unique random numbers:", rng.generate_multiple(5, unique=True))
print("Normal distribution:", rng.generate_normal_distribution(0, 1, 5))