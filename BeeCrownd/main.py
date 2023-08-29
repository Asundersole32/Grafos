class Nodes:
    def _init_(self, value):
        self.key = value
        self.left = None
        self.right = None


def build_expression(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    operators_list = []
    values_list = []

    for i in expression:
        if i.isdigit() or i.isalpha():
            values_list.append(Nodes(i))
        elif i in "+-*/":
            while (operators_list and operators_list[-1] != '(' and
                   precedence[i] <= precedence.get(operators_list[-1], 0)):
                try:
                    op_value = operators_list.pop()
                    right = values_list.pop()
                    left = values_list.pop()
                    node = Nodes(op_value)
                    node.left = left
                    node.right = right
                    values_list.append(node)
                except IndexError:
                    pass
                except Exception as error:
                    print("Error:", error)
                    return None
            operators_list.append(i)
        elif i == '(':
            operators_list.append(i)
        elif i == ')':
            while operators_list[-1] != '(':
                try:
                    op_value = operators_list.pop()
                    right = values_list.pop()
                    left = values_list.pop()
                    node = Nodes(op_value)
                    node.left = left
                    node.right = right
                    values_list.append(node)
                except IndexError:
                    pass
                except Exception as error:
                    print("Error:", error)
                    return None
            operators_list.pop()

    while operators_list:
        try:
            op_value = operators_list.pop()
            right = values_list.pop()
            left = values_list.pop()
            node = Nodes(op_value)
            node.left = left
            node.right = right
            values_list.append(node)
        except IndexError:
            pass
        except Exception as error:
            print("Error:", error)
            return None

    return values_list[0]


def print_levels(root):
    queue = [(root, 0)]
    current_level = -1

    while queue:
        node, level = queue.pop(0)
        if level > current_level:
            if current_level >= 0:
                print()
            current_level = level
            print(f"Nivel {current_level}:", end=" ")

        print(node.value, end="")

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    print()


expressions = []
while True:
    try:
        expression_input = input().strip()
        if not expression_input:
            break
        expressions.append(expression_input)
    except EOFError:
        break

for index, expression in enumerate(expressions):
    root = build_expression(expression)
    if root:
        print_levels(root)
        if not len(expressions) - 1 == index:
            print()