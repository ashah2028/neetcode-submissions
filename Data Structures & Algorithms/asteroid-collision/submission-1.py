class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #index is space
        #asteriods wont collide going same direction
        #collide if opposite 
        
        #put the positive asteroids in a stack

        #if negative you check with stack and if explosion you pop

        #stack 
        stack = []
        for ast in asteroids:
            alive = True
            #case if neg asteroid first
            #first consider negative case
            while ast < 0 and stack and stack[-1] > 0 and alive:
                #check if greater or less than stack[-1]
                if stack[-1] < abs(ast):
                    stack.pop()
                elif stack[-1] == abs(ast):
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(ast)
        return stack
