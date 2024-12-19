import os

if __name__ == '__main__':
    os.environ['VIRTUAL_ENV'] = './.venv'
    print('CrewAI project starts.')
    os.system('crewai install')
    os.system('crewai run')
