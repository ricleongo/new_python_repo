import operator

class CalculatorClass():
        
    def getTotalVotes(self, data):
        totalValues = len(list(data))
        return totalValues
    
    def getCandidateVoted(self, data, columnKey):
        results = []
        searchedValue = ''
        iterateUntil = len(data)

        data = sorted(data, key= lambda x: x[columnKey])

        for item in range(1, iterateUntil):
            currentValue = data[item].get(columnKey)

            if (searchedValue == '') | (searchedValue != currentValue):
                searchedValue = currentValue
                results.append(searchedValue)

        return results
    
    def getCandidateScoreByName(self, data, columnKey, list_data):
        results = {}
        iterateUntil = len(list_data)

        for item in range(0, iterateUntil):
            listperCandidate = [1 for candidate in data if candidate.get(columnKey) == list_data[item]]
            results[list_data[item]]= sum(listperCandidate)

        return sorted(results.items(), key=operator.itemgetter(1), reverse=True)

    def getCandidateWinner(self, list_data):
        return max(list_data, key = operator.itemgetter(1))[0]