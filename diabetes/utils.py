import random
import numpy as np


def set_seeds(seed: int = 42) -> None:
    """Set seeds for reproducibility.

    Args:
        seed (int, optional): seed for reproducibility. Defaults to 42.
    """
    random.seed(seed)
    np.random.seed(seed)
