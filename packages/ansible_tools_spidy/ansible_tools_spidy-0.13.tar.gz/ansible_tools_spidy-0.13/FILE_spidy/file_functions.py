import json
import sys
import yaml
import pprint
from termcolor import colored
import constrains_spidy.contrain_checker as constrains

sys.path.append("../")

"""
Dependencies of the Library: 

git clone https://github.com/ahupp/python-magic
pip3.5 install libmagic 
brew install libmagic 
pip3.5 termcolor 


Metadata of Library 

file_name = self explanatory 
file_path = self explanatory 

"""

class file_functions:

       def __init__(self,baseline={}):
           self.__baseline__ = baseline

           ### Metadata Constrain Checks
           metadata_headers = ["file_name", "file_loc"]
           constrain_check = constrains.constrain_check()
           constrain_check.metadata_checks(self.__baseline__,metadata_headers)

           ### File Path Exists Constrain Check
           constrain_check.check_file_exists(self.__baseline__["file_loc"])

##############################    JSON File Handling ######################################

       def get_json(self):

           ### File Exists
           constrain_check = constrains.constrain_check()
           constrain_check.check_file_exists(self.__baseline__["file_loc"] + "/" + self.__baseline__["file_name"])

           ### File Type Check
           constrain_check.check_file_type(self.__baseline__["file_loc"] + "/" + self.__baseline__["file_name"],"text/plain")

           ### Read from json file and return a dictionary
           try:
                with open(self.__baseline__["file_loc"] + "/" + self.__baseline__["file_name"], 'r') as json_file:
                     json_string = json.load(json_file)
                return json_string

           except ValueError:
                 print(colored("JSON Decoding Problem Check " + self.__baseline__["file_name"] + " for Formatting Issues",'blue',attrs=['reverse', 'blink']))
                 print()
                 sys.exit(1)

       def write_json(self,json_obj=None):

           #### Check if the Json Object is passed as parameter
           if(json_obj == None):
              print(colored("Kindly pass the Json Object as Parameter to the Function",'blue',attrs=['reverse', 'blink']))
              sys.exit(1)

           try:
                with open(self.__baseline__["file_loc"] + "/" + self.__baseline__["file_name"], 'w') as json_file:
                     json.dump(json_obj,json_file)

           except PermissionError:
               print(colored("Kindly Fix Permissions issue for " + self.__baseline__["file_loc"] + " before proceeding" , 'blue',attrs=['reverse', 'blink']))
               sys.exit(1)

#######################################  Yaml File Handling ##################################

       def get_yaml(self):

           ### File Exists
           constrain_check = constrains.constrain_check()
           constrain_check.check_file_exists(self.__baseline__["file_loc"] + "/" + self.__baseline__["file_name"])

           ### File Type
           constrain_check.check_file_type(self.__baseline__["file_loc"] + "/" + self.__baseline__["file_name"],"text/plain")

           ### Read from Yaml file and return Dict
           try:
                with open(self.__baseline__["file_loc"] + "/" + self.__baseline__["file_name"], 'r') as yaml_file:
                     yaml_string = yaml.load(yaml_file)

                return yaml_string

           except ValueError:
                 print(colored("YAML Decoding Problem Check " + self.__baseline__["file_name"] + " for Formatting Issues",'blue',attrs=['reverse', 'blink']))
                 print()
                 sys.exit(1)

       def write_yaml(self,yaml_obj=None):

           #### Check if the Json Object is passed as parameter
           if(yaml_obj == None):
              print(colored("Kindly pass the Yaml Object as Parameter to the Function",'blue',attrs=['reverse', 'blink']))
              sys.exit(1)

           try:
                with open(self.__baseline__["file_loc"] + "/" + self.__baseline__["file_name"], 'w') as yaml_file:
                     yaml.dump(yaml_obj,yaml_file)

           except PermissionError:
               print(colored("Kindly Fix Permissions issue for " + self.__baseline__["file_loc"] + " before proceeding" , 'blue',attrs=['reverse', 'blink']))
               sys.exit(1)

       def file_encrypt(self,public_key):
           pass
       def file_decrypt(self,private_key):
           pass
