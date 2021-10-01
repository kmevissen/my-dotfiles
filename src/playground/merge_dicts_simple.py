import ast

dict_1 = {"dag_name": "1",
          "execution_date": "2021-09-10"}

dict_2 = {"custom_label": "blabla",
          "description": "this is a bit of a description"}

dict_3 = {"action": "overwriting dag name",
          "new value": "will be 3",
          "dag_name": "3"}

print(dict(dict_1, **dict_2))

print(dict(dict_1, **dict_2, **dict_3))

tags = ["some random value", "2", "blabla"]


# t = { "tag " + tag : tag for tag in tags}
t = { "Tag " + str(i + 1) : tags[i] for i in range(0, len(tags) ) } if tags is not None else {}


print(tags)
print(", ".join(tags))
print(t)



b = "['var1','var2']"
c = ast.literal_eval(b)
print(c)