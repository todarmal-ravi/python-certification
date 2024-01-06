def arithmetic_arranger(problems, show_answers=False):
  # Check if the number of problems exceeds the limit
  if len(problems) > 5:
    return "Error: Too many problems."

  top_line = ""
  bottom_line = ""
  separator_line = ""
  answer_line = ""

  for problem in problems:
    elements = problem.split()

    if len(elements) != 3:
      return "Error: Each problem should have two operands and one operator."

    operand1, operator, operand2 = elements

    if not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits."

    if operator not in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."

    # Determine the length of the longest operand
    length = max(len(operand1), len(operand2)) + 2  # Add 2 for padding

    top_line += operand1.rjust(length) + "    "
    bottom_line += operator + operand2.rjust(length - 1) + "    "
    separator_line += "-" * length + "    "

    if show_answers:
      if operator == "+":
        result = str(int(operand1) + int(operand2))
      else:
        result = str(int(operand1) - int(operand2))
      answer_line += result.rjust(length) + "    "

  arranged_problems = top_line.rstrip() + "\n" + bottom_line.rstrip() + "\n" + separator_line.rstrip()

  if show_answers:
    arranged_problems += "\n" + answer_line.rstrip()

  return arranged_problems


print(arithmetic_arranger(["32 + 8", "1 / 3801", "9999 + 9999", "523 - 49"],True))
