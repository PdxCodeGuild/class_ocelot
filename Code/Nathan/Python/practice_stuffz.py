from blessed import Terminal

t = Terminal()

print(t.bold('Hi there!'))
print(t.bold_red_on_bright_green('It hurts my eyes!'))

with t.location(0, t.height - 1):
    print(t.center(t.blink('press any key to continue.')))

with t.cbreak():
    inp = t.inkey()
print('You pressed ' + repr(inp))