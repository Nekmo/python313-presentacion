import pandas as pd
import plotly.express as px
import plotly_template

df_py312 = pd.read_csv('py3.12.6.csv')
df_py313_stock = pd.read_csv('py3.13.0-stock.csv')
df_py313_nogil = pd.read_csv('py3.13.0-nogil.csv')
df_py313_nogil.columns = ['name', 'mean_py313_nogil', 'stddev_py313_nogil']
df_py313_jit = pd.read_csv('py3.13.0-jit.csv')
df_py313_jit.columns = ['name', 'mean_py313_jit', 'stddev_py313_jit']

df_common = pd.merge(df_py312, df_py313_stock, on='name', suffixes=('_py312', '_py313_stock'))
df_common = pd.merge(df_common, df_py313_nogil, on='name')
df_common = pd.merge(df_common, df_py313_jit, on='name')

# Rename the columns
df_common.rename(columns={
    'mean_py312': '3.12',
    'mean_py313_stock': '3.13-stock',
    'mean_py313_nogil': '3.13-nogil',
    'mean_py313_jit': '3.13-jit'
}, inplace=True)

# Sum the 'mean' values for each dataset
sum_py312_common = df_common['3.12'].sum()
sum_py313_stock_common = df_common['3.13-stock'].sum()
sum_py313_nogil_common = df_common['3.13-nogil'].sum()
sum_py313_jit_common = df_common['3.13-jit'].sum()

# Create a new dataframe with the aggregated results
df_aggregated_common = pd.DataFrame({
    'Python version': ['3.12', '3.13-stock', '3.13-nogil', '3.13-jit'],
    'Total Mean': [sum_py312_common, sum_py313_stock_common, sum_py313_nogil_common, sum_py313_jit_common]
})

# Create a bar plot with the aggregated results
fig = px.bar(df_aggregated_common, x='Python version', y='Total Mean', barmode="group", template='dark-theme',
             title='Pyperformance tests in seconds (lower is better)')

# Show the figure
fig.show()