import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load dataset
df = pd.read_csv("final_airbnb_hotel_dataset.csv")

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Airbnb Growth vs Hotel Industry Wages Across Major U.S. Cities (2014–2023)",
        style={"textAlign": "center"}
    ),

    dcc.Dropdown(
        id="city_dropdown",
        options=[{"label": c, "value": c} for c in df["city"].unique()],
        value="Chicago",
        clearable=False
    ),

    dcc.Graph(id="trend_graph")

])


@app.callback(
    Output("trend_graph", "figure"),
    Input("city_dropdown", "value")
)

def update_graph(selected_city):

    filtered = df[df["city"] == selected_city]

    fig = px.line(
        filtered,
        x="year",
        y=["airbnb_listings", "hotel_wages_millions"],
        markers=True
    )

    fig.update_layout(
        title=f"{selected_city}: Airbnb Listings vs Hotel Wages",
        yaxis_title="Listings/Wages(Million USD)"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)