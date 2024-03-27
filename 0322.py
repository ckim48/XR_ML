import pandas # pandas is the open-source library for data analysis
import json
from dash import Dash, html, dcc# open source library for building web analytical applications
import plotly.express as px
from dash.dependencies import Input,Output

data_file = "localization.json"
with open(data_file,'r') as file:
    data = json.load(file)
df = pandas.DataFrame(data['Sheet1'])

app = Dash(__name__)
app.layout = html.Div(
    children = [
        html.H1(children="Sample Dashboard", style={"color":"red"}),
        html.H2(children="Logncoding Capstone"),
        html.P(children="This is for practicing data analysis"),
        dcc.Graph(
            id = "subscription-plan-graph"
        ),
        dcc.Dropdown(
            id = 'age-dropdown',
            options = [{'label':age, 'value':age} for age in df['Age'].unique()],
            value ='20-35',
            clearable=False
        ),
        dcc.Dropdown(
            id = "chart-type-dropdown",
            options = [
                {'label': 'Bar Chart - Spotify Subscription Plan', 'value': 'bar-subscription'},
                {'label': 'Pie Chart - Gender Distribution', 'value': 'pie-gender'},
            ],
            value = "bar-subscription",
            clearable = False
        )
    ]
)
@app.callback(
    Output('subscription-plan-graph', 'figure'),
    [Input('chart-type-dropdown', 'value'), Input('age-dropdown', 'value')]
)
def update_figure(selected_chart, selected_age):
    filtered_df = df[df["Age"] == selected_age]
    if selected_chart == "bar-subscription":
        fig = px.bar(filtered_df, x="spotify_subscription_plan")
        print("CHAT")
    else:
        fig = px.pie(filtered_df, names="Gender")
        print("ABC")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)