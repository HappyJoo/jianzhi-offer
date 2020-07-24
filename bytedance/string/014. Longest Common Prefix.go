// Vertical
// Time complexity: O(mn) m is average length of strings. n is number of strings.
func longestCommonPrefix(strs []string) string {
    if len(strs) == 0 {
        return ""
    }

    for i := 0; i < len(strs[0]); i++ {
        for j := 0; j < len(strs); j++ {
            // Either strs[j] has the same length with strs[0] or the character are not equal.
            if i == len(strs[j]) || strs[j][i] != strs[0][i] { 
                return strs[0][:i]
            }
        }
    }

    return strs[0]
}

// One by one
// Time complexity: O(mn) m is average length of strings. n is number of strings.
func longestCommonPrefix(strs []string) string {
    if len(strs) == 0 {
        return ""
    }

    prefix := strs[0]

    for i := 0; i < len(strs); i++ {
        prefix = lcp(prefix, strs[i])
        if len(prefix) == 0 {
            break
        }
    }

    return prefix
}

func lcp(str1, str2 string) string {
    length := min(len(str1), len(str2))
    index := 0
    for index < length && str1[index] == str2[index] {
        index++
    }
    return str1[:index]
}

func min(n1, n2 int) int {
    if n1 < n2 {
        return n1
    }
    return n2
}