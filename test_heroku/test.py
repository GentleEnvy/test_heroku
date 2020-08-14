import sys

print(sys.argv)
DEBUG = bool(int(sys.argv[1]))
print(f'DEBUG = {DEBUG}')
