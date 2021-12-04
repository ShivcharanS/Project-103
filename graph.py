import pandas as pd

import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.line(df, x="Date", y="Number of cases", color="Country", title='Covid-19 cases')

fig.show()
