
class stringComp(object):
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2
        self.mc = []
        self.ec = []
        self.dcc = []

    def missingChars(self):
        for x in range(0, len(self.string1)):
            if self.string1[x] not in self.string2:
                self.mc.append(self.string1[x])
        return self.mc

    def extraChars(self):
        for x in range(0, len(self.string2)):
            if self.string2[x] not in self.string1:
                self.ec.append(self.string2[x])
        return self.ec

    def amountOfDifference(self):
        self.dcc = len(self.mc) + len(self.ec)
        return self.dcc

nsc = stringComp("rochelle", "eric")
nscmc = nsc.missingChars()
print(nscmc)
nscec = nsc.extraChars()
print(nscec)
nscaod= nsc.amountOfDifference()
print(nscaod)