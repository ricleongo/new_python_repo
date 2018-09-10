import operator

class CalculatorClass():

    def getTotalMonths(self, data):
        totalValues = len(list(data))
        return totalValues

    def getNetAmountByColumn(self, data, columnName):
        netAmount = 0
        list1 = [element.get(columnName) for element in data]
        iterateUntil = len(list1)

        for item in range(0, iterateUntil):
            netAmount += int(list1[item])

        return netAmount

    def getAverageChange(self, data, columnName):
        resultList = []
        columnList = [element.get(columnName) for element in data]
        iterateUntil = len(columnList)

        for item in range(1, iterateUntil):
            normalValue = float(columnList[item]) - float(columnList[item - 1])
            resultList.append(normalValue)

        return round(sum(resultList) / len(resultList), 2)

    def getGreatestProfit(self, data, columnKey, columnValue):
        resultList = {}
        iterateUntil = len(data)

        for item in range(1, iterateUntil):
            currentValue = data[item].get(columnValue)
            previousValue = data[item - 1].get(columnValue)

            normalValue = int(currentValue) - int(previousValue)
            resultList[data[item].get("Date")] = normalValue

        maxKey = max(resultList.items(), key = operator.itemgetter(1))[0]
        maxValue = max(resultList.items(), key = operator.itemgetter(1))[1]
        
        return maxKey, maxValue

    def getLowestProfit(self, data, columnKey, columnValue):
        resultList = {}
        iterateUntil = len(data)

        for item in range(1, iterateUntil):
            currentValue = data[item].get(columnValue)
            previousValue = data[item - 1].get(columnValue)

            normalValue = int(currentValue) - int(previousValue)
            resultList[data[item].get("Date")] = normalValue

        maxKey = min(resultList.items(), key = operator.itemgetter(1))[0]
        maxValue = min(resultList.items(), key = operator.itemgetter(1))[1]
        
        return maxKey, maxValue
