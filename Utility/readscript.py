import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\script.ini")

class readscript1:
    @staticmethod
    def geturl():
        url = config.get("test1","url")
        return url

    @staticmethod
    def getiframeid():
        iframeid = config.get("test1","iframeid")
        return iframeid

    @staticmethod
    def getdobxpath():
        dobxpath = config.get("test1","dobxpath")
        return dobxpath

    @staticmethod
    def getcalxpath():
        calxpath = config.get("test1", "calxpath")
        return calxpath

    @staticmethod
    def getdate():
        date = config.get("test1", "date")
        return date

    @staticmethod
    def getmonth():
        month = config.get("test1", "month")
        return month

    @staticmethod
    def getyear():
        year = config.get("test1", "year")
        return year

    @staticmethod
    def getmonthxpath():
        monthxpath = config.get("test1", "monthxpath")
        return monthxpath

    @staticmethod
    def getforwardtrixpath():
        forwardtrixpath = config.get("test1", "forwardtrixpath")
        return forwardtrixpath

    @staticmethod
    def getyearxpath():
        yearxpath = config.get("test1", "yearxpath")
        return yearxpath

    @staticmethod
    def getdatexpath():
        datexpath = config.get("test1", "datexpath")
        return datexpath

#####################################################################################################

class readscript2:
    @staticmethod
    def geturl():
        url = config.get("test2","url")
        return url

    @staticmethod
    def getproductsxpath():
        productsxpath = config.get("test2","productsxpath")
        return productsxpath

    @staticmethod
    def getselectproductopt():
        selectproductopt = config.get("test2","selectproductopt")
        return selectproductopt

    @staticmethod
    def getalloptionxpath():
        alloptionxpath = config.get("test2", "alloptionxpath")
        return alloptionxpath

    @staticmethod
    def getanimalxpath():
        animalxpath = config.get("test2", "animalxpath")
        return animalxpath

    @staticmethod
    def getselectanimalopt():
        selectanimalopt = config.get("test2", "selectanimalopt")
        return selectanimalopt

#####################################################################################################

class readscript3:
    @staticmethod
    def geturl():
        url = config.get("test3","url")
        return url

    @staticmethod
    def gettablexpath():
        tablexpath = config.get("test3","tablexpath")
        return tablexpath

    @staticmethod
    def getrowxpath():
        rowxpath = config.get("test3","rowxpath")
        return rowxpath

    @staticmethod
    def getcolxpath():
        colxpath = config.get("test3", "colxpath")
        return colxpath

    @staticmethod
    def getvaluexpath():
        valuexpath = config.get("test3", "valuexpath")
        return valuexpath

    @staticmethod
    def getdatexpath():
        datexpath = config.get("test3", "datexpath")
        return datexpath


#####################################################################################################


class readscript4:
    @staticmethod
    def geturl():
        url = config.get("test4","url")
        return url

    @staticmethod
    def getusernamexpath():
        usernamexpath = config.get("test4","usernamexpath")
        return usernamexpath

    @staticmethod
    def getpasswordxpath():
        passwordxpath = config.get("test4","passwordxpath")
        return passwordxpath

    @staticmethod
    def getsignxpath():
        signxpath = config.get("test4", "signxpath")
        return signxpath

    @staticmethod
    def getusername():
        username = config.get("test4", "username")
        return username

    @staticmethod
    def getpassword():
        password = config.get("test4", "password")
        return password

    @staticmethod
    def getinfoxpath():
        infoxpath = config.get("test4","infoxpath")
        return infoxpath

    @staticmethod
    def getfirstnamexpath():
        firstnamexpath = config.get("test4","firstnamexpath")
        return firstnamexpath

    @staticmethod
    def getfirstname():
        firstname = config.get("test4","firstname")
        return firstname

    @staticmethod
    def getmiddlenamexpath():
        middlenamexpath = config.get("test4", "middlenamexpath")
        return middlenamexpath

    @staticmethod
    def getmiddlename():
        middlename = config.get("test4", "middlename")
        return middlename

    @staticmethod
    def getlastnamexpath():
        lastnamexpath = config.get("test4", "lastnamexpath")
        return lastnamexpath

    @staticmethod
    def getlastname():
        lastname = config.get("test4", "lastname")
        return lastname

    @staticmethod
    def getsavexpath():
        savexpath = config.get("test4", "savexpath")
        return savexpath

###############################################################################################


class readscript5:
    @staticmethod
    def geturl():
        url = config.get("test5","url")
        return url

    @staticmethod
    def getcheckbox1():
        checkbox1 = config.get("test5","checkbox1")
        return checkbox1

    @staticmethod
    def getcheckbox2():
        checkbox2 = config.get("test5","checkbox2")
        return checkbox2


###################################################################################################


class readscript6:
    @staticmethod
    def geturl():
        url = config.get("test6","url")
        return url

    @staticmethod
    def getgmail():
        gmail = config.get("test6","gmail")
        return gmail

    @staticmethod
    def getsign():
        sign = config.get("test6","sign")
        return sign

#################################################################################################


class readscript7:
    @staticmethod
    def geturl():
        url = config.get("test7","url")
        return url

    @staticmethod
    def getcompxpath():
        compxpath = config.get("test7","compxpath")
        return compxpath

    @staticmethod
    def getcookiname():
        cookiname = config.get("test7","cookiname")
        return cookiname

    @staticmethod
    def getcookivalue():
        cookivalue = config.get("test7", "cookivalue")
        return cookivalue


########################################################################################


class readscript8:
    @staticmethod
    def geturl():
        url = config.get("test8","url")
        return url

    @staticmethod
    def getcontatusxpath():
        contatusxpath = config.get("test8","contatusxpath")
        return contatusxpath

    @staticmethod
    def getfirstnamexpath():
        firstnamexpath = config.get("test8","firstnamexpath")
        return firstnamexpath

    @staticmethod
    def getfirstname():
        firstname = config.get("test8", "firstname")
        return firstname

    @staticmethod
    def getcancelxpath():
        cancelxpath = config.get("test8", "cancelxpath")
        return cancelxpath

##############################################################################################



class readscript9:
    @staticmethod
    def geturl():
        url = config.get("test9","url")
        return url

    @staticmethod
    def getsignxpath():
        signxpath = config.get("test9","signxpath")
        return signxpath

    @staticmethod
    def getusernamexpath():
        usernamexpath = config.get("test9","usernamexpath")
        return usernamexpath

    @staticmethod
    def getusername():
        username = config.get("test9", "username")
        return username

    @staticmethod
    def getpasswordxpath():
        passwordxpath = config.get("test9", "passwordxpath")
        return passwordxpath

    @staticmethod
    def getpassword():
        password = config.get("test9", "password")
        return password

##################################################################################################



class readscript10:
    @staticmethod
    def geturl():
        url = config.get("test10","url")
        return url

    @staticmethod
    def getbrandxpath():
        brandxpath = config.get("test10","brandxpath")
        return brandxpath

    @staticmethod
    def getcheckboxxpath():
        checkboxxpath = config.get("test10","checkboxxpath")
        return checkboxxpath

    @staticmethod
    def getbrandname():
        brandname = config.get("test10", "brandname")
        return brandname

    @staticmethod
    def getsilderleftxpath():
        silderleftxpath = config.get("test10", "silderleftxpath")
        return silderleftxpath

    @staticmethod
    def getsilderrightxpath():
        silderrightxpath = config.get("test10", "silderrightxpath")
        return silderrightxpath

##################################################################################################


class readscript11:
    @staticmethod
    def geturl():
        url = config.get("test11","url")
        return url

    @staticmethod
    def getsourcexpath():
        sourcexpath = config.get("test11","sourcexpath")
        return sourcexpath

    @staticmethod
    def gettargetxpath():
        targetxpath = config.get("test11","targetxpath")
        return targetxpath

    @staticmethod
    def getpromptxpath():
        promptxpath = config.get("test11", "promptxpath")
        return promptxpath

    @staticmethod
    def getprompttext():
        prompttext = config.get("test11", "prompttext")
        return prompttext

    @staticmethod
    def gettextxpath():
        textxpath = config.get("test11", "textxpath")
        return textxpath

##################################################################################################


class readscript12:
    @staticmethod
    def geturl():
        url = config.get("test12","url")
        return url

    @staticmethod
    def getcorrectsearch():
        correctsearch = config.get("test12","correctsearch")
        return correctsearch

    @staticmethod
    def getincorrectsearch():
        incorrectsearch = config.get("test12","incorrectsearch")
        return incorrectsearch

    @staticmethod
    def getinputboxxpath():
        inputboxxpath = config.get("test12", "inputboxxpath")
        return inputboxxpath

    @staticmethod
    def getsubmitxpath():
        submitxpath = config.get("test12", "submitxpath")
        return submitxpath

    @staticmethod
    def getresultxpath():
        resultxpath = config.get("test12", "resultxpath")
        return resultxpath

##################################################################################################