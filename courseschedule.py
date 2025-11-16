class Solution(object):
    def hasCycle(self, course, seen, graph):
        
        if course in seen:
            return True
        
        if course not in graph:
            return False
        
        seen.add(course)

        
        for neighbour in graph[course]:
            if(self.hasCycle(neighbour,seen, graph)):
             return True

        seen.remove(course)    

        return False

    def canFinish(self, numCourses, preprequisites):
        graph = {}
        for prereq in preprequisites:
            if(prereq[0] in graph):
               graph[prereq[0]].append(prereq[1])
            else:
                graph[prereq[0]] = [prereq[1]]
        print(graph)   
        for course in range(numCourses):
            if(self.hasCycle(course,set(),graph)):
               return False
       
    
        return True
    
#print(Solution().canFinish(2,[[1,0]]))
#True    
print(Solution().canFinish(2,[[1,0],[0,1]]))
#False    