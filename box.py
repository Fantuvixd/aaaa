def directory(): import os; return os.getcwd()
def tzFilter():
    import datetime, pytz
    UTC = {"+11":'+660',"+10":'+600',"+09":'+540',"+08":'+480',"+07":'+420',"+06":'+360',"+05":'+300',"+04":'+240',"+03":'+180',"+02":'+120',"+01":'+60',"GMT":'+0',"-01":'-60',"-02":'-120',"-03":'-180',"-04":'-240',"-05":'-300',"-06":'-360',"-07":'-420',"-08":'-480',"-09":'-540',"-10":'-600',"-11":'-660',"-12":'+720'}
    zones = ['Etc/GMT-11','Etc/GMT-10','Etc/GMT-9','Etc/GMT-8','Etc/GMT-7','Etc/GMT-6','Etc/GMT-5','Etc/GMT-4','Etc/GMT-3','Etc/GMT-2','Etc/GMT-1','Etc/GMT0','Etc/GMT+1','Etc/GMT+2','Etc/GMT+3','Etc/GMT+4','Etc/GMT+5','Etc/GMT+6','Etc/GMT+7','Etc/GMT+8','Etc/GMT+9','Etc/GMT+10','Etc/GMT+11','Etc/GMT+12']
    for _ in zones:
        H = datetime.datetime.now(pytz.timezone(_)).strftime("%H"); Z = datetime.datetime.now(pytz.timezone(_)).strftime("%Z")
        if H=="23": break
    return UTC[Z]
    
def random_code(length: str = 15):
    import string, random
    code=[]; ch = list(string.ascii_letters+string.digits+"!@#$%^&*");random.shuffle(ch)
    for i in range(length): code.append(random.choice(ch))
    random.shuffle(namex); return "".join(code)