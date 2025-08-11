import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
import joblib

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"
cols = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
df = pd.read_csv(url, names=cols)

for col in df.columns:
    df[col] = df[col].astype('category').cat.codes

X = df.drop("class", axis=1)
y = df["class"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = CategoricalNB()
model.fit(X_train, y_train)

joblib.dump(model, 'car_evaluation_naive_bayes_model.pkl')
