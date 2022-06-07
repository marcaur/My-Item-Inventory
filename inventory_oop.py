#!/usr/bin/python3

"""
Input data from inventory on file, mainly books and VHS tapes 

Create methods to add/read items from CSV 

"""

import csv, pprint, sys 

class CheckInventory:
    # show all the instances

    all_instances = []

    

    # this executes every time an instance is created 
    def __init__(self,item_name:str, item_type:str, author:str, bk_year:int,bk_category:str, file_name:str):
        self.self = self 
        self.item_name = item_name 
        self.item_type = item_type 
        self.author = author 
        self.bk_year = bk_year 
        self.bk_category = bk_category
        self.file_name = file_name 

        # this line appends a copy of the instance to a list containing all instances
        CheckInventory.all_instances.append(self)



    def __repr__(self):
        return f"CheckInventory({self.item_name},{self.item_type})"
        


    def new_item(self):

        inventory_item = {
            "Type": [],
            "Title": [],
            "Author": [],
            "Year": [],
            "Category": []
            }

        with open(self.file_name,'w',newline='') as inventory_file:
            write_items = csv.DictWriter(self.file_name, ['Type','Title','Author','Year', 'Category'])
            write_items.writeheader()
            inventory_item["Type"].append(self.item_type)
            inventory_item["Title"].append(self.item_name)
            inventory_item["Author"].append(self.item_name)
            inventory_item["Year"].append(self.item_name)
            inventory_item["Category"].append(self.item_name)



            # write a new row 
            write_items.writerow(inventory_item)

    def add_item(self):

        inventory_item = {
            "Type": [],
            "Title": [],
            "Author": [],
            "Year": [],
            "Category": []
            }

        with open(self.file_name,'a',newline='') as inventory_file:
            write_items = csv.DictWriter(inventory_file, ['Type','Title','Author','Year', 'Category'])
            inventory_item['Type'].append(self.item_type)
            inventory_item['Title'].append(self.item_name)


            write_items.writerow(inventory_item)



my_check = CheckInventory("book","first").add_item('new_items2022.csv')


print(CheckInventory.all_instances)


