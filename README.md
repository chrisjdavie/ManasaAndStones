# ManasaAndStones

Solving the hackerrank Manasa And Stones puzzle

https://www.hackerrank.com/challenges/manasa-and-stones

The "cleverness" here comes from spotting the solution is a range from the minimum possible to the maximum possible values,
with the difference being the value of the swap. Computing all the values directly, or worse, the permutations, would 
result in a O(n**2) or O(n!) problem (I think). Solution is O(n).

## Execution

$ cd ManasaAndStones/

$ python src/FirstGo.py < data/Input0.txt
