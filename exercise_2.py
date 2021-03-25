class Test:
    def __init__(self,fullname) -> None:
        self.fullname = fullname
        self.money = 200
    def cash_out(self, money):
        return self.money - money
    def cash_in(self, money):
        return self.money + money


name = input('dawere saxeli gvari: ')
p = Test(name)
proccess = input('romeli operaciis shesruleba gsurt? 1) gatana 2) shetana: ')
if proccess == '1' :
    how_much = int(input('ramdeni ginda?: '))
    print('{} tqveni darchenili tanxaa: {}'.format(p.fullname, p.cash_out(how_much)))
elif proccess == '2' :
    a = int(input('ramdeni shegaqvs?: '))
    print('{} jamshi tqveni tanxaa: {}'.format(p.fullname, p.cash_in(a)))
else:
    print('arasworia')
