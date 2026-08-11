import pandas as pd

data = {"Name":["Promise", "Daniel", "Timi", "Eddie", "Muna"],
        "Age": ["30", "22", "19", "23", "21"]}

df = pd.DataFrame(data, index= ["Galaxy employee 1", "Galaxy employee 2", "Galaxy employee 3", "Galaxy employee 4", "Galaxy employee 5"])


#Add column 
df["Job Description"]= ["Supervisor", "Engineer", "Boy boy", "Daddy's boy", "Ladies man"]

print(df)

#Add a row
new_row = pd.DataFrame([{"Name":"Mele", "Age": "22", "Job Description": "Gym guy"},
                        {"Name":"Jess", "Age": "20", "Job Description": "Mummy's boy"}], index=["Galaxy employee 6","Galaxy employee 7"])

df= pd.concat([df,new_row])

print(df)