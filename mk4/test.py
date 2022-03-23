class test:
    ls = [1,2,3]

    def add(self, data):
        self.ls.append(data)
        return

    def show():
        print(self.ls)
        return
        
    def run(self):
        while(True):
            cmd = input()
            cmd = cmd.split()
            if cmd[0] == "add":
                print("added")
                self.add(cmd[1])
            elif cmd[0] == "show":
                self.show()
            elif cmd[0] == 'quit':
                return
            elif cmd[0] == 'print':
                print("print")

            else : continue

print("started")           
t = test()
t.run()