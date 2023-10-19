import json , re
import Licenses


# #######################################################################
def license_extractor(text):
    '''
    apply finditer on license text and returns list of callable iterators of finditer matches
    '''
    license = Licenses.licenses
    results = []
    for i in license: 
        licenseName = i["licenseName"]
        licenseId = i["licenseId"]
        # regexForLicenseExtraction = f'(The)?\s+({licenseName}|{licenseId})\s+'
        regexForLicenseExtraction = f'(The)?\s*({licenseName}|{licenseId})\s*'

        pattern = re.compile(regexForLicenseExtraction, re.I|re.M)
        match = pattern.finditer(text)
        results.append(match)
    
    # return []
    
    return results

def new_license_extractor(text):
    '''
    apply finditer on license text and returns list of callable iterators of finditer matches
    '''
    license = Licenses.licenses
    return [re.compile(f'(The)?\s*({i["licenseName"]}|{i["licenseId"]})\s*', re.I|re.M).finditer(text) for i in license]





###########################################################################################
def license_refiner(match,text):
    result = []
    licensesFound = []
    for callable_iterator in match:
        for i in callable_iterator:
            try:
                span = i.span()
                print(i.span())
                print(text[span[0]:span[1]])
                result.append(text[span[0]:span[1]])
            except:
                continue
    
    if result == []:
        # print("NO MATCH FOUND")
        return None
    else:
        # print("results",result)
        for i in result:
            # print(i)
            j = i.replace('\n',"")
            # pattern = re.compile()
            licensesFound.append(j)
    # print(licensesFound)
    return licensesFound

def new_license_refiner(matches,text):
    '''
    License refiner takes spans (returned from finditer) and extract substrings/text-chunks
    '''
    result = [text[match.span()[0]:match.span()[1]] for callable_iterator in matches for match in callable_iterator]
    return [i.replace('\n', '') for i in result] if result else None








###########################################################################################

def advance_license_check(text):
    '''
    advance license check takes out special licenses from licenses and apply regex on text
    '''
    license = Licenses.specialLicenses
    results = []
    for i in license: 
        # licenseName = i["licenseName"]
        # licenseId = i["licenseId"]
        regexForLicenseExtraction = f'(The)?\s+({i})\s+'
        pattern = re.compile(regexForLicenseExtraction, re.I|re.M)
        match = pattern.finditer(text)
        results.append(match)
    
    return results

def new_advance_license_check(text):
    '''
    advance license check takes out special licenses from licenses and apply regex on text
    '''
    license = Licenses.specialLicenses
    return [re.compile(f'(The)?\s+({lin})\s+', re.I|re.M).finditer(text) for lin in license]








################################################################# 

# REPORT ISSUE
def license_extraction(text):
    # licenseName = "MIT License"
    # licenseId = "MIT"
    # result = []
    license = Licenses.licenses

    # for lin in  license: 
    #     # print(lin["licenseName"])
    #     regexForLicenseExtraction = fr'(The)?\s*(\b{lin["licenseName"].lower()}|\b{lin["licenseId"].lower()})\s+'
    #     pattern = re.compile(regexForLicenseExtraction, re.I|re.M)
    #     match = pattern.findall(text)
    #     if match != []:
    #         print(match)
    #         result.append(match[0][1])
    # return result
    result = [i for i in [re.compile(fr'(The)?\s*(\b{lin["licenseName"].lower()}|\b{lin["licenseId"].lower()})\s+', re.I|re.M).findall(text) for lin in license] if i != []]
    result = [match for lin in license if (match:=re.compile(fr'(The)?\s*(\b{lin["licenseName"].lower()}|\b{lin["licenseId"].lower()})\s+', re.I|re.M).findall(text) != [])]
    # import re
    return result



# Giving un useful error: 
# (env-postgresdjango) D:\CVtoPUSH\Github\GithubRelease\GitHubCrawler\LicenseExtraction>python license_extraction.py
# Traceback (most recent call last):
#   File "D:\CVtoPUSH\Github\GithubRelease\GitHubCrawler\LicenseExtraction\license_extraction.py", line 60, in <module>
#     print(license_extraction(cleanedCode))
#   File "D:\CVtoPUSH\Github\GithubRelease\GitHubCrawler\LicenseExtraction\license_extraction.py", line 47, in license_extraction
#     result = [i for i in [re.compile(fr'(The)?\s*(\b{lin["licenseName"].lower()}|\b{lin["licenseId"].lower()})\s+', re.I|re.M).findall(text) for lin in license] if i != []]
# TypeError: '_Printer' object is not iterable







################################################################

def license_extraction(text):
    # licenseName = "MIT License"
    # licenseId = "MIT"
    result = []
    license = Licenses.licenses

    for lin in  license: 
        # print(lin["licenseName"])
        regexForLicenseExtraction = fr'(The)?\s*(\b{lin["licenseName"].lower()}|\b{lin["licenseId"].lower()})\s+'
        pattern = re.compile(regexForLicenseExtraction, re.I|re.M)
        match = pattern.findall(text)
        if match != []:
            print(match)
            result.append(match[0][1])
    return result


def new_license_extraction(text):
 
    license = Licenses.licenses

    # * Both lines not work same, first one is with double list comprehension and other with walrus operator (introduced in python 3.8)
    # through second line, we can only get the bool value of the expression used in if condition
    # Study about walrus operator
    result = [match[0] for match in [re.compile(fr'(The)?\s*(\b{lin["licenseName"].lower()}|\b{lin["licenseId"].lower()})\s+', re.I|re.M).findall(text) for lin in license] if match != []]
    result = [match[0] for lin in license if (match := re.compile(fr'(The)?\s*(\b{lin["licenseName"].lower()}|\b{lin["licenseId"].lower()})\s+', re.I|re.M).findall(text) != [])]
    return result







##############################################################
def get_maxsized_license(licenses):
    '''
    get_maxsized_license: returns most appropriate matching group out of all captured groups
    '''
    maxValue = ""
    maxv = 0
    for lin in licenses[0]:
        print(lin)
        if maxv < len(lin[1]):
            maxValue = lin[1]
    
    return maxValue


def new_get_maxsized_license(licenses):
    '''
    get_maxsized_license: returns most appropriate matching group out of all captured groups
    '''
    return max([lin for lin in [lin[1] for lin in licenses[0]]], key= len)
    










# LAST UPDATE: 

import json , re
import Licenses
import test_license
import difflib



def license_extractor(text):
    '''
    license_extractor: apply finditer on license text and returns list of callable iterators of finditer matches
    '''
    license = Licenses.licenses
    return [re.compile(f'(The)?\s*({lin["licenseName"]}|{lin["licenseId"]})\s*', re.I|re.M).finditer(text) for lin in license]

def license_refiner(matches,text):
    '''
    license_refiner: takes spans (returned from finditer) and extract substrings/text-chunks
    '''
    result = [text[match.span()[0]:match.span()[1]] for callable_iterator in matches for match in callable_iterator]
    return [i.replace('\n', '') for i in result] if result else None

def advance_license_check(text):
    '''
    advance_license_check: takes out special licenses from licenses and apply regex on text
    '''
    license = Licenses.specialLicenses
    return [re.compile(f'(The)?\s+({lin})\s+', re.I|re.M).finditer(text) for lin in license]

def license_extraction(text):
    '''
    This function is used to iterate over licenses list and returns the matched capturing group 
    '''
    spdxLicenses = Licenses.licenses
    staticLicenses = Licenses.staticLicensesName
    licenseAbreviations = Licenses.Licenseabbreviations
    spl = Licenses.specialPurposeLicense
    spl.extend(Licenses.interNationalLicense)
    # print(spl)
    # print(staticLicenses)
    # spdxlin = []
    spdxlin = [match for match in [re.compile(fr'(The)?\s*(\b{lin["licenseName"]}),?.?\s+', re.I|re.M).findall(text) for lin in spdxLicenses] if match != []]

    if spdxlin == []:
        print("in Identifiers")
        spdxIdentifiers = [match for match in [re.compile(fr'(The)?\s*(\b{lin["licenseId"]}),?.?\s+', re.I|re.M).findall(text) for lin in spdxLicenses] if match != []]
        spdxIdentifiers.extend(spdxlin)
    # spdxlin = [match for match in [re.compile(fr'(The)?\s*(\b{lin["licenseName"]}|\b{lin["licenseId"]}),?.?\s+', re.I|re.M).findall(text) for lin in spdxLicenses] if match != []]
    
    # print("RESULTS: ", result)
    staticlin =  [match for match in [re.compile(fr'(The)?\s*(\b{lin}).?,?\s+', re.I|re.M).findall(text) for lin in staticLicenses] if match != []]
    ablin = []
    if spdxlin == [] and staticlin == []:
        ablin =  [match for match in [re.compile(fr'(The)?\s*(\b{lin}).?,?\s+', re.I|re.M).findall(text) for lin in licenseAbreviations] if match != []]
        print( "ABLIN IS: ",ablin)
    
    if spdxlin == [] and staticlin == [] and ablin == []:
        splin = [match for match in [re.compile(fr'(The)?\s*(\b{lin}).?,?\s+', re.I|re.M).findall(text) for lin in spl] if match != []]
        ablin.extend(splin)

    return spdxlin, staticlin, ablin



def license_extraction_2(text): 
    pass



def settingup_licenses_2(spdxGroup, staticGroup=None, ablinGroup=None):
    max = 0
    # min = 0
    license = ""
    print("MATCHED GROP: SPDX: ", spdxGroup)

    spdxGroups = [license for lin in { lin.upper() for group in spdxGroup for tup in group for lin in tup if lin != "" and lin.lower() != "the"} if len(lin)> max if (max:= len(lin)) if (license:= lin)]

    # spdxGroups = set(spdxGroups)
    print("BIGGEST SPDX GROUP: ", spdxGroups)
    for lin in spdxGroups:
        print(lin)
        if len(lin) > max: 
            max = len(lin)
            license = lin 
    
    print("Biggest License is: ",license)

def settingup_licenses(spdxGroup, staticGroup, ablinGroup):
    '''
    settingup_licenses: returns most appropriate groups
    '''
    spdxGroups = { lin.upper() for group in spdxGroup for tup in group for lin in tup if lin != "" and lin.lower() != "the"}
    # license = ""
    # max = 0
    # spdxGroups = {license for lin in { lin.upper() for group in spdxGroup for tup in group for lin in tup if lin != "" and lin.lower() != "the"} if len(lin)> max if (max:= len(lin)) if (license:= lin)}
    # print("\nSPDX GROU: ", spdxGroups)
    staticGroups = { lin.upper() for group in staticGroup for tup in group for lin in tup if lin != "" and lin.lower() != "the"}
    if ablinGroup != []:
        ablinGroups = { lin.upper() for group in ablinGroup for tup in group for lin in tup if lin != "" and lin.lower() != 'the'}
        return spdxGroups | staticGroups | ablinGroups
    return spdxGroups | staticGroups




def get_maxsized_license(licenses):
    '''
    get_maxsized_license: returns most appropriate matching group out of all captured groups
    '''
    return max([lin for lin in [lin[1] for lin in licenses[0]]], key= len) if len(licenses) > 0 else "Un-named License"
    # return []


def clean(text):
    '''
    Cleanup copyright text: to remove extra lines
    '''
    text = text.replace("\n\n", " ").replace("\n"," ").replace("(","").replace(")", "").strip()
    text = text.split()
    text = " ".join(text)
    return text


# def remove_extrac

def exceptional_cases(str1,str2):
    print("String 1 is: ", str1 , " and string 2 is: ", str2)
    GNU_exceptionList = ["GNU AFFERO GENERAL PUBLIC LICENSE", 
                         "GNU LESSER GENERAL PUBLIC LICENSE",
                         "GNU GENERAL PUBLIC LICENSE",
                         "GNU LIBRARY GENERAL PUBLIC LICENSE",]
    
    print("Im in exceptional cases function")
    print(str1.upper().strip())
    print((str1.upper().strip() in GNU_exceptionList))
    return 0.5 if (str1.upper().strip() in GNU_exceptionList and str2.upper().strip() in GNU_exceptionList) and (str1 != str2) else None


def calculate_similarity(str1, str2):
    excSimilarity = exceptional_cases(str1,str2)
    print("ExcSIM: ",excSimilarity)
    if excSimilarity == 0.5:
        print("yes it is exceptional")
        return excSimilarity
    seq = difflib.SequenceMatcher(None, str1.lower().replace("license", ""), str2.lower().replace("license", ""))
    similarity = seq.ratio()
    # percentage = similarity * 100
    return similarity



def remove_non_similar(org_licence):
    '''
    remove_non_similar: takes licenses list, iterate over each element and finds out it's similarity with every other element and removes element with less than threshold
    '''
    copy_licence = org_licence.copy()
    for lin in org_licence: 
        for i in range(org_licence.index(lin)+1, len(org_licence)):
            percentage_match = calculate_similarity(org_licence[i], lin)
            print("Percentage match is: ",percentage_match)
            if percentage_match > 0.7:
                # print()      
                lenstr1 = len(org_licence[i])
                lenstr2 = len(lin)
                if lenstr1 > lenstr2:
                    copy_licence.remove(lin)
                else:
                    print("License is: ", org_licence[i])
                    copy_licence.remove(org_licence[i])


    copy_licence.sort(key=len)
    return copy_licence

def remove_abbr(licenses):
    # global final_lin
    copy_licence2 = licenses.copy()
    # print(copy_licence2)
    for lin in licenses:
        for i in range(licenses.index(lin)+1, len(licenses)): 
            lin2 = licenses[i]
            if lin in licenses[i]:
                lenstr1 = len(license[i])
                lenstr2 = len(lin)
                if lenstr1 > lenstr2:
                    copy_licence2.remove(lin)
                else:
                    copy_licence2.remove(license[i])
    
    return copy_licence2



def license_extractor(text):
    spdxLicenses = Licenses.licenses
    linList = []
    for lin in spdxLicenses:
        # print(lin)
        pattern = re.compile(r'\blicense\b.*', re.IGNORECASE)
        cleaned_string = re.sub(pattern, "License", lin["licenseName"])
        # pattern = re.compile(fr'(The)?\s*(\b{lin["licenseName"]}),?.?\s+', re.I|re.M)
        pattern = re.compile(fr'(The)?\s*(\b{cleaned_string}),?.?\s+', re.I|re.M)

        matches = pattern.findall(text)
        for match in matches: 
            if match != []:
                linList.append(match)
    # spdxlin = [match for match in [re.compile(fr'(The)?\s*(\b{lin["licenseName"]}),?.?\s+', re.I|re.M).findall(text) for lin in spdxLicenses] if match != []]

    return linList

            
def attach_license(licenses):
    '''
    gets the list of licenses, and attach license if not available
    '''
    LW = []
    if licenses == []:
        return []
    for i in licenses:
        if "LICENSE" not in i:
            LW.append(i + " LICENSE")
        else:
            LW.append(i)

    return LW

def serializer(licenses):
    
    return ",".join(licenses)



if __name__ == "__main__": 
    text = test_license.upl
    cleanedText = clean(text)
    print(cleanedText)
    matchedGroups, staticMatchedGroups , ablin= license_extraction(cleanedText)
    print("TYPE OF MATCHED GROUP: ", type(matchedGroups), matchedGroups)
    print("TYPE OF Static GROUP: ", type(staticMatchedGroups), staticMatchedGroups)
    print("TYPE OF ablin GROUP: ", type(ablin), ablin)

    caprturedGroups = settingup_licenses(matchedGroups, staticMatchedGroups, ablin)
    print("\nCaptured Groups: ", caprturedGroups)

    nonSimilarLicnese = (remove_non_similar(list(caprturedGroups)))
    nonABBR = remove_abbr(nonSimilarLicnese)

    print("NON ABBR",nonABBR)
    attachedLicense = attach_license(nonABBR)
    print(attachedLicense)
    serialize = serializer(attachedLicense)
    print(serialize)
    print(type(serialize))

