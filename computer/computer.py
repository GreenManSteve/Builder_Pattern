class Computer():
    def display(self):
        temp = vars(self)
        for item in temp:
            print(item, ':', temp[item])