
# before you running this project you need to install the following libraries
# pip install pandas
# pip install openpyxl

import pandas as pd

# Path to the Excel file
file_path = 'data/database.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Strip spaces from column names to avoid key errors
df.columns = df.columns.str.strip()

# Ensure that "Criterio", "Pontos" and "Obtidos" are created and present in the Excel file
if 'Criterio' in df.columns and 'Pontos' in df.columns and 'Obtidos' in df.columns:
    # Group by "Criterio" and calculate the percentage of maximum scores
    result = df.groupby('Criterio').apply(lambda group: (group['Pontos'] == group['Obtidos']).mean() * 100)
    result = result.reset_index(name='Percentual Pontuação Máxima')

    # Show the result
    print("Percentual de Salas que Obtiveram Pontuação Máxima por Critério:")
    print(result)
else:
    print("Erro: Certifique-se de que as colunas 'Criterio', 'Pontos' e 'Obtidos' estão presentes no arquivo Excel.")
