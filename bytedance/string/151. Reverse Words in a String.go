// solution 1 shorter
func reverseWords(s string) string {
    s = strings.Trim(s, " ")
    i, j := len(s) - 1, len(s) - 1
    queue := []string{}
    for i >= 0 {
        for i >= 0 && s[i] != ' ' {
            i--
        }
        queue = append(queue, s[i+1:j+1])
        for i >= 0 && s[i] == ' ' {
            i--
        }
        j = i
    }

    // res := []byte{}
    // for k := len(queue) - 1; k >= 0; k-- {
    //     res = append(res, []byte(queue[k])...)
    //     res = append(res, ' ')
    // }
    
    rs := strings.Join(queue, " ")
    return rs
}


// solution 2
func reverseWords(s string) string {
    if s == "" {
        return ""
    }
    res := []byte{}
    queue := []string{}

    word := []byte{}
    for i := 0; i < len(s); i++ {
        if s[i] == ' ' {
            if len(word) > 0 {
                queue = append(queue, string(word))
                word = []byte{}
            }
        } else {
            word = append(word, s[i])
        }
    }
    if len(word) > 0 {
        queue = append(queue, string(word))
    }
    
    if len(queue) <= 0 {
        return ""
    }

    for i := len(queue) - 1; i >= 0; i-- {
        res = append(res, []byte(queue[i])...)
        res = append(res, ' ')
    }

    return string(res[:len(res)-1])
}
