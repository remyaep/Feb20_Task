
import os
class packageClass:
    def __init__(self,location):
        self.location = location

        
    def get_txt_files(self):
        """ this function returns the list of all all the txt file from the input location """     

        try:
            file_names=[]
            for file in os.listdir(self.location):  
                if file.endswith((".txt",".csv")):
                    file_names.append(file) #Adding all the txt/csv files to the empty list
            return file_names        
                      
        except Exception as e:
            return e
        except FileNotFoundError as f:
            return f

        
   
    def get_list_of_data(self,data):
        """This function is used to get the all the words from the file in list format. Finally it will sort the list of words and return it"""
        list_of_data=[]
        for i in data:
            list_of_data.append(i[0])
        
        list_of_data = sorted(list_of_data)
        return list_of_data
    
    def get_distinct_data(self,list_of_data):
        """This function is used to get the all the unique words from the file in list format. Finally it will sort the list of unique words and return it"""
        distinct_data = list(set(list_of_data))
        distinct_data = sorted(distinct_data)
        return distinct_data
    
    def get_count_of_words(self,list_of_data,distinct_data):
        """This function is used to find the count of each word. Count will be stored in list format and it wil be returned"""
        count_of_words = []
        for i in sorted(distinct_data):
            count_of_words.append(list_of_data.count(i))
        return count_of_words