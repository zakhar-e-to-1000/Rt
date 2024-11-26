class CasaCentr:
    def __init__(self) -> None:
        self.casa_list = []

    def add_casa(self, casa: list):
        self.casa_list.append(casa)

    def finished_on(self, i):
        self.casa_list[i].pop(0)
    
    def new_customer(self, customer):
        min_queue = min(*self.casa_list, key=len)
        min_queue.append(customer)
    
    def trancfer_customer(self, casa_from, casa_to):
        customer = casa_from.pop()
        casa_to.append(customer)

    def normalize(self):
        lent = sum(map(len, self.casa_list))
        min_num = lent//len(self.casa_list)
        if(lent%len(self.casa_list)!=0):
            min_num+=1
        boo = True
        while boo:
            boo = False
            for casa in self.casa_list:
                if len(casa)>min_num:
                    boo = True
                    for other_casa in self.casa_list:
                        if  other_casa is not casa and len(other_casa)<min_num:
                            while  len(casa)>=min_num and len(other_casa)<min_num:
                                self.trancfer_customer(casa, other_casa)
        # while boo:
        #     for casa in  self.casa_list:
                
cc = CasaCentr()
q2 = [1 for  _ in range(1)]
q3 = [7 for  _ in range(7)]
q1 = [5 for  _ in range(5)]
q4 = [10 for  _ in range(10)]

cc.add_casa(q1)
cc.add_casa(q2)
cc.add_casa(q3)
cc.add_casa(q4)
for casa in cc.casa_list:
    print(casa)
cc.normalize()

for casa in cc.casa_list:
    print(casa)