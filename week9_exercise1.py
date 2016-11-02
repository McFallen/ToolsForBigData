import json
import re
from sklearn import ensemble, metrics
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import CountVectorizer

def valid_entries(filenumber):
    articles = []
    if filenumber < 10:
        filenumber = "0" + str(filenumber)

    with open("input/reuters-0" +  str(filenumber) + ".json") as json_data: data = json.load(json_data)

    for entry in data:
        if 'body' in entry and 'topics' in entry:
            articles.append(entry)

    return articles

def valid_articles(n): return reduce(lambda x, y: x + valid_entries(y), range(n), [])

def bag_of_words(articles):
    bodies = map(lambda x: x['body'], articles)
    earns = map(lambda x: 1 if 'earn' in x['topics'] else 0, articles)
    bow = CountVectorizer()
    return (earns, bow.fit_transform(bodies).toarray())

def bag_of_words_feature_hash(articles):
    bodies = map(lambda x: (x['body']), articles)
    earns = map(lambda x: 1 if 'earn' in x['topics'] else 0, articles)
    bow = HashingVectorizer(n_features=1000)
    return (earns, bow.fit_transform(bodies).toarray())

def tree_estimator(bow, train=0.8):
    clf = ensemble.RandomForestClassifier(n_estimators=50)
    body_vec = bow[1]
    topics_vec = bow[0]

    split_int = int((round(float(len(body_vec)) * train)))

    x_train, x_test = body_vec[:split_int], body_vec[-split_int:]
    y_train, y_test = topics_vec[:split_int], topics_vec[-split_int:]
    
    clf.fit(x_train, y_train)

    pred = clf.predict(x_test)
    
    score = metrics.accuracy_score(y_test, pred)

    return score

if __name__ == "__main__":
    all_articles = valid_articles(10)

    print "Amount of valid articals:", len(all_articles)

    bow = bag_of_words(all_articles[:5000])
    print tree_estimator(bow)

    feat_hash = bag_of_words_feature_hash(all_articles)
    print tree_estimator(feat_hash)