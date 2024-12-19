import logging

from sympy import simplify
from dotenv import load_dotenv
from ceo import (
    Agent,
    Personality,
    get_openai_model,
    agentic,
    ability
)

load_dotenv()
logging.getLogger('ceo').setLevel(logging.DEBUG)
model = get_openai_model()


@ability
def calculator(expr: str) -> float:
    # this function only accepts a single math expression
    return simplify(expr)


@ability
def write_file(filename: str, content: str) -> str:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return f'{content} written to {filename}.'


jack = Agent(abilities=[calculator], brain=model, name='Jack', personality=Personality.INQUISITIVE)
tylor = Agent(abilities=[write_file], brain=model, name='Tylor', personality=Personality.PRUDENT)


@agentic(jack)
def agent1():
    return


@agentic(tylor)
def agent2():
    return


if __name__ == '__main__':
    ceo = Agent(abilities=[agent1, agent2], brain=model, name='CEO', personality=Personality.INQUISITIVE)
    ceo.assign("Here is a sphere with radius of (1 * 9.5 / 2 * 2) cm and pi here is 3.14159, find the area and volume respectively then write the results into a file called 'result.txt'.")
    result = ceo.just_do_it()
    print(result)