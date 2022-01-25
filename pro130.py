from os import startfile
import pandas as pd
import csv

df = pd.read_csv("final_data.csv")

del df["Distance"]
del df["Mass"]
del df["Radius"]
del df["D_Distance"]
del df["D_Mass"]
del df["D_Radius"]
del df["Dwarf_name"]
del df["Star_name"]

df = df.rename({
                'Distance': "main_distance", 
                'Mass': "main_mass", 
                'Radius': "main_Radius",
                'D_Distance': "main_distance", 
                'D_Mass': "main_mass", 
                'D_Radius': "main_Radius",  
                'Dwarf_name': "Name"
                'Star_name': "Name"
            }, axis='columns')

df.to_csv('final_data.csv')