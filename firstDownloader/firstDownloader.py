"""
this is for python 2.7.5, needs adjustments to work with 3.3.3

this program will:
download all emoticon images for emoticons the user owns
download all emoticon images usable by emotityper
display a list of strings with all the emoticons the user owns in them
display a list of emoticons used by this program
tell you how many emoticons you own vs. how many this program uses
do all of it

"""

import urllib
import os
import re
#from collections import OrderedDict

emotilist = ['sunship', 'adamantine', '5Star', '9mm', 'bash', 'BlueMagic', 'bullet',
             'co2', 'essenceofdeath', 'gciknife', 'lol', 'mana', 'wtf', 'SRank', 'zz',
             'eye', 'xxx', 'agathacross', 'ai_repair', 'snooze', 'question', 'lp3p',
             'spark', 'lp33', 'AxeNSword', 'riddle', 'NZA2_Zed', 'NZA2_IronCross',
             'repairpad', 'duel', 'PS2', 'abc', 'asterisk', 'bndage', '99', 'ampersand',
             'comic', 'airmech', 'betalord', 'alphahero', 'htt', 'hth', 'deadlyd',
             'deadly0', 'deadly3', 'horseshoe', '2', '47', 'A', 'ai_fuel', 'arkham',
             'Avengers', 'beer', 'choke', 'csgoa', 'csgob', 'csgox', 'dsfight', 'FF',
             'fraud', 'gmod', 'glow', 'icon', 'ins', 'kudos', 'lcrown', 'lp3l', 'mmep_e',
             'mmep_m', 'mmep_p', 'p2aperture', 'p2blue', 'p2orange', 'P', 'plex',
             'power_main', 'riflesword', 'RogueMoneybags', 'shield_up', 'si',
             'silverdollar', 'slender', 'spatula', 'sr4', 'TheD', 'tinycoin', 'twbuh',
             'tyger', 'vectorcoin', 'vs', 'warband', 'wvwarning', 'XMen', 'xp', 'Y',
             'zero', 'exclamation', 'dipaddle', 'codknife', 'twplus']
username = ""
directory = ""
userURL = ""
choice = ""
userColonList = []
userList = []


def setUsername():
    """This sets the username, userURL variables and then runs the menu"""
    global username
    global userURL
    username = raw_input('Steam Custom URL name -- profile MUST be public (type semijames): ')
    userURL = 'http://steamcommunity.com/id/' + username + '/inventory/json/753/6'
    print "\nCustom URL name set to", username
    print "\nCustom URL set to", userURL

    menu()


def menu():
    #print "menu begun...\n"
    "This runs defs based on user choice"

    print "\nOk, " + username + ", what do you want to do?\n"
    print "1) Download Images of All Emoticons used by EmotiTyper to current directory\\firstDownloader_images_EmotiTyper\\"
    print "2) Download Images of All Emoticons You Own to current directory\\firstDownloader_images_" + username + "\\"
    print "3) Print a nice long string of all my emoticons in :emoticon: format"
    print "4) Print a list of my emoticons in list format ['emoticon', 'emoticon' ... ]"
    print "5) Print a list of emoticons I own that are usable by EmotiTyper"
    print "6) Print a list of the emoticons from teh Master List that I do not have"
    print "7) Change Custom URL\n"

    print "8) Exit"
    global choice
    choice = raw_input("\nChoose (1-8): ")
    #print choice, type(choice)
    if str(choice) == "1":
        getImages(emotilist)
        doMore()
    elif str(choice) == "2":
        getImages(emoticonNakedNameList())
        doMore()
    elif str(choice) == "3":
        printColonEmoticonString()
        doMore()
    elif str(choice) == "4":
        print emoticonNakedNameListOnly()
        doMore()
    elif str(choice) == "5":
        compareLists()
        doMore()
    elif str(choice) == "6":
        print dontHave()
        doMore()
    elif str(choice) == "7":
        setUsername()
        doMore()
    elif str(choice) == "8":
        print "Thank you for using (or not using) this utility."
    else:
        print "Please choose a valid choice! D:<"
        menu()
    return choice


def doMore():
    "This asks if the user wants to return to the Menu"
    #print "doMore begun...\n"
    print "\nWould you like to do more?"
    do = raw_input("Y/n  ")
    #print do, type(do)
    if do in ['y', 'Y', 'yes', 'YES', 'Yes', '']:
        menu()
    else:
        print "Ok, then. Bye."


def chooseDirectory(choice):
    "This specifies the directory to download emoticons to based on user choice"
    #print "chooseDirectory begun...\n"
    #print "choice is " + choice
    if choice == "1":  #This needs to be fixed to work with any option that says "do everything"
        directory = os.getcwd() + "\\firstDownloader_images_EmotiTyper\\"  #sets 'directory' variable to a subdirectory in the current working directory
    else:
        directory = os.getcwd() + "\\firstDownloader_images_" + username + "\\"
    print "directory chosen is " + directory
    return directory


def dupeCheck(seq):
    "This checks to see if there are any duplicate emoticon names in the results of scrapeEmotilist(), in the case of multiple copies of emoticons in the user inventory"
    #print "dupeCheck begun...\n"
    seen = set()
    seen_add = seen.add
    theReturn = [x for x in seq if x not in seen and not seen_add(x)]
    return theReturn


def scrapeEmotilist():
    "This will retrieve all names between, and including, '-:' and ':' on the userURL and return the results in a list"
    #print "scrapeEmotilist begun...\n"
    userPage = urllib.urlopen(userURL)
    text = userPage.read()
    #print text
    returnList = re.findall('-:.*?:', text)
    #print returnList
    return returnList


def colonEmoticonList():
    "This returns a list of the results of scrapeEmotilist in :emoticon: format"
    #print "colonEmoticonList begun...\n"
    tempReturnList = []
    for n in scrapeEmotilist():
        tempReturnList.append(n.replace('-', ''))
    return (dupeCheck(tempReturnList))  #returns a list in :emoticon: format



def printColonEmoticonString():
    "This prints a string of the results of scrapeEmotilist in :emoticon: format"
    #print "printColonEmoticonString begun...\n"
    tempReturnList = []
    for n in scrapeEmotilist():
        tempReturnList.append(n.replace('-', ''))
    print ' '.join(dupeCheck(tempReturnList))



def emoticonNakedNameList():
    "This produces a list of the results from scrapeEmotilist()"
    #print "emoticonNakedNameList begun...\n"
    tempReturnList = []
    for n in scrapeEmotilist():
        tempReturnList.append(n.replace('-', '').replace(':', ''))
    #print dupeCheck(tempReturnList)
    return dupeCheck(tempReturnList)


def emoticonNakedNameListOnly():
    "This does the same as emoticonNakedNameList, but also asks if the user wants to do more.  For when this is chosen as a menu option, and not called by another function."
    #print "emoticonNakedNameList begun...\n"
    tempReturnList = []
    for n in scrapeEmotilist():
        tempReturnList.append(n.replace('-', '').replace(':', ''))
    return dupeCheck(tempReturnList)



def dontHave():
    "This does the same as emoticonNakedNameList, but also asks if the user wants to do more.  For when this is chosen as a menu option, and not called by another function."
    #print "emoticonNakedNameList begun...\n"
    tempReturnList = []
    for n in scrapeEmotilist():
        tempReturnList.append(n.replace('-', '').replace(':', ''))
    return dupeCheck(tempReturnList)



def yourEmoticons():
    #print "yourEmoticons begun...\n"
    print "\nYour Emoticons: \n", scrapeEmotilist()
    if choice != '6':
        doMore()


def emotiTyperEmoticons():
    #print "emotiTyperEmoticons begun...\n"
    print "\nValid EmotiTyper Emoticons You Own: \n", compareLists()



"""
old non-def version:
    tempReturnList = []
    for n in returnList:
        tempReturnList.append(n.replace('-', '').replace(':', ''))
    return dupeCheck(tempReturnList)
"""


def getImages(myList):
    """This retrieves images in emotilist from the Steam cdn and puts them in the target directory"""
    #print "getImages begun...\n"
    directory = chooseDirectory(choice)
    if not os.path.exists(directory):
        os.makedirs(directory)

    for n in myList:
        url = 'http://cdn.steamcommunity.com/economy/emoticon/' + n
        urllib.urlretrieve(url, directory + n + ".png")

    if len(emotilist) == len(scrapeEmotilist()):
        print "\nfirstDownloader_Images_" + username + " directory created, emoticon images in inventory of " + username + " downloaded."
    else:
        print "\nfirstDownloader_Images_EmotiTyper directory created, emoticon images downloaded."



def compareLists():
    """This compares the return of emoticonNakedNameList() i.e. the user's emoticon list, with the masterlist,
    and creates a new list of emoticons that are common to both lists."""
    global emotilist
    compareListReturn = []
    nakedList = emoticonNakedNameList()  # making an object from a function?
    #print "nakedList: ", nakedList
    for n in nakedList:
        if n in emotilist:
            compareListReturn.append(n)
    #print "\ncompareListreturn: ", compareListReturn
    print "\nYou own " + str(len(compareListReturn)) + "/" + str(len(emotilist)) + " emoticons usable by this program"
    if raw_input("\nWould you like to see them?(Y/n)  ") in ['y', 'Y', 'yes', 'YES', 'Yes', '']:
        showMe = []
        for n in compareListReturn:
            newN = ':' + n + ':'
            showMe.append(newN)
        print "\n" + ' '.join(showMe) + "\n"



if __name__ == "__main__":
    setUsername()
    #menu()
    #doMore()
    #scrapeEmotilist()
    #getImages(emotilist)
    #getImages(emoticonNakedNameList())
    #print "\nYou own " + str(len(compareLists())) + "/" + str(len(emotilist)) + " emoticons usable by this program"
