import json
import os
from pathlib import Path

class Calculator:
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.join(Path(__file__).parent, "config.json")
        self._load_config(config_path)
        self._init_operations()

    def _load_config(self, path):
        try:
            with open(path) as f:
                self.config = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.config = {
                "prompts": {
                    "enter": "Введіть",
                    "operation": "Оберіть операцію (+, -, *, /)",
                    "invalid": "Невірний ввід!"
                },
                "results": {
                    "template": "Результат:"
                },
                "limits": {
                    "max_input": 1000
                }
            }

    def _init_operations(self):
        from operations import Addition, Subtraction, Multiplication, Division
        self.operations = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division()
        }

    def run(self):
        a = self._get_valid_input("перше число")
        b = self._get_valid_input("друге число")
        op = input(f"{self.config['prompts']['operation']}: ")

        try:
            result = self.operations[op].execute(a, b)
            print(f"{self.config['results']['template']} {result}")
        except (KeyError, ValueError) as e:
            print(f"Помилка: {e}")

    def _get_valid_input(self, prompt):
        while True:
            try:
                value = float(input(f"{self.config['prompts']['enter']} {prompt}: "))
                if -self.config['limits']['max_input'] <= value <= self.config['limits']['max_input']:
                    return value
                print(f"Число має бути між ±{self.config['limits']['max_input']}")
            except ValueError:
                print(self.config['prompts']['invalid'])

if __name__ == "__main__":
    Calculator().run()