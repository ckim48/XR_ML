import pandas as pd
import plotly.graph_objs as go
from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc

data = pd.read_csv("static/data/consulting_data_content_logic.csv")

data_male = data[data["gender"] == "Male"]
data_female = data[data["gender"] == "Female"]
# fig.show()
# print(data["age"])
# age_histogram = go.Histogram(x=data["age"], nbinsx=10)
# age_layout = go.Layout(title="Age Distribution")
# age_fig = go.Figure(data=[age_histogram], layout=age_layout)
# age_fig.show()
def generate_consult(data, consultant):
    data_consult = data[data["the_consultant"] == consultant]
    consulting_counts = data_consult["type_of_consulting"].value_counts()
    consulting_df = consulting_counts.reset_index()
    consulting_df.columns = ["Type of Consulting", "Count"]
    colors = ["#79A7DF", "#79DF8F", "#DFB279", "#DF8879", "#8B79DF", "#DF79DA"]
    ######  Pie chart for the number of type of consulting  #######
    fig_consult = go.Figure(data=[go.Pie(labels=consulting_df["Type of Consulting"], values=consulting_df["Count"],
                                         marker=dict(colors=colors))])
    fig_consult.update_layout(title='Number of Each Type of Consulting')
    return fig_consult

def generate_age(data, consultant):
    data_consult = data[data["the_consultant"] == consultant]
    age_groups = pd.cut(data_consult["age"], bins=[0, 20, 30, 40, 50, 60, 70],
                        labels=["0-20", "21-30", "31-40", "41-50", "51-60", "61-70"])
    age_group_counts = age_groups.value_counts()
    fig = go.Figure(data=[go.Pie(labels=age_group_counts.index, values=age_group_counts.values)])
    fig.update_layout(title="Age Group Distribution", paper_bgcolor="#F1FCF3")

    return fig


colors = ["#F9AD9C","#F9DD9C","#DCF99C","#9CF9D9","#BB9CF9","#F99CF4"]
def generate_sentiment_score_chart(data, consultant):
    data_consult = data[data["the_consultant"] == consultant]
    sentiment_scores = data_consult.groupby('type_of_consulting')["sentiment"].mean().reset_index()
    fig_sentiment = go.Figure(data=[
        go.Bar(
            x = sentiment_scores["type_of_consulting"],
            y = sentiment_scores["sentiment"],
            marker_color= colors[:len(sentiment_scores)]
        )
    ])
    fig_sentiment.update_layout(
        title="Average Sentiment by Type of Consulting",
        xaxis_title="Type of Consulting",
        yaxis_title="Average Sentiment Score",
    )
    return fig_sentiment
def generate_sentiment_by_gender(data, consultant):
    data_consult = data[data["the_consultant"] == consultant]
    sentiment_scores = data_consult.groupby('gender')["sentiment"].mean().reset_index()
    fig_sentiment = go.Figure(data=[
        go.Bar(
            x = sentiment_scores["gender"],
            y = sentiment_scores["sentiment"],
            marker_color= colors[:len(sentiment_scores)]
        )
    ])
    fig_sentiment.update_layout(
        title="Average Sentiment by Gender",
        xaxis_title="Gender",
        yaxis_title="Average Sentiment Score",
    )
    return fig_sentiment


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP,
                                           "https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,opsz,wght@0,6..12,200..1000;1,6..12,200..1000&family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap"
                                           ])

app.layout = html.Div([ dbc.Container(children=[
    html.H1("Sample Title", className="text-center mb-5", style={"color": "#11942F", "fontFamily": "Playfair Display"}),
    html.P("Description about this page...", className="text-center mb-5", style={"color": "#11942F", "fontFamily": "Playfair Display"} ),
    dcc.Dropdown(
        id="chart-selector",
        options=["AI", "Human"],
        value="Human",
        className="mb-4",
        style={"width":"35%"}
    ),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H4("First Chart", className="card-title text-center", style={"fontSize": "30px"}), style={"backgroundColor": "#F1FCF3", "color": "#11942F"}),
                dbc.CardBody([
                    dcc.Graph(
                        id="age-distribution",
                        figure=generate_age(data,"Human")
                    )
                ])
            ], className="shadow",style={"border": "3px dotted black", "backgroundColor": "#F1FCF3"})
        ], width=12, lg=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H4("Second Chart", className="card-title")),
                dbc.CardBody([
                    dcc.Graph(
                        id="consult-distribution",
                        figure=generate_consult(data,"Human")
                    )
                ])
            ], className="shadow mt-4 mt-lg-0")
        ], width=12, lg=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H4("Third Chart", className="card-title text-center", style={"fontSize": "30px"}),
                               style={"backgroundColor": "#F1FCF3", "color": "#11942F"}),
                dbc.CardBody([
                    dcc.Graph(
                        id="sentiment-chart",
                        figure=generate_sentiment_score_chart(data,"Human")
                    )
                ])
            ], className="shadow mt-4 mt-lg-5", style={"border": "2px solid #74CA87"})
        ], width=12, lg=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H4("Fourth Chart", className="card-title text-center", style={"fontSize": "30px"}),
                               style={"backgroundColor": "#F1FCF3", "color": "#11942F"}),
                dbc.CardBody([
                    dcc.Graph(
                        id="sentiment-gender-chart",
                        figure=generate_sentiment_by_gender(data, "Human")
                    )
                ])
            ], className="shadow mt-4 mt-lg-5", style={"border": "2px solid #74CA87"})
        ], width=12, lg=6),
    ]),

])
], style={"background-color": "#74CA87"})

@app.callback(
    [Output("consult-distribution", "figure"), Output("age-distribution", "figure"), Output("sentiment-chart", "figure"), Output("sentiment-gender-chart", "figure")],
    [Input("chart-selector", "value")]
)
def update_chart(consult_type):
    if consult_type == "AI":
        fig_consult = generate_consult(data,"AI")
        fig_age = generate_age(data,"AI")
        fig_sentiment = generate_sentiment_score_chart(data,"AI")
        fig_sentiment_gender = generate_sentiment_by_gender(data, "AI")

        return fig_consult, fig_age, fig_sentiment, fig_sentiment_gender
    else:
        fig_consult = generate_consult(data,"Human")
        fig_age = generate_age(data,"Human")
        fig_sentiment = generate_sentiment_score_chart(data,"Human")
        fig_sentiment_gender = generate_sentiment_by_gender(data, "Human")

        return fig_consult, fig_age, fig_sentiment, fig_sentiment_gender


if __name__ == '__main__':
    app.run_server(debug=True)