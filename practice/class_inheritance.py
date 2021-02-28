class SuperList(list):
    def __len__(self):
        print("1000")

l1 = SuperList()
l1.append(5)
l1.append(6)
print(l1)
l1.__len__()