import pandas as pd
from dash import Dash, dcc, html, Output, Input
# Dash is the library for making web-based dashboard with python
# .query("type == 'conventional' and region=='Albany'")
data = (
    pd.read_csv("avocado.csv")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
        )
regions = data["region"].sort_values().unique()
# Create my web-based dashboard application
app = Dash(__name__)
app.layout = html.Div(
    children= [html.H1(children="Sample Dashboard", style={"color": "#D08F81", "fontSize": "50px"}),
               html.H2(children="This is sample site"),
               html.H1(children="Agian"),
               html.P(children="abcdefgeag"),
               dcc.Graph(
                   id="price-chart",
                   figure = {
                       "data": [
                           {
                               "x": data["Date"],
                               "y": data["AveragePrice"],
                               "type": "lines",
                           }
                       ],
                       "layout": {"title": "Average Price of Avocados in Albany", "colorway": ["#D05AED"]}
                   }
               ),
               dcc.Graph(
                   figure={
                       "data": [
                           {
                               "x": data["Date"],
                               "y": data["Total Volume"],
                               "type": "lines",
                           }
                       ],
                       "layout": {"title": "Volume"}
                   }
               ),
               html.Div(
                   children=[
                       dcc.Dropdown(
                            id="region-filter",
                            options=[
                                {"label":region,"value": region}
                                for region in regions
                           ],
                           value="Albany",
                           clearable=False,
                           className="dropdown",
                       )
                   ]
               )

               ]
)
@app.callback(
    Output("price-chart", "figure"),
    Input("region-filter", "value")
)
def update_charts(region):
    filtered_data = data.query("region == @region and type == 'conventional'")
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
            }
        ],
        "layout": {"title": "Average Price of Avocados", "colorway": ["#D05AED"]}
    }
    return price_chart_figure

# Run my web application
if __name__ == "__main__":
    app.run_server(debug=True)