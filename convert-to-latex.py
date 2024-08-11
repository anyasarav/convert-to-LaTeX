# ensure the OpenAI Python package is installed by using 'pip install openai' in cmd prompt
import openai
import re

openai.api_key = 'Your Open AI Key'

def equation_to_latex(equation):
    """Converts an equation to LaTeX format using OpenAI's API."""
    response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        messages=[
        {"role": "user", "content": f"Convert the equation '{equation}' to LaTeX. Make it compatible with React LaTeX by not wrapping equal signs. Remember to wrap individual elements in dollar signs."}],
        temperature=0,
        max_tokens=50,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    latex_equation = response.choices[0].message.content
    return latex_equation

def is_mathematical(text):
    """Check if text contains mathematical symbols."""
    return re.search(r'[+\-*/^=<>]', text) is not None

json_data = [
    {
        "question": "In the figure above, equilateral triangle WXY is inscribed in circle O. What is the measure, in radians, of angle WYO?",
        "options": [
            "A) $\\frac{\u03c0}{3}$ radians",
            "B) $\\frac{2\u03c0}{3}$ radians",
            "C) $\\frac{\u03c0}{2}$ radians",
            "D) \u03c0 radians"
        ]
    },
    {
        "question": "A wind turbine on a wind farm has a blade with a length of 60 meters and completes one rotation in 6 seconds. Find the angular velocity of the blade in radians per second.",
        "options": [
            "A) $\\frac{\u03c0}{6}$ radians per second",
            "B) $\\frac{\u03c0}{9}$ radians per second",
            "C) $\\frac{\u03c0}{12}$ radians per second",
            "D) $\\frac{\u03c0}{3}$ radians per second"
        ]
    }
    # add more test data as needed
]

for i, question_data in enumerate(json_data, start=1):
    print(f"Question {i}: {question_data['question']}")
    for option in question_data["options"]:
        print(option)
    print()

for question_data in json_data:
    question = question_data["question"]
    for option in question_data["options"]:
        if is_mathematical(option):
            latex_equation = equation_to_latex(option)
            print("Original Equation:", option)
            print("LaTeX Format:", latex_equation)
            print("\n")
