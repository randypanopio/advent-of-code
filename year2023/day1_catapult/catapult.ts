import { processInputFile } from "../input_analyzer";

const findNumberPairsPerEntryAndSum = (input: string[]) => {
    let ans: number[] = []
    let l_digit: string = ""
    let r_digit: string = ""
    input.forEach((entry) => {
        for (let i = 0; i < entry.length; i++){
            if (entry[i] >= '0' && entry[i] <= '9'){
                l_digit = entry[i]
            }
        }
        for (let j = entry.length -1; j >=0; j--){
            if (entry[j] >= '0' && entry[j] <= '9'){
                r_digit = entry[j]
            }
        }
        // force concat as a string, then revert back to num
        let number: number = parseInt("" + l_digit + r_digit)
        ans.push(number)
    });
    return ans
}

let inp : string[] = processInputFile('year2023/day1_catapult/input.txt')
console.log(findNumberPairsPerEntryAndSum(inp).reduce((a, b) => a + b, 0))