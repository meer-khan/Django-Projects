''' Copyright (C) 2022 by SeQuenX  - All Rights Reserved

* This file is part of the ComplyVantage product development,

* and is released under the "Commercial License Agreement".

*

* You should have received a copy of the Commercial License Agreement license with

* this file. If not, please write to: legal@sequenx.com, or visit www.sequenx.com

'''



import pathlib #Python Default
from zipfile import ZipFile #Python Default
import os #Python Default
import pandas as pd
from guesslang import Guess, GuesslangError
from guesslang.model import DATASET
import time
import datetime 


    
def language_detection(code,file_extension, guess):
    # print("Guess langugae initiated...")
    prediction = guess.language_name(code)
    # print(prediction)
    prediction = prediction.lower()
    language = ''
    if (prediction == "groovy" or prediction == "kotlin" ) and file_extension == ".java":
        language = "Java"
    elif prediction == "java" and file_extension == "groovy":
        language = "Groovy"
    elif prediction == "haskel" and file_extension == ".py":
        language = "Python"
    elif prediction == "typescript" and file_extension == ".js":
        language = "JavaScript"
    elif prediction == "javascript" and file_extension == ".ts":
        language = "TypeScript"
    elif prediction == "coffeescript" and file_extension == ".js":
        language = "JavaScript"
    elif prediction == "coffeescript" and file_extension == ".ts":
        language = "TypeScript"
    elif prediction == "c" and file_extension in ['.cpp' , '.c++' , '.cplusplus']:
        language = "C++"
    elif prediction == "c++" and file_extension == ".c":
        language = "C"
    elif file_extension == '.gradle':
        language = "Gradle File"
    elif file_extension == '.jar':
        language = "Jar File"
    elif  file_extension == ".json":
        language = "Json File"
    elif prediction == "ini" and file_extension == ".txt":
        language = "Text File"
    elif file_extension.lower() in ['.png' , '.jpg' , '.jpeg' , '.tif' , '.tiff' , '.bmp' , '.JPG' , '.JPEG' , '.PNG' , 
    '.gif' , '.eps' , '.raw' , '.cr2' , '.nef' , '.orf' , '.sr2']:
        language = "Image File"
    elif file_extension == ".bin":
        language = "Bin File"
    else: 
        language = prediction.title()
    return language

def is_file_empty(file_path,content):
    # if elif else 
    return False if os.stat(file_path).st_size == 0 and os.path.getsize(file_path) == 0 else (False if len(content) <= 30 else True)

def parsing_all_files_and_folders(extractedFilesDirectory):
    fileNamesNPaths = [{"path":os.path.join(root,filename), "fileName":filename} for root,dirs,files in os.walk(extractedFilesDirectory) for filename in files]
    return fileNamesNPaths


def modified_get_file_and_check_extension(filePath): 
    fileExtension = pathlib.Path(filePath).suffix
    with open(filePath, "r" , encoding = "utf-8", errors = "ignore") as f: 
        code = f.read()
    return code, fileExtension




# TODO: Need to test and implement during optimizations
def modified_checking_extension_langagues_of_all_files(fileData, guess):
    supportedProgrammingLanguages = ['.py' , '.java' , '.kt' , '.cpp' , '.c++' , '.cp' , '.js' , '._js' , 
    '.cs' , '.c' , '.go' , '.r' , '.swift' , '.php' , '.php3' , '.php4' , '.php5' , '.dart' , 
    '.kt' , '.pl' , '.plx' , '.rb' , '.rs' , '.scala' , '.html' , '.css' , '.net' , 
    '.sqlite3' , '.m' , '.groovy' , '.mkd' , '.sql' , '.mysql' , '.hs' , '.ts' , '.jl' , '.scss', ".lua" , ".json", ".rs"
    ]
    language = None
    # uniqueLanguages= set()
    code , fileExtension = modified_get_file_and_check_extension(fileData["path"])
    isSupported = fileExtension in supportedProgrammingLanguages
    isCode = is_file_empty(fileData["path"],code)
    if isCode: 
        language = language_detection(code,fileExtension,guess)
        # uniqueLanguages.add(language.title())
        fileData.update({"language":language, "extension":fileExtension,"isSupported": isSupported, "isCode": isCode})
        return fileData
    
    else: 
        fileData.update({"language":language, "extension":fileExtension,"isSupported": isSupported, "isCode": isCode})
        return fileData



guess = Guess()
startTime = time.time()
parsingResult = parsing_all_files_and_folders(r"D:\CVtoPUSH\Github\GitHubPOC\Test Cases\hybridTest")
print("Results of parsing:\n", )
print(parsingResult)


print("Results of checking extensions:\n")
results = list(map(modified_checking_extension_langagues_of_all_files,parsingResult))
# results = [modified_checking_extension_langagues_of_all_files(data,guess) for data in parsingResult]
print(results)
print(len(results))
endTime = time.time()
print(endTime - startTime)