<<<<<<< HEAD
class sectionInfo():
    def __init__(self, first, second, cnt):
        self.point['first'] = first # bottom-left
        self.point['second'] = second # bottom-right
        self.found = cnt
    def pointChange(self, point, val):
        self.point[point] = val
    def getSection(self):
        return self.section
    def setFound(self, num):
        self.found = num
=======
class squareInfo():
    section = {}
    found = []
    def __init__(self, bl, br, tl, tr, cnt):
        self.section['bl'] = bl # bottom-left
        self.section['br'] = br # bottom-right
        self.section['tl'] = tl # top-left
        self.section['tr'] = tr # top-right
        self.found = cnt
    def sectionChange(self, section, val):
        self.section['section'] = val
    def getSection(self):
        return self.section
>>>>>>> f4996fb9b9842864eac66e96a938ca2d98acc5c6

class sectionList():
    def __init__(self):
        self.li = []

    def find(self, point, num):
        if point == None:
            point = ['first', 'second']
        for l in self.li:
            sec = l.getSection()
            if point is list:
                for p in point:
                    if sec[p] == num:
                        return l, p
            else:
                if sec[point] == num:
                    return l, point
        return None, None

    def modifyAll(self, inSec):
        section = ['first', 'second']
        retInSec = inSec.getSection()
        for sec in self.li:
            retSec = sqr.getSection()
            if retSec[sec] == retInSec[sec]:
                sec = inSec
                return

    def addSection(self, first, second, cnt):
        self.li.append(sectionInfo(first, second, cnt))
