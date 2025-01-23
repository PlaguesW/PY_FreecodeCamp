def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = []
    bottom_line = []
    separator_line = []
    solution_line = []

    # Iterate over each problem
    for prob in problems:
        parts = prob.split()  # Split the problem into operands and operator

        if len(parts) != 3:
            return "Error: Each problem must have two operands and an operator."

        left_operand, operator, right_operand = parts

        # Check if operator is valid
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Validate operands: must be digits only, length <= 4
        if not (left_operand.isdigit() and right_operand.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(left_operand) > 4 or len(right_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine spacing
        # The width needed is the maximum length of the two operands + 2 (for operator + 1 space)
        max_len = max(len(left_operand), len(right_operand))
        width = max_len + 2

        # Build the lines
        # right-align the operands
        top_line.append(left_operand.rjust(width))
        bottom_line.append(operator + right_operand.rjust(width - 1))
        separator_line.append("-" * width)

        if solve:
            # Compute the result
            if operator == "+":
                answer = str(int(left_operand) + int(right_operand))
            else:
                answer = str(int(left_operand) - int(right_operand))
            solution_line.append(answer.rjust(width))

    # Join everything with 4 spaces between problems
    arranged_top = "    ".join(top_line)
    arranged_bottom = "    ".join(bottom_line)
    arranged_sep = "    ".join(separator_line)

    if solve:
        arranged_solution = "    ".join(solution_line)
        arranged_problems = (
            arranged_top + "\n" +
            arranged_bottom + "\n" +
            arranged_sep + "\n" +
            arranged_solution
        )
    else:
        arranged_problems = (
            arranged_top + "\n" +
            arranged_bottom + "\n" +
            arranged_sep
        )

    return arranged_problems
