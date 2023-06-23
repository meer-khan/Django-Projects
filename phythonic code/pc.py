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


 
def making_new_DIR(fileDirectoryPath , filepath):
    

    if os.path.isdir(fileDirectoryPath):
        newDirPath = os.path.join(fileDirectoryPath, "ComplyVantage")
        fileName = pathlib.Path(filepath).stem
        newDirPathNamedasProject = os.path.join(newDirPath,fileName)

        if os.path.isdir(newDirPath):
            # NEW CODE

            if os.path.isdir(newDirPathNamedasProject):
                raise Exception(fileName+" folder name already exists")
            
            else:
                os.mkdir(newDirPathNamedasProject)
            
            return newDirPathNamedasProject,fileName
                    # END CODE
            # raise Exception("Directory already exists as ComplyVantage Name!")
            # return newDirPath

        else:
            os.mkdir(newDirPath)
            if os.path.isdir(newDirPathNamedasProject):
                raise Exception("Project folder name already exists")
            
            else:
                os.mkdir(newDirPathNamedasProject)
            return newDirPathNamedasProject,fileName
            # return newDirPath

# TODO: Need to test and implement during optimizations
def un_zipping_compressed_files(filePath, extractedDirPath = None):
    '''
    This function uncompresses the file
    Checks if given file name is valid, and then extracts its directory path then
    unzip the path, if user provided the directory path for extraction then it will 
    extract all the files there otherwise, extract all the files in the directory 
    where zipped file extists.
    it will create a new folder named as ComplyVantage and unzip all the files there 
    '''
    # check if path 
    print("FILE PATH IS: ", filePath)
    if os.path.isfile(filePath):
        folderName = os.path.dirname(filePath)

    else: 
        raise Exception("No such File exists to unzip!")

    try:
        with ZipFile(filePath, 'r') as zip:
    # printing all the contents of the zip file
            zip.printdir()
            if extractedDirPath == None : 
                newDir,zipProjectName = making_new_DIR(folderName , filePath)
                # extracting files at default location
                print('Extracting all the files at: ' + newDir)
                zip.extractall(newDir)
                print('Extraction Done!\n'
                    "GuessLang Started...")
                return newDir,zipProjectName
            
            elif extractedDirPath is not None:
                if os.path.isdir(extractedDirPath):
                    newDir,zipProjectName = making_new_DIR(extractedDirPath, filePath)

                    if  os.path.isdir(newDir):
                    # extracting all the files at the given location
                        print('Extracting all the files at: ' + newDir)
                        zip.extractall(newDir)
                        print('Unzipping Done!\n'
                            "GuessLang Started")
                        return newDir,zipProjectName
                
                    else:
                        raise Exception("No such Directory exists to extract the Files!")
                else:
                    raise Exception("Not A valid Folder path for Unzipping")
                
            else:
                raise Exception("Internal Error")
    
    except OSError as e:
        raise Exception("No such Directory exists to unzip!")

# TODO: Need to test and implement during optimizations
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


def modified_extension_checker(filePath): 
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
    code , fileExtension = modified_extension_checker(fileData["path"])
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

def writing_to_csv(userDict,csvDirectory):
    df = pd.DataFrame(userDict)
    print(df)
    # df.to_csv(csvDirectory, index=False)
    ct = datetime.datetime.now()
    try:
        if os.path.isdir(csvDirectory):
            newCSVDirectory = os.path.join(csvDirectory, 'ComplyVantage_Date_%d_%d_%d_Time_%d_%d_%d'%(ct.day,ct.month,ct.year,ct.hour,ct.minute,ct.second)+'.csv')
            try:
                df.to_csv(newCSVDirectory,index=False)
                print("CSV Created Successfully!")
                print("CSV created at: " + newCSVDirectory)
                return newCSVDirectory
            
            except Exception as e:
                print(e)
                print("CSV Creation Failed!")
        else: 
            raise Exception("Directory doesnot exist for CSV")
    
    except Exception as e:
        print(e)
        print("CSV Creation Failed!")

guess = Guess()
startTime = time.time()
parsingResult = parsing_all_files_and_folders(r"D:\CVtoPUSH\Github\GitHubPOC\Test Cases\hybridTest")
# print("Results of parsing:\n", )
print(parsingResult)


# print("Results of checking extensions:\n")
filesData = list(map(modified_checking_extension_langagues_of_all_files,parsingResult))
# results = [modified_checking_extension_langagues_of_all_files(data,guess) for data in parsingResult]
csvPath = writing_to_csv(filesData)
print(filesData)
print(len(filesData))
endTime = time.time()
print(endTime - startTime)