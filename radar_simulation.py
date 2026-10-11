import pandas as pd
import numpy as np

def generate_radar_data():

    np.random.seed(42)

    data = {
        "distance": np.random.randint(100, 1000, 10),
        "doppler": np.random.uniform(10, 100, 10)
    }

    return pd.DataFrame(data)
