raw_input = open('input.txt','r').read().split('\n')
raw_input = [list(i) for i in raw_input]
input = list()
for i in raw_input: input.append([int(v) for v in i])

start = [0,0]
end = [12,12]

heatloss = 0
visited = list()
steps = 0

