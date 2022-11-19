import ast

def ast_parser(file):
    tree = ast.parse(file)
    print(ast.dump(tree, indent=3))
    return