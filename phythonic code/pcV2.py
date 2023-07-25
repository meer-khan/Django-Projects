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
    
