#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Osama Abdelaal
# DATE CREATED: 08.11.2020                               
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames of the image 
    files. This is used to check the accuracy of the image classifier model.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by pretrained CNN models (string)
    Returns:
     petlabels_dic - Dictionary storing image filename (as key) and Pet Image
                     Labels (as value)  
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Processes each of the files to create a dictionary where the key
    # is the filename and the value is the picture label (below).
 
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()  
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):
       
       # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
       # isn't an pet image file
       if in_files[idx][0] != ".":
           
           # Creates temporary label variable to hold pet label name extracted 
           pet_label = ""
           #Iterate over each labels in file names and extract only the breed name
           # add it to Pet_label and split each word by ".'
           for i in in_files[idx].split("_"):
                if i.isalpha():
                    pet_label += i.lower()+"."
           # If filename doesn't already exist in dictionary add it and it's
           # pet label - otherwise print an error message because indicates 
           # duplicate files (filenames)
           if in_files[idx] not in results_dic:
               results_dic[in_files[idx]] = [pet_label]
              
           else:
               print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])
    # returns dictionary of labels
    return(results_dic)
