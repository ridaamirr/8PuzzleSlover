from queue import Queue
import heapq
import time
import tracemalloc

def moveleft(tempconfg,confg,zeropos):
	tempconfg = tempconfg[:zeropos-1] + '0' + tempconfg[zeropos:]
	tempconfg = tempconfg[:zeropos] + confg[zeropos-1] + tempconfg[zeropos+1:]
	return tempconfg
def moveright(tempconfg,confg,zeropos):
	tempconfg = tempconfg[:zeropos+1] + '0' + tempconfg[zeropos+2:]
	tempconfg = tempconfg[:zeropos] + confg[zeropos+1] + tempconfg[zeropos+1:]
	return tempconfg
def moveup(tempconfg,confg,zeropos):
	tempconfg = tempconfg[:zeropos-3] + '0' + tempconfg[zeropos-2:]
	tempconfg = tempconfg[:zeropos] + confg[zeropos-3] + tempconfg[zeropos+1:]
	return tempconfg
def movedown(tempconfg,confg,zeropos):
	tempconfg = tempconfg[:zeropos+3] + '0' + tempconfg[zeropos+4:]
	tempconfg = tempconfg[:zeropos] + confg[zeropos+3] + tempconfg[zeropos+1:]
	return tempconfg

class Node:
	def __init__(self, c="",d=0,p=None):
		self.distancefromroot=d
		self.confg = c
		self.parent=p

	def setconfg(self, c):
		self.confg = c

	def getconfg(self):
		return self.confg

	def getdis(self):
		return self.distancefromroot

	def getparent(self):
		return self.parent

	def generateChildren(self):
		children = []
		if self.confg[4] == '0':
			tempconfg = self.confg
			children.append(Node(moveup(tempconfg,self.confg,4),self.distancefromroot+1,self))
			children.append(Node(movedown(tempconfg,self.confg,4),self.distancefromroot+1,self))
			children.append(Node(moveright(tempconfg,self.confg,4),self.distancefromroot+1,self))
			children.append(Node(moveleft(tempconfg,self.confg,4),self.distancefromroot+1,self))
		elif self.confg[0] == '0':
			tempconfg = self.confg
			# first child - moving right
			tempconfg = tempconfg[:1] + '0' + tempconfg[2:]
			tempconfg = self.confg[1] + tempconfg[1:]
			children.append(Node(tempconfg,self.distancefromroot+1,self))

			tempconfg = self.confg
			# second child - moving down
			tempconfg = tempconfg[:3] + '0' + tempconfg[4:]
			tempconfg = self.confg[3] + tempconfg[1:]
			children.append(Node(tempconfg,self.distancefromroot+1,self))
		elif self.confg[2] == '0':
			tempconfg = self.confg
			children.append(Node(moveleft(tempconfg,self.confg,2),self.distancefromroot+1,self))
			children.append(Node(movedown(tempconfg,self.confg,2),self.distancefromroot+1,self))
		elif self.confg[8] == '0':
			tempconfg = self.confg
			# first child - moving left
			tempconfg = tempconfg[:7] + '0' + tempconfg[8:]
			tempconfg = tempconfg[:8]+ self.confg[7]
			children.append(Node(tempconfg,self.distancefromroot+1,self))

			tempconfg = self.confg
			# second child - moving up
			tempconfg = tempconfg[:5] + '0' + tempconfg[6:]
			tempconfg = tempconfg[:8]+ self.confg[5]
			children.append(Node(tempconfg,self.distancefromroot+1,self))
		elif self.confg[6] == '0':
			tempconfg = self.confg
			children.append(Node(moveright(tempconfg,self.confg,6),self.distancefromroot+1,self))
			children.append(Node(moveup(tempconfg,self.confg,6),self.distancefromroot+1,self))
		elif self.confg[1] == '0':
			tempconfg = self.confg
			children.append(Node(moveright(tempconfg,self.confg,1),self.distancefromroot+1,self))
			children.append(Node(moveleft(tempconfg,self.confg,1),self.distancefromroot+1,self))
			children.append(Node(movedown(tempconfg,self.confg,1),self.distancefromroot+1,self))
		elif self.confg[3] == '0':
			tempconfg = self.confg
			children.append(Node(movedown(tempconfg,self.confg,3),self.distancefromroot+1,self))
			children.append(Node(moveright(tempconfg,self.confg,3),self.distancefromroot+1,self))
			children.append(Node(moveup(tempconfg,self.confg,3),self.distancefromroot+1,self))
		elif self.confg[5] == '0':
			tempconfg = self.confg
			children.append(Node(moveup(tempconfg,self.confg,5),self.distancefromroot+1,self))
			children.append(Node(movedown(tempconfg,self.confg,5),self.distancefromroot+1,self))
			children.append(Node(moveleft(tempconfg,self.confg,5),self.distancefromroot+1,self))
		elif self.confg[7] == '0':
			tempconfg = self.confg
			children.append(Node(moveright(tempconfg,self.confg,7),self.distancefromroot+1,self))
			children.append(Node(moveleft(tempconfg,self.confg,7),self.distancefromroot+1,self))
			children.append(Node(moveup(tempconfg,self.confg,7),self.distancefromroot+1,self))
		return children

	def __lt__(self, other):
			return self.distancefromroot < other.distancefromroot

	def printconfg(self):
		print(self.confg[0]," ",self.confg[1]," ",self.confg[2])
		print(self.confg[3]," ",self.confg[4]," ",self.confg[5])
		print(self.confg[6]," ",self.confg[7]," ",self.confg[8])
		print("----------")

def printpath(node):
	if node == None:
		return
	printpath(node.getparent())
	i=node.getconfg()
	print(i[0]," ",i[1]," ",i[2])
	print(i[3]," ",i[4]," ",i[5])
	print(i[6]," ",i[7]," ",i[8])
	print("----------")


def PrintResults(node,visited,memory):
	print("Memory Used: ",memory)
	print("Path Cost: ",node.distancefromroot)
	print("No of Node Visited: ",visited)
	print("---------------------")
	printpath(node)
	return 1


def BFS(StartState, GoalState):
	visited=[]
	visited.append(StartState.getconfg())
	q = Queue()
	q.put(StartState)

	while not q.empty():
		u = q.get()
		Children=u.generateChildren()
		for child in Children:
			if child.getconfg() not in visited:
				visited.append(child.getconfg())
				q.put(child)
				if GoalState.getconfg() == child.getconfg():
					return child,len(visited)

	return None,None

def DFS(StartState,GoalState):
	stack = [StartState]
	visited=[]
	while stack:
		u = stack.pop()
		visited.append(u.getconfg())
		if GoalState.getconfg() == u.getconfg():
			return u,len(visited)
		Children=u.generateChildren()
		for child in Children:
			if child.getconfg() not in visited:
				stack.append(child)
	return None,None


def UCS(StartState,GoalState):
	heap=[]
	heapq.heappush(heap,StartState)
	visited=[]

	while heap:
		u = heapq.heappop(heap)
		visited.append(u.getconfg())
		if GoalState.getconfg() == u.getconfg():
			return u,len(visited)
		Children=u.generateChildren()
		for child in Children:
			if child.getconfg() not in visited:
				heapq.heappush(heap, child)
	return None ,None

def DLS(StartState,GoalState,depth,visited):
	visited.append(StartState.getconfg())
	if GoalState.getconfg() == StartState.getconfg():
			return StartState,len(visited)
	if depth==0:
		return None,len(visited)
	Children=StartState.generateChildren()
	for child in Children:
		if child.getconfg() not in visited:
			r1,r2=DLS(child,GoalState,depth-1,visited)
			if r1:
				return r1,r2
	return None,len(visited)

def IDS(StartState,GoalState):
	depth=1
	total_visited=0
	while True:
		visited=[]
		r1,r2=DLS(StartState,GoalState,depth,visited)
		total_visited+=r2
		if r1:
			return r1,total_visited
		depth=depth+1

print("Select Algorithm:\n1.DFS\n2.BFS\n3.IDS\n4.UCS")
Algo=int(input("Seclected Algorithm: "))
st="312458067"
gt="012345678"
StartState = Node(st)
GoalState = Node(gt)
print("---------------------")
if Algo == 1:
	print("DFS Algorithm")
elif Algo == 2:
	print("BFS Algorithm")
elif Algo == 3:
	print("IDS Algorithm")
elif Algo == 4:
	print("UCS Algorithm")
print("---------------------")

if Algo == 1:
	starttime=time.time()
	tracemalloc.start()
	node,lenvisited=DFS(StartState,GoalState)
	snapshot = tracemalloc.take_snapshot()
	mem=tracemalloc.get_traced_memory()
	tracemalloc.stop()
	mem=mem[1]-mem[0]
	print("Time Taken: ",time.time()-starttime," seconds")
	PrintResults(node,lenvisited,mem)
elif Algo == 2:
	starttime=time.time()
	tracemalloc.start()
	node,lenvisited=BFS(StartState,GoalState)
	snapshot = tracemalloc.take_snapshot()
	mem=tracemalloc.get_traced_memory()
	tracemalloc.stop()
	mem=mem[1]-mem[0]
	print("Time Taken: ",time.time()-starttime," seconds")
	PrintResults(node,lenvisited,mem)
elif Algo == 3:
	starttime=time.time()
	tracemalloc.start()
	node,lenvisited=IDS(StartState,GoalState)
	snapshot = tracemalloc.take_snapshot()
	mem=tracemalloc.get_traced_memory()
	tracemalloc.stop()
	mem=mem[1]-mem[0]
	print("Time Taken: ",time.time()-starttime," seconds")
	PrintResults(node,lenvisited,mem)
else:
	starttime=time.time()
	tracemalloc.start()
	node,lenvisited=UCS(StartState,GoalState)
	snapshot = tracemalloc.take_snapshot()
	mem=tracemalloc.get_traced_memory()
	tracemalloc.stop()
	mem=mem[1]-mem[0]
	print("Time Taken: ",time.time()-starttime," seconds")
	PrintResults(node,lenvisited,mem)

if not node:
	print("Solution could not be found")


