class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        

        #approach #2 -> split based off "/""

        paths = path.split("/")

        for chars in paths:
            if chars == "..":
                if stack:
                    stack.pop()
            elif chars != "" and chars != ".":
                stack.append(chars) 
        return "/" + "/".join(stack)

#"/neetcode/practice//...///../courses"

#[, neetcode, practice, courses  ]
