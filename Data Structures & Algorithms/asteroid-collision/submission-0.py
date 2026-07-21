class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #Just need to return the asteroids that not exploded
        #Since pos never meets, need to check with negs to see if explosion
        #Stack where i keep popping until neg one is exploded or stack empty
        #In the end return whatever is left on the stack

        stack = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                diff = ast + stack[-1]
                #ast bigger
                if diff < 0:
                    stack.pop()
                #ast smaller (destroy)
                elif diff > 0:
                    ast = 0
                #same size destroy both)
                else:
                    ast = 0
                    stack.pop()
            #truth value ast = 0 -> destroyed
            if ast:
                stack.append(ast)
        return stack



        