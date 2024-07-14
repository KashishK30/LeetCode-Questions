class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Helper function to parse the formula
        def parse_formula(formula):
            # Initialize a stack with a default dictionary to keep count of atoms
            stack = [defaultdict(int)]
            i, n = 0, len(formula)  # Initialize the index and the length of the formula
            
            while i < n:  # Loop through the formula
                if formula[i] == '(':  # If we encounter '(', push a new dictionary onto the stack
                    stack.append(defaultdict(int))
                    i += 1  # Move to the next character
                elif formula[i] == ')':  # If we encounter ')', pop the top dictionary from the stack
                    top = stack.pop()
                    i += 1  # Move to the next character
                    i_start = i
                    while i < n and formula[i].isdigit():  # Read the multiplier if present
                        i += 1
                    multiplier = int(formula[i_start:i] or 1)  # Default multiplier is 1 if none is specified
                    for atom, count in top.items():  # Multiply counts of atoms inside parentheses by the multiplier
                        stack[-1][atom] += count * multiplier
                else:
                    i_start = i
                    i += 1
                    while i < n and formula[i].islower():  # Read the atom name
                        i += 1
                    atom = formula[i_start:i]  # Extract the atom name
                    i_start = i
                    while i < n and formula[i].isdigit():  # Read the count if present
                        i += 1
                    count = int(formula[i_start:i] or 1)  # Default count is 1 if none is specified
                    stack[-1][atom] += count  # Add the atom count to the top dictionary on the stack
            
            return stack[0]  # Return the final dictionary with atom counts
        
        atom_counts = parse_formula(formula)  # Parse the formula and get the atom counts
        result = []
        
        for atom in sorted(atom_counts):  # Sort atom names alphabetically
            count = atom_counts[atom]  # Get the count for each atom
            result.append(atom)  # Append the atom name to the result
            if count > 1:  # Append the count if it is greater than 1
                result.append(str(count))
        
        return ''.join(result)  # Join the result list into a string and return it