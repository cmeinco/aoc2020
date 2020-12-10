
# class Node(object):
#     def __init__(self, value, parent):
#         self.value = value
#         self.children = []
#     def add_child(self, obj):
#         self.children.append(obj)

def reducetree(tree):
    cuttree={}

    # for x in tree.keys():
    #     cuttree[x]={}
    #     cuttree[x]["children"]=[]
    #     cuttree[x]["parentcount"]=0

    # if parentcount=1, reduce it.
    # if key==0, skip

    # Rule 1, 1:1 remap/reduce
    for x in tree.keys():
        if x>0:
            if len(tree[x]["children"]) == 1:
                #if tree[x]["parentcount"] == 1 
                # find where it's the child, replace with it's own child
                for z in range(x-4,x+4):
                    if tree.get(z):
                        if x in tree[z]["children"]:
                            for i in range(0,len(tree[z]["children"])):
                                if tree[z]["children"][i] == x:
                                    tree[z]["children"][i] = tree[x]["children"][0]
            else:
                if not cuttree.get(x):
                    cuttree[x]={}
                    cuttree[x]["children"]=[]
                    cuttree[x]["parentcount"]=0
                cuttree[x]["children"].extend(tree[x]["children"])
                cuttree[x]["parentcount"]=tree[x]["parentcount"]
        else:
            if not cuttree.get(x):
                cuttree[x]={}
                cuttree[x]["children"]=[]
                cuttree[x]["parentcount"]=0
            cuttree[x]["children"].extend(tree[x]["children"])
            cuttree[x]["parentcount"]=tree[x]["parentcount"]



    return cuttree

def y2020_d10_star02_pathcount(tree,calltimes=0,key=0):
    if calltimes%90==0:
        print(f"{calltimes = } {key =}",flush=True)
    pathcount=0
    if key>0 and len(tree[key]["children"]) == 0:
        return 1
    for child in tree[key]["children"]:
        pathcount+=y2020_d10_star02_pathcount(tree,calltimes+1,child)    
    return pathcount

def f(T, k):
  if not T["children"]:
    return [0, 0]

  result = [0, 0]

  for c in T["children"]:
    [a, b] = f(c, k)
    result[1] += a + b

    if T["value"] >= k <= c["value"]:
      # One valid path from T to c
      # plus extending all the paths
      # that start at c
      result[0] += 1 + a

  return result

def y2020_d10_star02(input):
    
    tree={}
 
    walladapter=0
    
    tree[0]={}
    tree[0]["children"]=[]
    tree[0]["parentcount"]=0
    tree[0]["parents"]=[]
    tree[0]["pathcount"]=1
    
    #nodelist.append(new Node(walladapter))
    
    lines = [0]
    for line in input.split("\n"):
        if len(line)>0:
            lines.append(int(line))
    lines.sort()
    #print(f"{lines = }")
    devicejolts=((lines[len(lines)-1])+3)
    #print(f"Set Device Jolts to: {devicejolts = }")
    lines.append(devicejolts)
    
    
    for x in range(0,len(lines)):
        if not tree.get(lines[x]):
            tree[lines[x]]={}
            tree[lines[x]]["children"]=[]
            tree[lines[x]]["parentcount"]=0
            tree[lines[x]]["parents"]=[]
            tree[lines[x]]["pathcount"]=0
                    
    for x in range(0,len(lines)):
        for y in range(0,len(lines)):
            if lines[x]!=lines[y]:
                if (lines[y]-1) == lines[x] or (lines[y]-2) == lines[x] or (lines[y]-3) == lines[x]: 
                    # add as child
                    tree[lines[x]]["children"].append(lines[y])
                    tree[lines[y]]["parents"].append(lines[x])
                    tree[lines[y]]["parentcount"]+=1

    for x in range(0,len(lines)):
        for p in tree[lines[x]]["parents"]:
            tree[lines[x]]["pathcount"]+=tree[p]["pathcount"]
        
    return tree[lines[len(lines)-1]]["pathcount"]


#     prevadapter=walladapter
#     for x in range(0,len(lines)):
#         if not tree.get(lines[x]):
#             tree[lines[x]]={}
#             tree[lines[x]]["children"]=[]
#             tree[lines[x]]["parentcount"]=0
#         for z in range(1,len(lines)):
#             if lines[z]!=lines[x]:
#                 if not tree.get(lines[z]):
#                     tree[lines[z]]={}
#                     tree[lines[z]]["children"]=[]
#                     tree[lines[z]]["parentcount"]=0
#                 if (lines[z]-1) == prevadapter or (lines[z]-2) == prevadapter or (lines[z]-3) == prevadapter: 
#                     if not lines[z] in tree[prevadapter]["children"]:
#                         tree[prevadapter]["children"].append(lines[z])
#                         tree[lines[z]]["parentcount"]+=1
                    
#         prevadapter=lines[x]
    
    
    

    # totalpaths=1
    # for x in tree.keys():
    #     if x!= lines[len(lines)-1]:
    #         #print(abs(len(tree[x]["children"])-tree[x]["parentcount"]))
    #         pc=abs(len(tree[x]["children"])-tree[x]["parentcount"])
    #         tree[x]["paths"]=abs(len(tree[x]["children"])-tree[x]["parentcount"])
    #         if pc>1:
    #             totalpaths*=tree[x]["paths"]
    #     print(f"{tree[x] = } {pc =} { totalpaths = }")

    # print(f"Total Paths: {totalpaths = }")

    #print(f"{len(tree.keys()) = } {tree = }")

    #return tree[devicejolts]["parentcount"]
    #return y2020_d10_star02_pathcount(tree)
    #newtree = reducetree(tree)
    #print(f"{len(newtree.keys()) = } {newtree = }")
    #return 0
    #return y2020_d10_star02_pathcount(newtree)
    return totalpaths


def getInput():
    return """26
97
31
7
2
10
46
38
112
54
30
93
18
111
29
75
139
23
132
85
78
99
8
113
87
57
133
41
104
98
58
90
13
91
20
68
103
127
105
114
138
126
67
32
145
115
16
141
1
73
45
119
51
40
35
150
118
53
80
79
65
135
74
47
128
64
17
4
84
83
147
142
146
9
125
94
140
131
134
92
66
122
19
86
50
52
108
100
71
61
44
39
3
72
"""

def getTestInput1():
    return """16
10
15
5
1
11
7
19
6
12
4
"""

def getTestInput2():
    return """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

if __name__ == "__main__":
    print(f"TestInput1: {y2020_d10_star02(getTestInput1())}")

    print(f"TestInput2: {y2020_d10_star02(getTestInput2())}")


    print(f"Final Input: {y2020_d10_star02(getInput())}")
