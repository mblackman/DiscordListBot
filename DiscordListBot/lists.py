import sys
import os
import json
import io

class listFile:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, string):
        if not string:
            return

        self.items.append(string)

    def remove_item(self, arg):
        if not arg:
            return false

        try:
            itemNum = int(arg)

            if itemNum >= len(self.items):
                return False

            self.items.pop(itemNum)
            return True

        except ValueError:
            if arg in self.items:
                self.items.remove(arg)
                return True
        
        return false

    def to_string(self, print_line_number = False):
        if not print_line_number:
            return '\n'.join(self.items)

        count = 0
        returnString = ""

        for item in self.items:
            returnString += str(str(count) + " " + item)

        return returnString

class notebook:
    def __init__(self, file_name = "lists", file_extension = "json", file_path = None):
        fileExtension = file_extension.replace('.', '')

        self.filePath = file_path
        self.fileName = file_name + fileExtension
        
        if not self.filePath is None:
            self.fileUri = os.path.join(self.filePath, self.fileName)
        else:
            self.fileUri = os.path.join(os.getcwd(), self.fileName)

        self.lists = []

    def add_to_list(self, list_name, new_line):
        addToList = get_list(self, list_name)

        if addToList == None:
            addToList = create_list(self, list_name)

        addToList.addItem(new_line)

    def create_list(self, list_name):
        if contains_list(list_name):
            return False

        self.lists.append(listFile(list_name))
        return True

    def get_list(self, list_name):
        for list in self.lists:
            if list.name == list_name:
                return list

        return None

    def remove_list(self, arg):
        try:
            itemNum = int(arg)

            if itemNum >= len(self.lists):
                return False

            self.lists.pop(itemNum)
            return True

        except ValueError:
            for list in self.lists:
                if list.name == list_name:
                    self.lists.remove(list)
                    return True

    def lists_as_string(self, show_numbers = True):
        returnString = ""
        count = 0

        for list in self.lists:
            if show_numbers:
                returnString += str(str(count), " ", list.name, '\n')
                count += 1
            else:
                returnString += str(list.name, '\n')

        return returnString

    def contains_list(self, list_name):
        for list in self.lists:
            if list.name == list_name:
                return True

        return False

