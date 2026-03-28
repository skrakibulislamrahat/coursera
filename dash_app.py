import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("dataset_part_2.csv")
app = Dash(__name__)

app.layout = html.Div([
    html.H1("SpaceX Launch Dashboard"),
    dcc.Dropdown(
        id="site-dropdown",
        options=[{"label":"All Sites","value":"ALL"}] + [{"label":s,"value":s} for s in sorted(df["LaunchSite"].unique())],
        value="ALL"
    ),
    dcc.Graph(id="success-pie"),
    dcc.Graph(id="payload-scatter")
])

@app.callback(
    Output("success-pie","figure"),
    Output("payload-scatter","figure"),
    Input("site-dropdown","value")
)
def update(site):
    dff = df if site == "ALL" else df[df["LaunchSite"] == site]
    pie = px.pie(dff, names="LaunchSite" if site=="ALL" else "Class", title="Success Pie Chart")
    scatter = px.scatter(dff, x="PayloadMass", y="FlightNumber", color="Class", hover_data=["Orbit"])
    return pie, scatter

if __name__ == "__main__":
    app.run(debug=True)
