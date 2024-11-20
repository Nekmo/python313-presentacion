import pandas as pd
import plotly.express as px
import plotly_template

df_py312 = pd.read_csv('py3.13.0-stock.csv')
df_py312 = df_py312.loc[df_py312['name'].str.startswith('async_')]
df_py313_stock = pd.read_csv('py3.13.0-jit.csv')
df_py313_stock = df_py313_stock.loc[df_py313_stock['name'].str.startswith('async_')]

# Merge the dataframes on the 'name' column
df_merged = pd.merge(df_py312, df_py313_stock, on='name', suffixes=('_stock', '_jit'))
df_merged["name"] = df_merged["name"].str.replace("async_", "")
df_merged["name"] = df_merged["name"].str.replace("_", " ")

# Rename the columns
df_merged.rename(columns={'mean_stock': 'Stock', 'mean_jit': 'JIT', 'name': "Test name"}, inplace=True)

# Create a bar plot with separate columns for each dataframe
fig = px.bar(df_merged, x='Test name', y=['Stock', 'JIT'], barmode="group",
             title="Comparison of Stock and JIT means (lower is better)", template='dark-theme2')
fig.update_layout(
    yaxis_title="Total mean time (s)",
    legend_title="Python ver.",
)

# Show the figure
fig.show()