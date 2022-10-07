import random
from datetime import datetime, timedelta
import operator
from models.stacks import Stack


def list_all_operands():
    return {"operands": "add, mul, div, sub"}, 200


def apply_operand(**kwargs):
    stack = Stack.get_single(filters={'id': kwargs.get("stack_id")})
    if stack:
        my_stack = stack.as_dict().get("stack")
        if len(my_stack) > 1:
            ops = {"add": operator.add,
                   "sub": operator.sub,
                   "mul": operator.mul,
                   "div": operator.itruediv
                   }
            new_value = ops[kwargs.get("op")](my_stack[-1], my_stack[-2])
            new_list = my_stack[:len(my_stack)-2] + [int(new_value)]
            stack.update_row(data={'stack': new_list})

        return 201
    else:
        return "Bad request: stack not found ", 404


def create_new_stack(**kwargs):
    stack = Stack.add_data(**kwargs)
    return stack.as_dict(), 201


def get_stack(**kwargs):
    stack = Stack.get_single(filters={'id': kwargs.get("stack_id")})
    if not stack:
        return "Bad request: stack not found ", 404
    return stack.as_dict()


def get_all_stacks():
    stacks = Stack.get_all()
    list_stacks = [] if not stacks else [s.as_dict() for s in stacks]
    return {'stacks': list_stacks}, 200


def delete_stack(**kwargs):
    stack = Stack.get_single(filters={'id': kwargs.get("stack_id")})
    stack.delete_row()
    return "Stack deleted", 200


def push_value_stack(**kwargs):
    stack = Stack.get_single(filters={'id': kwargs.get("stack_id")})
    if stack:
        my_stack = stack.as_dict().get("stack")
        stack.update_row(data={'stack': my_stack.append(kwargs.get("value"))})
        return 201
    else:
        return "Bad request: stack not found ", 404
