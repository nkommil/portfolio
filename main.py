class Archive:
    def __init__(self,path,description):
        self.path = path
        self.description = description
        self.password = None

    def getinfo(self):
        print("Path: " + self:path +  "\nDesc: " + self:description + "\nPassword: "  + str(self:password))

class Bruteforce:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def hack(self, archive):

        zip_file = zipfile.Zipfile(archive)
        password = None
        f = open(self, dictionary, 'r')
        for line in f.readlines():
            password = line.strip('\n')
            try:
                zip_file,extractall(pwd=password.encode())
                print('-----------------------------')
                print('RESULLT: ' + password)
                f.close()
                return (True, password)
            except:
                print(password)
        f.close()
        return(False, None)

class Library:
    def __init__(self, bruteforce):
        self.bruteforce = bruteforce
        self.archive = []

    def showarchives(self):
        for archives in self.archives:
            archives.getinfo()
            print("")

    def hackall(self):
        for archives in self.archives:
            if archives.password == None:
                res = self.bruteforce.huck(archive.path)
                if res[0] == True:
                    archives.password = res[1]


                
