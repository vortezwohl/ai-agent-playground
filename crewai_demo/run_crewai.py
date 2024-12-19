import os

if __name__ == '__main__':
    os.environ['VIRTUAL_ENV'] = './.venv'
    print('crewai starts.')
    os.system('crewai run')
