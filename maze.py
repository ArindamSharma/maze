class Maze:
    def __init__(self,filename):
        f=open(filename,"r")
        self.maze=[]
        for i in f.readlines():
            tmp=[]
            for j in i:
                if(j=="#"):
                    tmp.append(0)
                elif(j=="a" or j=="b"):
                    tmp.append(j)
                elif(j==" "):
                    tmp.append(1)
                else:
                    pass
            self.maze.append(tmp)
        f.close()

    def printmaze(self,grid=False):
        if grid:pixel="_|"
        else:pixel="  "
        box="\x1b[5;30;47m"+pixel+'\x1b[0m'
        space="  "
        start="\x1b[5;30;42m"+space+'\x1b[0m'
        end="\x1b[5;30;41m"+space+'\x1b[0m'
        for i in self.maze:
            for j in i:
                if(j==0):
                    print(box,end="")
                elif(j==1):
                    print(space,end="")
                elif(j=="a"):
                    print(start,end="")
                elif(j=="b"):
                    print(end,end="")
                else:
                    pass
            print()
        print()

    def printmatrix(self):
        for i in self.maze:
            for j in i:
                print(j,end=" ")
            print()

    def debug(self):
        # self.printmatrix()
        # dfs
        # bfs
        # greedy bfs
        # a*
        
        pass

if __name__=='__main__':
    maze=Maze("maze1.txt")
    maze.printmaze(True)
    # maze.printmaze()
    # maze.printmatrix()