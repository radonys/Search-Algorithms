
import sys
import Queue
from Queue import PriorityQueue
import time
import math
goal_state = [1, 4, 7, 2, 5, 8, 3, 6, 0]
total_cost = 0
z=1

		
def move_up( state ):
	
	new_state = state[:]
	index = new_state.index( 0 )

	if index not in [0, 3, 6]:
		###cal_cost( state, index-1 )
		temp = new_state[index - 1]
		new_state[index - 1] = new_state[index]
		new_state[index] = temp
		return new_state
	else:		return None

def move_down( state ):
	
	new_state = state[:]
	index = new_state.index( 0 )
	
	if index not in [2, 5, 8]:
		temp = new_state[index + 1]
		new_state[index + 1] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None

def move_left( state ):
	
	new_state = state[:]
	index = new_state.index( 0 )
	
	if index not in [0, 1, 2]:
		temp = new_state[index - 3]
		new_state[index - 3] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None

def move_right( state ):
	
	new_state = state[:]
	index = new_state.index( 0 )
	if index not in [6, 7, 8]:
		temp = new_state[index + 3]
		new_state[index + 3] = new_state[index]
		new_state[index] = temp
		return new_state
	else:
		return None

def create_node( state, parent, operator, depth, cost ):
	return Node( state, parent, operator, depth, cost )

def expand_node( node, nodes ):
	expanded_nodes = []
	
	expanded_nodes.append( create_node( move_up( node.state ), node, "u", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_left( node.state ), node, "l", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_right( node.state), node, "r", node.depth + 1, 0 ) )
	expanded_nodes.append( create_node( move_down( node.state ), node, "d", node.depth + 1, 0 ) )
	
	expanded_nodes = [node for node in expanded_nodes if node.state != None] 
	return expanded_nodes

def bfs( start, goal ):

	nodes = [] #Queue
	
	nodes.append( create_node( start, None, None, 0, 0 ) )
	while True:
		if len( nodes ) == 0: return None
		
		node = nodes.pop(0)
		
		if node.state == goal:
			moves = []
			temp = node
			while True:
				moves.insert(0, temp.operator)
				if temp.depth == 1: break
				temp = temp.parent
			return moves				
		nodes.extend( expand_node( node, nodes ) )###bfs main step
		
		
def dfs( start, goal, depth=10 ):
	
	depth_limit = depth
	nodes = []
	nodes.append( create_node( start, None, None, 0, 0 ) )
	while True:
		if len( nodes ) == 0: return None
		node = nodes.pop(0)
		if node.state == goal:
			moves = []
			temp = node
			while True:
				moves.insert(0, temp.operator)
				if temp.depth <= 1: break
				temp = temp.parent
			return moves				
		if node.depth < depth_limit:
			expanded_nodes = expand_node( node, nodes )
			expanded_nodes.extend( nodes ) ###dfs main step
			nodes = expanded_nodes
			###print nodes


def bidirec(start,goal_state):
    
    i_queue=Queue.Queue()
    i_queue.put(start)
    
    f_queue=Queue.Queue()
    f_queue.put(goal_state)
    
    i_append=[]
    i_append.append(start)
    
    f_append=[]
    f_append.append(goal_state)
    
    i_parent=[]
    i_parent.insert(0,0)
    
    f_parent=[]
    f_parent.insert(0,0)
    
    i_print=[]
    f_print=[]
    
    i_visit=[]
    f_visit=[]  
    
    while True:
        if i_queue.empty() or f_queue.empty():
            return None
            
        c_start=i_queue.get()
        c_final=f_queue.get()
        
        t_start=i_append.index(c_start)
        t_final=f_append.index(c_final)
        
        if find_state(i_visit,f_visit) or  c_start==c_final:
        
            i_print = goal_path( start,c_start,i_append,i_parent)
            f_print = goal_path( goal_state,c_final,f_append,f_parent)
            
            print i_print[::-1]
            print f_print[::-1]

            if len(i_visit)>len(f_visit):
                return len(i_visit)+1
            else:
                return len(f_visit)+1
                
        if c_start and function_visit(c_start,i_visit)==0:
            
            if move_up(c_start) and function_visit(move_up(c_start),i_visit)==0:
                i_queue.put(move_up(c_start))
                i_append.append(move_up(c_start))
                y=i_append.index(move_up(c_start))
                i_parent.insert(y,t_start)
                
            if move_down(c_start) and function_visit(move_down(c_start),i_visit)==0:
                i_queue.put(move_down(c_start))
                i_append.append(move_down(c_start))
                y=i_append.index(move_down(c_start))
                i_parent.insert(y,t_start)
            
            if move_left(c_start) and function_visit(move_left(c_start),i_visit)==0:
                i_queue.put(move_left(c_start))
                i_append.append(move_left(c_start))
                y=i_append.index(move_left(c_start))
                i_parent.insert(y,t_start)
            
            if move_right(c_start) and function_visit(move_right(c_start),i_visit)==0:
                i_queue.put(move_right(c_start))
                i_append.append(move_right(c_start))
                y=i_append.index(move_right(c_start))
                i_parent.insert(y,t_start)
                
        if c_final and function_visit(c_final,f_visit)==0:
            
            if move_up(c_final) and function_visit(move_up(c_final),f_visit)==0:
                f_queue.put(move_up(c_final))
                f_append.append(move_up(c_final))
                y=f_append.index(move_up(c_final))
                f_parent.insert(y,t_final)
            
            if move_down(c_final) and function_visit(move_down(c_final),f_visit)==0:
                f_queue.put(move_down(c_final))
                f_append.append(move_down(c_final))
                y=f_append.index(move_down(c_final))
                f_parent.insert(y,t_final)
            
            if move_left(c_final) and function_visit(move_left(c_final),f_visit)==0:
                f_queue.put(move_left(c_final))
                f_append.append(move_left(c_final))
                y=f_append.index(move_left(c_final))
                f_parent.insert(y,t_final)
            
            if move_right(c_final) and function_visit(move_right(c_final),f_visit)==0:
                f_queue.put(move_right(c_final))
                f_append.append(move_right(c_final))
                y=f_append.index(move_right(c_final))
                f_parent.insert(y,t_final)
        i_visit.append(c_start)
        f_visit.append(c_final)
        
def find_state(i_visit,f_visit):
    for x in i_visit:
        for y in f_visit:
            if x==y:
                return 1
    return 0
def goal_path(start,goal_state,appended_list,parent):
    p=[]
    x=appended_list.index(goal_state)
    p.append(goal_state)
    while parent[x]!=x:
        p.append(appended_list[parent[x]])
        x=parent[x]
    return p


def function_visit(current_state,visited):
    for x in visited:
        if x==current_state:
            return 1
    return 0			
    

def goal_path(start,goal,appended_list,parent):
    p=[]
    x=appended_list.index(goal)
    p.append(goal)
    while parent[x]!=x:
        p.append(appended_list[parent[x]])
        x=parent[x]
    return p


def visit(c_state,visited):
    for x in visited:
        if x==c_state:
            return 1
    return 0
    
def cal_cost(c_state,i):
    x=c_state.index(0)
    y=i.index(0)
    check=c_state[y]
    if check==1 or check==2 or check==3:
        return 1
    elif check==4 or check==5 or check==6:
        return 2
    elif check==7 or check==8:
        return 3
        
class Node:
	def __init__( self, state, parent, operator, depth, cost ):

		self.state = state
		self.parent = parent
		self.operator = operator
		self.depth = depth
		self.cost = cost



class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item


def left(t):
	l = list(t[0])
	cost = t[2]
	i = l.index(0)
	if i  in [0,3,6]:
		return -1
	temp = l[i-1]
	if temp in [1,2,3]:
		cost += 1
	if temp in [4,5,6]:
		cost += 2
	if temp in [7,8]:
		cost += 3 
	l[i-1] = l[i]
	l[i] = temp
	path = list(t[1])
	return tuple((l,path,cost)) 
 	

def right(t):
	l = list(t[0])
	cost = t[2]
	i = l.index(0)
	if i  in [2,5,8]:
		return -1
	temp = l[i+1]
	if temp in [1,2,3]:
		cost += 1
	if temp in [4,5,6]:
		cost += 2
	if temp in [7,8]:
		cost += 3 
	l[i+1] = l[i]
	l[i] = temp
	path = list(t[1])
	return tuple((l,path,cost)) 
 	


def up(t):
	l = list(t[0])
	cost = t[2]
	i = l.index(0)
	if i  in [0,1,2]:
		return -1
	temp = l[i-3]
	if temp in [1,2,3]:
		cost += 1
	if temp in [4,5,6]:
		cost += 2
	if temp in [7,8]:
		cost += 3 
	l[i-3] = l[i]
	l[i] = temp
	path = list(t[1])
	return tuple((l,path,cost)) 
 	


def down(t):
	l = list(t[0])
	cost = t[2]
	i = l.index(0)
	if i  in [6,7,8]:
		return -1
	temp = l[i+3]
	if temp in [1,2,3]:
		cost += 1
	if temp in [4,5,6]:
		cost += 2
	if temp in [7,8]:
		cost += 3 
	l[i+3] = l[i]
	l[i] = temp
	path = list(t[1])
	return tuple((l,path,cost)) 
 	


def ufs(s,e):
	visited = []
	start = (s,[],0) #(vertex,path to this vertex [])
	q = MyPriorityQueue()
	q.put(tuple(start),start[2])
	while q:
		current = tuple(q.get())
		current[1].append(current[0])
		if(current[0] == e):
			return current[1],current[2]
		if (left(list(current)) != -1) and (current[0] not in visited):
			t = tuple(left(tuple(current)))
			q.put(t,t[2])
		if (right(list(current)) != -1) and (current[0] not in visited):
			t = tuple(right(list(current)))
			q.put(t,t[2])
		if (up(list(current)) != -1) and (current[0] not in visited):
			t = tuple(up(list(current)))
			q.put(t,t[2])
		if (down(list(current)) != -1) and (current[0] not in visited):
			t = tuple(down(list(current)))
			q.put(t,t[2])
		if current[0] not in visited:
			visited.append(current[0])
def printPath(path,cost):
	print "----------------"
	print "cost :",cost
	print "----------------"

	for l in path:
		print l[0:3]
		print l[3:6]
		print l[6:9]
		print "###########"
	print "cost is:",len(path)
def main():
	global total_cost
	#starting_state = [0, 4 , 7, 1 ,2 ,8, 3, 5, 6]
	starting_state = [1, 4, 7, 2, 5, 0, 3, 6, 8]
	
	#
	print "****************AI First Assignment****************"
	print "	    8-puzzle Solving Techniques		"
	print "1) Breadth-First Search"
	print "2) Depth-First Search"
	print "3) Uniform Cost Search"
	print "4) Bidirectional Search using BFS"
	data = input("Enter option number: ")
	if data==1:
		tim=[]
	    	total=0
	    	ts=time.time()
		result = bfs( starting_state, goal_state )
		te=time.time()
		totalt=float(total)+float(te-ts)
		tim.append(float(te-ts))
		avg=float(totalt)/z
		sd=0.0
		for g in range(0,len(tim)):
		    sd=sd+float(tim[g]-avg)*float(tim[g]-avg)
		sd=float(sd)/z
		sd=math.sqrt(sd)
		print "Average time  of processes = %f "%(avg)
		#print "Standard Deviation = %f"%(sd)
		
	elif data==2:
		tim=[]
	    	total=0
	    	ts=time.time()
		result = dfs( starting_state, goal_state )
		te=time.time()
		totalt=float(total)+float(te-ts)
		tim.append(float(te-ts))
		avg=float(totalt)/z
		sd=0.0
		for g in range(0,len(tim)):
		    sd=sd+float(tim[g]-avg)*float(tim[g]-avg)
		sd=float(sd)/z
		sd=math.sqrt(sd)
		print "Average time  of processes = %f "%(avg)
		#print "Standard Deviation = %f"%(sd)
		
	elif data==3:
		
		tim=[]
	    	total=0
	    	ts=time.time()
		path,cost =  ufs(list(starting_state),list(goal_state))
		printPath(path,cost)
		#result2 = ucs( starting_state, goal_state )
		te=time.time()
		totalt=float(total)+float(te-ts)
		tim.append(float(te-ts))
		avg=float(totalt)/z
		sd=0.0
		for g in range(0,len(tim)):
		    sd=sd+float(tim[g]-avg)*float(tim[g]-avg)
		sd=float(sd)/z
		sd=math.sqrt(sd)
		print "Average time  of processes = %f "%(avg)
		#print "Standard Deviation = %f"%(sd)
		#print result2, " moves"
		#print "Cost is" 
		#print total_cost
		
	elif data==4:
		###result = bis( starting_state, goal_state )
		tim=[]
	    	total=0
	    	ts=time.time()
		result1= bidirec( starting_state, goal_state )
		###print "Steps in process" , result
		te=time.time()
		#print "%d.%f"%(i,te-ts)
		totalt=float(total)+float(te-ts)
		tim.append(float(te-ts))
		avg=float(totalt)/z
		sd=0.0
		for g in range(0,len(tim)):
		    sd=sd+float(tim[g]-avg)*float(tim[g]-avg)
		sd=float(sd)/z
		sd=math.sqrt(sd)
		print "Average time  of processes = %f "%(avg)
		#print "Standard Deviation = %f"%(sd)
		print result1, " moves"
	if data >=1 and data <=2:	
		if result == None :
			print "No solution found"
		elif result == [None]:
			print "Start node was the goal!"
		else:
			print result
			print len(result), " moves"
		
	

if __name__ == "__main__":
	main()


