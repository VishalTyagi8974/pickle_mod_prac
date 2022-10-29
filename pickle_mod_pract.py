import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
print(data)

textfile=open("textfile_iris.txt","wt")
textfile.write(data)
textfile.close()

with open("textfile_iris.txt") as f:
    data_list= f.readlines()

pickled_data= "pickled_iris.pkl"
file= open(pickled_data, "wb")

pickle.dump(data_list, file)
file.close()

with open("pickled_iris.pkl", "rb") as fi:
    iris= pickle.load(fi)
    print(iris)