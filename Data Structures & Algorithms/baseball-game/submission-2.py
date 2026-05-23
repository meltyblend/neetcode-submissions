class Solution:
    def calPoints(self, operations: List[str]) -> int:

        my_stack = []
        sum = 0
        ans = 0

        for i in range(len(operations)):
            if operations[i].lstrip('-').isdigit() == True:
                num = int(operations[i])
                my_stack.append(num)

            elif operations[i] == "+":
                sum = my_stack[-1] + my_stack[-2]
                my_stack.append(sum)

            elif operations[i] == "D":
                double = 2 * my_stack[-1]
                my_stack.append(double)
                
            elif operations[i] == "C":
                my_stack.pop()

        for k in range(len(my_stack)):
            ans += my_stack[k]
        return ans


