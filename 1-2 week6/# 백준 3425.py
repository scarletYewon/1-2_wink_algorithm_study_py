# 백준 3425
import sys

input = sys.stdin.readline

def command(commands, num):
    stack = [num]
    for cmd in commands:
        if cmd[:3] == "NUM":
            n = int(cmd[4:])
            stack.append(n)
        elif cmd == "POP":
        elif cmd == "INV":
        elif cmd == "DUP":
        elif cmd == "SWP":
        elif cmd == "ADD":
        elif cmd == "SUB":
        elif cmd == "POP":
        elif cmd == "POP":

        elif not stack:
            return "Error"