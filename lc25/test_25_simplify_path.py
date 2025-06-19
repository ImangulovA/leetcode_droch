from 25_simplify_path import Solution

def test_example1():
    sol = Solution()
    assert sol.simplifyPath("/home/") == "/home"

def test_example2():
    sol = Solution()
    assert sol.simplifyPath("/../") == "/"

def test_example3():
    sol = Solution()
    assert sol.simplifyPath("/home//foo/") == "/home/foo"
