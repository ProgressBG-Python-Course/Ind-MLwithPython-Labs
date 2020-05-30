import pandas as pd

df = pd.read_excel('../datasets/ames_datapreprocessing_knime.xlsx', encoding='utf-8', index=False);

df.to_csv('ames_datapreprocessing_knime.csv', encoding='utf-8')
