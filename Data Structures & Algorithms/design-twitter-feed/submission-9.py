class Twitter:

    def __init__(self):
        self.feed = {}
        self.follows = {}
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.feed:
            self.feed[userId] = []
            self.follows[userId] = []

        self.feed[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]: 
        res = []
        if userId in self.feed:
            res = self.feed[userId].copy()

        if self.follows[userId] != []:
            for follow in self.follows[userId]:
                res = self.feed[follow] + res
                print(res)
        res = sorted(res, key = lambda x: x[0], reverse = True)
        return [tweetId for time, tweetId in res[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = []
        if followeeId not in self.follows:
            self.follows[followeeId] = []

        if followerId != followeeId and followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        for idx, i in enumerate(self.follows[followerId]):
            if i == followeeId:
                self.follows[followerId].pop(idx)
        
            
