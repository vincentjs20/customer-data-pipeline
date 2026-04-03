import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "customers.json")

def load_customers():
    with open(DATA_PATH, "r") as file:
        return json.load(file)

