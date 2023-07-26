colours = ['red', 'green', 'blue', 'white', 'black']
backward_colours = []
def coloursReversed():
    for rcolour in colours:
        new = ""
        for i in range(len(rcolour) -1 ,-1, -1):
            new = new + rcolour[i]
        
        backward_colours.append(new)
coloursReversed()
print(backward_colours)