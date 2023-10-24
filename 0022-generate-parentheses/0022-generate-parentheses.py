class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def solver(numOpen, numClosed, parenthesis):
            if len(parenthesis) == (n * 2): 
                result.append(parenthesis)
                return 
            if numClosed < numOpen: 
                parenthesis += ")"
                solver(numOpen, numClosed + 1, parenthesis)
                parenthesis = parenthesis[:-1]
            if numOpen < n:
                parenthesis += "("
                solver(numOpen + 1, numClosed, parenthesis)
                parenthesis = parenthesis[:-1]
        
        solver(0, 0, "")
        return result


#["((()))","(()())","(())()","()(())","()()()"]
#["()()()"]
#["(()())"]
#If no open parenthesis to the left, an closed parenthesis is not allowed (closed == open, I won't allow greater)
#If numOpenParanthesis >= n no open parenthesis is allowed 
#[""]