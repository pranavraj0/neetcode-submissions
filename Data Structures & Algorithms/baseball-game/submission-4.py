class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        #don't have to specifically check for int - type casting negative and built in string functions do not account for negative numeric values
        # so instead, if not any other op, has to be an int

        for op in operations:
            if op == '+':
                record.append(record[len(record) - 2] + record[len(record) - 1])
            elif op == 'D':
                record.append(record[len(record) - 1] * 2)
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))

        return sum(record)

        
        