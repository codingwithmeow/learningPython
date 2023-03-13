import pandas as pd

# how to make data frame
s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1 ,oranges = s2)
dataframe = pd.DataFrame(data)
print(f"The dataframe = \n{dataframe}")

#example
data2 = [["student1",50],["student2",60],["student3",70],["student4",80]]
dataframe2 = pd.DataFrame(data2,columns= ['Name','Grade'],index=[1,2,3,4])
print(dataframe2)

dict ={"Name" : ["student1","student2","student3","student4"],"Grade" : [50,60,70,80]}
dataframe3 = pd.DataFrame(dict,index=["212","232","236","454"])  # index could be the student number like used in here
print(dataframe3)

dict_list = [
                {"Name":"student1","Grade":60},
                {"Name":"student2","Grade":40},
                {"Name":"student3","Grade":30},
                {"Name":"student4","Grade":90}
            ]
dataframe4 = pd.DataFrame(dict_list,index=[1,2,3,4])
print(dataframe4)







