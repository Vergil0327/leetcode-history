class ListNode:
    def __init__(self, ID, ts):
        self.tweetId = ID
        self.timestamp = ts
        self.next = self.prev = None

class Twitter:

    def __init__(self):
        self.timestamp = 0
        def initListNode():
            root = ListNode(-1, -1)
            root.next = root.prev = root
            return root
        self.user2tweet = defaultdict(initListNode)
        self.user2followers = defaultdict(set)
        self.user2followees = defaultdict(set)
        

    def insertToFront(self, root, node):
        node.prev = root
        node.next = root.next
        node.prev.next = node
        node.next.prev = node
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.insertToFront(self.user2tweet[userId], ListNode(tweetId, self.timestamp))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        
        # don't forget to retrieve ourselves's newsfeed
        self.user2followees[userId].add(userId)
        for followeeId in self.user2followees[userId]:
            root = self.user2tweet[followeeId]
            if root.next.timestamp != -1:
                heapq.heappush(maxHeap, [-root.next.timestamp, root.next])
            
        newsFeed = []
        n = 10
        while maxHeap and n > 0:
            _, node = heapq.heappop(maxHeap)
            newsFeed.append(node.tweetId)
            if node.next.timestamp != -1:
                heapq.heappush(maxHeap, [-node.next.timestamp, node.next])
            
            n -= 1
        return newsFeed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user2followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user2followees[followerId].discard(followeeId)
        


# userId1: [tweet, timestamp]...
# userId2: [tweet, timestamp]...
# userId3: [tweet, timestamp]...

# followeeId: set([followId1, 2, 3])
