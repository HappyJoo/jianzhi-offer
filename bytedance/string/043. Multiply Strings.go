func multiply(num1 string, num2 string) string {
    if num1 == "0" || num2 == "0" {
        return "0"
    }
    
    l1, l2 := len(num1), len(num2)
    total := l1 + l2
    res := make([]int, total)
    
    sum := 0
    for i := l1 - 1; i >= 0; i-- {
        for j := l2 - 1; j >= 0; j-- {
            sum = res[i + j + 1] + int(num1[i] - '0') * int(num2[j] - '0')
            res[i + j + 1] = sum % 10
            res[i + j] += sum / 10
        }
    }
    
    re := ""
    for k, v := range res {
        if k == 0 && v == 0 {
            continue
        }
        re += string(v + '0')
    }
    return re
}