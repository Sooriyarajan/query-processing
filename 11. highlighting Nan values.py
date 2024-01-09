import pandas as pd
import numpy as np
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])
rows, cols = np.random.choice(10, size=5), np.random.choice(4, size=5)
df.iloc[rows, cols] = np.nan
styled_df = df.style.applymap(lambda val: f'background-color: red' if pd.isna(val) else '')
styled_df
