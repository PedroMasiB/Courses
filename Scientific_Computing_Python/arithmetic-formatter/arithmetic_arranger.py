import re


def arithmetic_arranger(problems, n = False):
    arranged_problems = []
    a_int = []
    try:  
        if not all(isinstance(problem, str) for problem in problems):
            print('Error: All problems must be strings.')
            return arranged_problems
          
        if len(problems) > 5:
            print('Error: Too many problems.')
            return arranged_problems
        
        for problem in problems:
            a = re.findall('[0-9.]+', problem)
            b = re.findall('[+\-*/%]', problem)
            
            if not a or not b:
                print('Error: No valid problems input')
                arranged_problems = []
                return arranged_problems
            
            for x in a:
                if x.isdigit() is False:
                    print('Error: Numbers must only contain digits.')
                    arranged_problems = []
                    return arranged_problems
                elif len(x) > 4:
                    print('Error: Numbers cannot be more than four digits.')
                    arranged_problems = []
                    return arranged_problems
            a_int = [int(x) for x in a]
            
            if b[0] != '+' and b[0] != '-':
                print('Error: Operator must be + or -')
                arranged_problems = []
                return arranged_problems

            if b[0] == '+':
                result = a_int[0] + a_int[1]
            else:
                result = a_int[0] - a_int[1]

            width = max(len(a[0]), len(a[1])) + 2
            arranged_problem = f'{a[0]:>{width}}\n{b[0]} {a[1]:>{width-2}}\n{"-" * width}'
            if n:
                arranged_problem += f'\n{result:>{width}}'
            
            arranged_problems.append(arranged_problem)

            
            
    except:
        print("Error")
    
    return arranged_problems