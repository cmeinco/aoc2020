def y2020_d10_star01(input):
    
    onejdiff=0
    thrjdiff=0
    devicejolts=0
    
    lines = [0]
    for line in input.split("\n"):
        if len(line)>0:
            lines.append(int(line))
    
    lines.sort()
    
    print(f"{lines = }")
    devicejolts=((lines[len(lines)-1])+3)
    print(f"Set Device Jolts to: {devicejolts = }")
    
    lines.append(devicejolts)
    
    prevadapter=0
    for x in range(1,len(lines)):
        if (lines[x]-1) == prevadapter:
            onejdiff+=1
        if (lines[x]-3) == prevadapter: 
            thrjdiff+=1
        prevadapter=lines[x]
            
    print(f"Final: {onejdiff = } {thrjdiff = } ")
    return (onejdiff*thrjdiff)



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
    print(f"TestInput1: {y2020_d10_star01(getTestInput1())}")

    print(f"TestInput2: {y2020_d10_star01(getTestInput2())}")


    print(f"Final Input: {y2020_d10_star01(getInput())}")
