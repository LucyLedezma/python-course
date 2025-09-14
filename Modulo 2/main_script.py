import random

print(f'imported module name: {random.__name__}')
if __name__ == '__main__':
    choices = [10, 30, 60]
    print('Executing from main block.')
    print(f'Selected choice: {random.choice(choices)}')