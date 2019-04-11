import turtle

def LSystemTransform(start, rules, n):
    prev = start
    for i in range(n):
        temp = ''
        for ch in prev:
            if ch in rules.keys():
                temp += rules[ch]
            else:
                temp += ch
        prev = temp
    return prev

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if (cmd == 'F' or cmd == 'f'):
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

#inst = LSystemTransform("F", {'F': 'F-F++F-F'}, 4)
inst = LSystemTransform("F", {'F': 'fF-FB++FB-B'}, 5)
print(inst)

t = turtle.Turtle()            
wn = turtle.Screen()

t.up()
t.back(200)
t.down()
t.speed(0)
#drawLsystem(t, inst, 60, 5)
drawLsystem(t, inst, 30, 20)   
wn.exitonclick()


