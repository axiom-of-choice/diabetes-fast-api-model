from food.fruits import Fruit
from config.config import logger


def test_is_crisp():
    logger.debug("Testing is_crisp")
    fruit = Fruit("apple")
    logger.debug(f"Testing {fruit.name}")
    assert fruit.is_crisp() == True
    assert Fruit("orange").is_crisp() == False
