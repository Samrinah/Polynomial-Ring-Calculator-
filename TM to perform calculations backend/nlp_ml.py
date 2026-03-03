import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


X_train = [
    "add 3 and 5", "sum 12 and 7", "please add 13 and 6",
    "subtract 8 from 15", "minus 4 and 2", "subtract 20 by 5",
    "multiply 5 and 6", "times 7 and 3", "multiply 10 by 2",
    "divide 10 by 2", "divide 100 by 25", "quotient of 20 and 4"
]

y_train = [
    "ADD", "ADD", "ADD",
    "SUB", "SUB", "SUB",
    "MUL", "MUL", "MUL",
    "DIV", "DIV", "DIV"
]


vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
clf = MultinomialNB()
clf.fit(X_train_vec, y_train)


def nlp_parse_ml(text):
    x_vec = vectorizer.transform([text])
    op = clf.predict(x_vec)[0]
    nums = re.findall(r'\d+', text)
    is_binary = all(set(n) <= {'0','1'} for n in nums)
    return op, nums, is_binary
