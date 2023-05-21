from dataclasses import dataclass


@dataclass
class Fruit:
    name: str

    def is_crisp(self):
        name = self.name
        if name:
            name = name.lower()
        if name in ["apple", "watermelon", "cherries"]:
            return True
        elif name in ["orange", "mango", "strawberry"]:
            return False
        else:
            raise ValueError(f"{name} not in known list of fruits.")
            return False
