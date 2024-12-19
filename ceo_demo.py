import logging

from ceo import (
    Agent,
    Personality,
    get_openai_model,
    ability
)
from sympy import simplify
from dotenv import load_dotenv

load_dotenv()
logging.getLogger('ceo').setLevel(logging.DEBUG)
# logging.getLogger('ceo.prompt').setLevel(logging.DEBUG)


@ability
def calculator(expr: str) -> float:
    # this function only accepts a single math expression
    return simplify(expr)


@ability
def write_file(filename: str, content: str) -> str:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return f'{content} written to {filename}.'


if __name__ == '__main__':
    ceo = Agent(abilities=[calculator, write_file], brain=get_openai_model(), name='CEO', personality=Personality.INQUISITIVE)
    ceo.assign(r"这是一个半径为 (1 * 9.5 / 2 * 2) 厘米的球体，其中π取值为 3.14159，请分别计算其表面积和体积，然后将结果写入 D:\project\playground\result.txt，")
    result = ceo.just_do_it()
    print(result)
