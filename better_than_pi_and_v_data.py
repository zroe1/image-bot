import random
import numpy as np
import matplotlib.pyplot as plt

def generate_operation():
    """ Returns a random arithmetic operation symbol.

    If a random integer between 0 and 1 is 1, returns '+'. Otherwise, returns
    a random choice among '+', '-', '*', and '/'.
    """
    return random.choice(["+", "-", "*", "/"])

def generate_equation(num_terms):
    """ Generates an equation with 'num_terms' as coefficients or coefficients
    with 'x', interspersed with random arithmetic operations. Coefficients range
    from 1 to 10, with a 30% chance of including 'x' in each term.

    Parameters:
    - num_terms (int): Number of terms in the equation.

    Returns:
    - list[str]: Equation components.
    """
    terms = []
    for i in range(num_terms):
        coeficient = random.randint(1, 10)
        if random.randint(1, 10) > 3:
          terms.append(str(coeficient))
        else:
          terms.append(str(coeficient) + "x")
        if i < num_terms - 1:
          terms.append(generate_operation())
    return terms

def generate_simple_linear_question(num_terms):
    """ Generates an equation with in the same manner as "generate_equation
    but without only addition as an operation between terms.
    """
    terms = []
    for i in range(num_terms):
        coeficient = random.randint(1, 10)
        if random.randint(1, 10) > 4:
          terms.append(str(coeficient))
        else:
          terms.append(str(coeficient) + "x")
        if i < num_terms - 1:
          terms.append('+')
    return terms

def get_xs_and_ys(equation):
  equation_copy = [n for n in equation]
  colapse_multiplication_and_division(equation_copy)
  # print("here!")
  # print(equation_copy)

  xs = np.arange(0.1, 10.1, 0.1)
  ys = np.full(xs.shape, 0.0)
  ys_temp = np.array([])

  for i, num in enumerate(equation_copy):
    if isinstance(num, np.ndarray):
      ys_temp = num
    elif num in ["+", "-", "*", "/"]:
      continue
    elif 'x' in num:
      ys_temp = xs * float(num[0])
    else:
      ys_temp = np.full(xs.shape, float(num))
    if i > 0 and equation_copy[i - 1] == '-':
      ys -= ys_temp
    else:
      ys += ys_temp

  return xs, ys

def colapse_multiplication_and_division(equation):
  i = 0
  while i < len(equation):
    term = equation[i]
    # print(term)
    if term == '*' or term == '/':
      xs = np.arange(0.1, 10.1, 0.1)

      operation = equation[i]
      first_term = equation[i - 1]
      second_term = equation[i + 1]

      ys_temp_1 = np.array([])
      ys_temp_2 = np.array([])

      if isinstance(first_term, np.ndarray):
        ys_temp_1 = first_term
      elif 'x' in first_term:
        ys_temp_1 = xs * float(first_term[0])
      else:
        ys_temp_1 = np.full(xs.shape, float(first_term))

      if isinstance(second_term, np.ndarray):
        ys_temp_2 = second_term
      elif 'x' in second_term:
        ys_temp_2 = xs * float(second_term[0])
      else:
        ys_temp_2 = np.full(xs.shape, float(second_term))

      # print(equation[i-1:i+2])
      if operation == '*':
        equation[i] = ys_temp_1 * ys_temp_2
      else:
        equation[i] = ys_temp_1 / ys_temp_2
      equation.pop(i + 1)
      equation.pop(i - 1)
      # print(equation)
      i -= 1
    i += 1
  return equation

output_rows = 20
output_cols = 15

fig, axs = plt.subplots(output_rows, output_cols, figsize=(25, 12), dpi=50)

# plt.ylim([0, 50])

for row in axs:
  for ax in row:
    ax.set_ylim([0, 50])
    # ax.set_xlim([0, 10])

    # Remove both ticks and tick labels
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

for i in range(output_rows):
  for j in range(output_cols):
    e = generate_equation(6)
    x, y = get_xs_and_ys(e)
    axs[i][j].plot(x, y)

plt.show()