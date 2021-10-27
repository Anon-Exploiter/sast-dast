'''
Parse bandit results and only return HIGH/MEDIUM results
'''

def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read(file_name).strip()

def main():
    bandit_output_file = '../bandit-output.json'
    file_contents = read_file(bandit_output_file)
    print(file_contents)

if __name__ == '__main__':
    main()