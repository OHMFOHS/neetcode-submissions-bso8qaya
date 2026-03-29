class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        close_to_open = {')' : '(', '}' : '{', ']' : '[' }
        for c in s:
            if c in '({[':
                st.append(c)
            else:
                if not st:
                    return False
                bracket = st.pop()
                if bracket != close_to_open[c]:
                    return False
        return False if st else True

