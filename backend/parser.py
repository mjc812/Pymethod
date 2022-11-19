import ast

def trace_calls(file):
    tree = ast.parse(file)
    print(ast.dump(tree, indent=3))
    return