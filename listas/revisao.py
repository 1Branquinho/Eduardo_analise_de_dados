#1
my_list = [10, 20, 30]
print(type(my_list))

#2  
names = ["Alice", "Bob", "Charlie"]
first = names[0]
print(first)

#3
my_data = {"id": 1, "status": "active"}
print(type(my_data))
#4
user = {"name": "Eduardo", "age": 20}
name_value = user["name"]
print(name_value)
#5
collection = [
    {"product": "A", "price": 10},
    {"product": "B", "price": 20}
]
print(type(collection))
print(type(collection[0]))
#6
import pandas as pd

data = [{"name": "Eduardo"}, {"name": "Ana"}]
df = pd.DataFrame(data)
print(df)
#7
import pandas as pd

df = pd.read_csv("my_file.csv")
#8
import pandas as pd

df = pd.read_excel("my_data.xlsx")
#9
import pandas as pd

df = pd.DataFrame({"age": [15, 25, 35]})
high_age = df[df["age"] > 18]

#10
import pandas as pd

df = pd.DataFrame({"city": ["SP", "RJ", "SP"]})
filter_sp = df[df["city"] == "SP"]

#11
import pandas as pd

df = pd.DataFrame({"age": [20, 30, 40], "city": ["SP", "SP", "RJ"]})
final_df = df[(df["age"] > 25) & (df["city"] == "SP")]