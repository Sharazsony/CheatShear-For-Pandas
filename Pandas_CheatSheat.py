                         """pandas Library"""
#cleaning Data process                         
                         
#how to make dataframe 
"""
import pandas as pd
Employ={"Name":["a","b"],"Age":[1,2]}
df=pd.DataFrame(Employ)
print(df)
"""

#Read excel file in panda
"""
import pandas as pd
#read excel file and convert it into DataFrame
Data=pd.read_excel("/file_example_XLS_10.xls")
df=pd.DataFrame(Data)
print(df)
"""
#    Analysis Data 

#how to check data types and count
"""print(df.info())"""

#statics terms
"""print(df.describe())"""

#    Data Cleaning
#find how many values are null
"""print(df.isnull().sum())"""

#dupplicate you check column wise
"""print(df["First Name"].duplicated())"""
#remove duplicate specific column
"""Without= df.drop_duplicates("Id")"""
#to drop all null
"""df.dropna()"""
#replace
"""df['First Name']=df['First Name'].replace('Dulce', 'sharaz')"""
#to find avg(mean)
"""print(df["Age"].mean())"""

#to fill null values with forward / back values
"""df.fillna(method="bfill")""" #method=ffill

#    Data Tranformation
"""
df.loc[(df["Age"]>40),"Age Limit"]="Above 40"
df.loc[(df["Age"]<40),"Age Limit"]="Less 40"
print(df)
"""
#count how many person age less than 40
"""
print("Count of less than 40 :   ",(df["Age Limit"]=="Less 40").sum())
"""
#if I want to combine first and second name then simply
"""
df["Full Name"]=df["First Name"]+" "+df["Last Name"]
"""
#usage of Group by
"""
print(df.groupby("Country").agg({"Id":"count"})
"""
"""
print(df.groupby(["Country","Gender"]).agg({"Id":"count"}))
"""
#    Join to DataFrame
#using merge
""""
import pandas as pad
Data1={"rol":[1,2,3],"name":["sharaz","rehan","numan"]}
Data2={"rol":[1,4,3],"city":["fsd","lhr","Multan"]}
D1=pad.DataFrame(Data1)
D2=pad.DataFrame(Data2)


print(pad.merge(D1,D2,on="rol"))
print("\t........")
print(pad.merge(D1,D2,on="rol",how="left"))
"""
#concat
"""
print(pad.concat([D1,D2]))
"""
#output
"""
 rol    name    city
0    1  sharaz     NaN
1    2   rehan     NaN
2    3   numan     NaN
0    1     NaN     fsd
1    4     NaN     lhr
2    3     NaN  Multan
"""
#Make pivot
"""
import pandas as pd

# Create DataFrame
data = {
    "keys": ["k1", "k2", "k1", "k2"],
    "Names": ["John", "Ben", "David", "Peter"],
    "Houses": ["red", "blue", "green", "red"]
}

df = pd.DataFrame(data)

# Print original DataFrame
print(" Before :  \n",df)

# Use pivot_table to avoid errors due to duplicate entries
pivot_df = df.pivot(index="keys", columns="Names", values="Houses")

print("\n\n",pivot_df)
"""

#Output of pivot function
"""
Before :  
   keys  Names Houses
0   k1   John    red
1   k2    Ben   blue
2   k1  David  green
3   k2  Peter    red


 Names   Ben  David John Peter
keys                         
k1      NaN  green  red   NaN
k2     blue    NaN  NaN   red
"""
    