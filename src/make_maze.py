import random
import sys

#Reading of input parametres.
n = int(sys.argv[1]) #the number of rows and columns of the graph grid
x = int(sys.argv[2]) #the coordinate of the starting node
y = int(sys.argv[3]) #the coordinate of the starting node
random.seed(sys.argv[4])
output_file = (sys.argv[5]) #the file of maze's storage

if n <= 30 and x < n and x >= 0 and y < n and y >= 0:
    neighbouring_nodes = {} #declaration of graph with neighbouring nodes
    #graph creation
    for i in range(n):
        for j in range(n):
            list = []
            if (j + 1 < n):
                list.append((i, j + 1)) #add the east neighbour
            if (i + 1 < n):
                list.append((i + 1, j)) #add the south neighbour
            if (j - 1 >= 0):
                list.append((i, j - 1)) #add the west neighbour
            if (i - 1 >= 0):
                list.append((i - 1, j)) #add the north neighbour
            neighbouring_nodes[(i, j)]=list

    visited = [] #declaration of list with the nodes who have been visited 

    f = open(output_file+'.txt', 'w') #creation of the file with the path

    def create_maze(mytuple):
        visited.append(mytuple) #visit of the particular tuple
        random_neighbours = random.sample(neighbouring_nodes[mytuple], len(neighbouring_nodes[mytuple]))
        for i in random_neighbours:
            flag = False
            for j in visited:
                if (i == j):
                    flag = True 
            if not flag:
                f.write("%s, %s\n" % (mytuple, i)) 
                create_maze(i) #call method recursively

    #call of method with the user's tuple
    users_tuple = (x, y)
    create_maze(users_tuple) 
    
    f.close()
else:
    print ('Error on inupt parameters. Try again!')


                

            
        
        
        
        
    










    


    

