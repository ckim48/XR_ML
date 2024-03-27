import pandas as pd
import plotly.graph_objs as go

data = pd.read_csv("consulting_data_content_logic.csv")

print(data.info())
print(data.head(10))

data_male = data[data["gender"] == "Male"]
data_female = data[data["gender"] == "Female"]

print("Average Sentiment for Male: ", data_male["sentiment"].mean())
print("Average Sentiment for Female: ", data_female["sentiment"].mean())

print("Type of Conulsting\n", data["type_of_consulting"].unique())
print("Type of content\n", data["consulting_content"].unique())
print("Type of consultants\n", data["the_consultant"].unique())

consulting_counts = data["type_of_consulting"].value_counts()

print(consulting_counts)

consulting_df = consulting_counts.reset_index()
consulting_df.columns = ["Type of Consulting","Count"]

colors = ["#79A7DF", "#79DF8F", "#DFB279", "#DF8879", "#8B79DF", "#DF79DA"]

######  Pie chart for the number of type of consulting  #######
# fig = go.Figure(data=[go.Pie(labels=consulting_df["Type of Consulting"], values=consulting_df["Count"],
#                               marker=dict(colors=colors))])
# fig.update_layout(title='Number of Each Type of Consulting')
# fig.show()
# print(data["age"])
# age_histogram = go.Histogram(x=data["age"], nbinsx=10)
# age_layout = go.Layout(title="Age Distribution")
# age_fig = go.Figure(data=[age_histogram], layout=age_layout)
# age_fig.show()

age_groups = pd.cut(data["age"], bins=[0,20,30,40,50,60,70], labels = ["0-20","21-30","31-40","41-50","51-60","61-70"])
age_group_counts = age_groups.value_counts()
#print(age_group_counts)
fig = go.Figure(data=[go.Pie(labels=age_group_counts.index, values=age_group_counts.values)])
fig.update_layout(title="Age Group Distribution")

fig.show()