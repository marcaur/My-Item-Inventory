#!/usr/bin/python3

"""
Input data from inventory on file, mainly books and VHS tapes 
Create methods to add/read items from CSV 


Info
1) Title
2) Type (VHS/Book)

Class Methods:
- only accessible from class level 

@classmethod
def CheckInventory.create_new_csv(cls, file_name)

@classmethod 
def CheckInventory.add_to_csv(cls, file_name)

@classmethod 
def CheckInventory.read_csv(cls, file_name)

Static Methods do not send the object as a parameter
- Used within class, but does not need an instance
- Can be used a 'common' function with no relationship to instance 




"""

import csv, pprint, sys 

class CheckInventory:
    # show all the instances

    all_instances = []


    file_name = "new_items2022.csv"

    # this executes every time an instance is created 
    def __init__(self,item_type:str, item_name:str):
        self.self = self 
        self.item_name = item_name 
        self.item_type = item_type 

        # this line appends a copy of the instance to a list containing all instances
        CheckInventory.all_instances.append(self)



    def __repr__(self):
        return f"CheckInventory({self.item_name},{self.item_type})"
        


    def new_item(self, file_name):

        inventory_item = {
            "Type": [],
            "Title": [],
            }

        with open(file_name,'w',newline='') as inventory_file:
            write_items = csv.DictWriter(file_name, ['Type','Title'])
            write_items.writeheader()
            inventory_item["Type"].append(self.item_type)
            inventory_item["Title"].append(self.item_name)

            # write a new row 
            write_items.writerow(inventory_item)

    def add_item(self, file_name):

        inventory_item = {
            "Type": [],
            "Title": [],
            }

        with open(file_name,'a',newline='') as inventory_file:
            write_items = csv.DictWriter(inventory_file, ['Type','Title','Author'])
            inventory_item['Type'].append(self.item_type)
            inventory_item['Title'].append(self.item_name)


            write_items.writerow(inventory_item)


    # show_flips = list(zip(my_item["Type"],my_item["Title"]))


my_check = CheckInventory("book","first").add_item('new_items2022.csv')


print(CheckInventory.all_instances)


