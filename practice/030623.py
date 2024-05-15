import pandas
from main_back import lowercase, tokenization, remove_punctuation, remove_stopwords,lst_to_string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

data = pandas.read_csv("McDonald_s_Reviews.csv", encoding='ISO-8859-1')
#print(data)
print(data.info())
# Remove Missing Values
# remove rows where either 'review' or 'rating' column has null value
cleaned_data = data.dropna(subset=["review","rating"])
print(cleaned_data.info())

print(cleaned_data["review"])
print(cleaned_data["rating"])

cleaned_data["rating"] = cleaned_data["rating"].str.replace(' stars?','',regex=True).astype(int)
print(cleaned_data.info())
# "        My name is Scott.            "
# "My name is Scott."
cleaned_data["review"] = cleaned_data["review"].str.strip()
pattern = r"^[A-Za-z0-9\s\.,;:!?\"\'-]+$"
cleaned_data = cleaned_data[cleaned_data["review"].str.match(pattern,case=False)]
print(cleaned_data["review"])
print(cleaned_data.info())
cleaned_data["review"]  = cleaned_data["review"].apply(lowercase)
cleaned_data["review"]  = cleaned_data["review"].apply(tokenization)
cleaned_data["review"]  = cleaned_data["review"].apply(remove_punctuation)
cleaned_data["review"]  = cleaned_data["review"].apply(remove_stopwords)
cleaned_data["review"]  = cleaned_data["review"].apply(lst_to_string)
print(cleaned_data["review"])

X = cleaned_data["review"]
y = cleaned_data["rating"]

# 1. Train: 80%
#    - Train_X
#    - Train_y
# 2. Test: 20 %
#    - Test_X
#    - Test_y
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train)
print(y_train)

# Change X(text) in to vectors and define a machine learning algorithm
model = make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=1000))
# Train
model.fit(X_train, y_train)
# Test
y_pred = model.predict(X_test)
print(X_test)
print(y_pred)
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy)
print("Done!")