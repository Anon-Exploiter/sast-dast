'''
Parse bandit results and only return HIGH/MEDIUM results
'''

def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read(file_name).strip()

def main():
    bandit_output = '../bandit-output.json'
    file_contents = read_file(bandit_output)

    print(file_contents)

if __name__ == '__main':
    main()