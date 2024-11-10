import copy

import plotly.graph_objects as go
import plotly.io as pio

LAYOUT = {
    # Fonts
    'title': {
        'font': {
            'family': 'HelveticaNeue-CondensedBold, Helvetica, Sans-serif',
            'size': 30,
            'color': '#fff'
        }
    },
    'font': {
        'family': 'Helvetica Neue, Helvetica, Sans-serif',
        'size': 24,
        'color': '#fff'
    },

    'coloraxis': {'colorbar': {'outlinewidth': 0, 'ticks': ''}},

    # Colorways
    'colorway': ['#4872FD', '#FFD538'],

    'shapedefaults': {'line': {'color': '#2a3f5f'}},

    # Keep adding others as needed below
    # 'hovermode': 'x unified',

    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',

    'xaxis': {'automargin': True,
              'gridcolor': 'rgba(255, 255, 255, 0.2)',
              'linecolor': 'rgba(255, 255, 255, 0.2)',
              'ticks': '',
              'title': {'standoff': 15},
              'zerolinecolor': 'rgba(255, 255, 255, 0.2)',
              'zerolinewidth': 2},
    'yaxis': {'automargin': True,
              'gridcolor': 'rgba(255, 255, 255, 0.2)',
              'linecolor': 'rgba(255, 255, 255, 0.2)',
              'ticks': '',
              'title': {'standoff': 15},
              'zerolinecolor': 'rgba(255, 255, 255, 0.2)',
              'zerolinewidth': 2}
}
DATA = {
    # Each graph object must be in a tuple or list for each trace
    'bar': [
        go.Bar(
            texttemplate='%{value:.2s}',
            textposition='outside',
            textfont={
                'family': 'Helvetica Neue, Helvetica, Sans-serif',
                'size': 20,
                'color': '#FFFFFF'
            }
        )
    ]
}

pio.templates["dark-theme"] = go.layout.Template(
    # LAYOUT
    layout=LAYOUT,
    # DATA
    data=DATA,
)

pio.templates["dark-theme2"] = go.layout.Template(
    # LAYOUT
    layout=LAYOUT | {"font": (LAYOUT["font"] | {"size": 15})},
    # DATA
    data=DATA,
)
