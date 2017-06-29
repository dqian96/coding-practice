// Problem: Valid Paranthesis
// (https://leetcode.com/problems/valid-parentheses/#/description)

func isValid(s string) bool {
    array := make([]rune, len(s))
    stack := array[:0]
    for _, element := range s {
        if element == '(' || element == '{' || element == '[' {
            stack = append(stack, element)
        } else if len(stack) > 0 && (stack[len(stack) - 1] == element- 1 || stack[len(stack) - 1] == element - 2) {
            stack = stack[:len(stack) - 1]
        } else {
            return false
        }
    }
    if len(stack) == 0 {
        return true
    }
    return false
}
