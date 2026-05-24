class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = [] 
        
        my_dict = {")" : "(", "]" : "[", "}" : "{"}

        for i in s:
            if i in my_dict:
                if my_stack and my_stack[-1] == my_dict[i]:
                    my_stack.pop()
                else:
                    return False
            else: 
                my_stack.append(i)
        
        return True if not my_stack else False
            

            