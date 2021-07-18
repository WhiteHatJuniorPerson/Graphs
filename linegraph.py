import pandas as pd 
import plotly.express as px

df = pd.read_csv("data.csv")
graph = px.line(df,x="date",y="cases",color="country")
graph.show()