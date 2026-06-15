class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        output = []
        visit = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
''' 
        print(f"numCourses = {numCourses}")
        print(f"prerequisites = {prerequisites}")
        prereq = {c: [] for c in range(numCourses)}
        print(f"prereq = {prereq}")
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        print(f"prereq = {prereq}")

        output = []
        print(f"output = {output}")
        visit, cycle = set(), set()
        print(f"visit = {visit}")
        print(f"cycle = {cycle}")

        def dfs(crs):
            print("...........................................................")
            print(f"dfs({crs}), crs = {crs}")
            if crs in cycle:
                print(f"{crs} in cycle = {cycle}, return False")
                return False
            if crs in visit:
                print(f"{crs} in visit = {visit}, return True")
                return True
            print(f"cycle = {cycle}")
            cycle.add(crs)
            print(f"cycle.add({crs}) = {cycle}")
            for pre in prereq[crs]:
                print(f"pre in prereq[{crs}] = {pre}")
                print(f"calling dfs({pre}) to check, if dfs({pre}) == False then return False else continue the loop")
                if dfs(pre) == False:
                    return False
            print(f"cycle = {cycle}")
            cycle.remove(crs)
            print(f"cycle after cycle.remove({crs}) = {cycle}")
            print(f"visit = {visit}")
            visit.add(crs)
            print(f"visit after visit.add({crs}) = {visit}")
            print(f"output = {output}")
            output.append(crs)
            print(f"output after output.append({crs}) = {output}")
            print(f"return True")
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output  
'''     