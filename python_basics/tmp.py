def foo():
	print('foo')

def bar():
	print('bar')

functions = [ foo, bar ]
print(functions)

x = functions[-1]
x()

