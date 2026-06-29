class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        answer = []
        for i in nums:
            if i in count_dict: 
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        # print(count_dict)
        frequency_list = list(sorted(count_dict.items(), key = lambda x:x[1], reverse = True))
        print(frequency_list)
        for i in range (0,k):
            answer.append(frequency_list[i][0])
        return answer




        