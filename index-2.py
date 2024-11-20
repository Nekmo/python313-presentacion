import plotly.graph_objects as go
import plotly_template

fig = go.Figure(go.Bar(
            x=[11.76, 92.57, 110.19],
            y=['3.13-nogil', '3.13.0', '3.12.6'],
            marker_color=['#FFD538', '#4973FF', '#4973FF'],
            orientation='h'))

fig.update_layout(
    title='Factorial number 24 threads (lower is better) - AMD Ryzen 9 7900',
    xaxis_title='Execution Time (ms)',
    yaxis_title='Python Versions',
    yaxis=dict(
        categoryorder='total ascending'
    ), template='dark-theme'
)

fig.show()