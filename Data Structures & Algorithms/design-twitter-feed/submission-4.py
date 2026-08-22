import heapq

class Post:
    def __init__(self, time=float('inf'), tweetId=0, next=None):
        self.time = time
        self.tweetId = tweetId
        self.next = next

class Twitter:
    '''
    
    '''
    def __init__(self):
        # Data models:
        #   Adjacency matrix to record followee-followers
        #   HeapQueue of user's own posts (size 10)
        #   HeapQueue of user's feed 
        #   Global counter to act as "time"
        
        self.time = 0 # will be negative to use minheap easily
        self.users = set()
        self.following = {} # user: following
        self.followers = {} # user: followers
        self.postsByUser = {} # user: posts

    def createUser( self, userId ) -> None:
        # helper function to instantiate entry
        if userId not in self.users:
            self.users.add( userId )
            self.following[ userId ] = set()
            self.followers[ userId ] = set()
            self.postsByUser[ userId ] = Post() # dummy head

    def postTweet(self, userId: int, tweetId: int) -> None:
        # If user not in Adj matrix, add user;
        # Assign global counter (then increment it) to tweetId
        # push into user's own post linked list
        self.createUser( userId )
        
        postTime = self.time
        head = self.postsByUser[userId].next
        newPost = Post( postTime, tweetId, head )
        self.postsByUser[userId].next = newPost
        self.time -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        # merge k sorted list. stop at 10 or if heap is empty
        recentPosts = []
        feed = []
        # user's own posts
        post = self.postsByUser[userId].next
        if post:
            heapq.heappush( recentPosts, (post.time, post) )
        # user's followings' posts
        for following in self.following[ userId ]:
            post = self.postsByUser[following].next
            if post:
                heapq.heappush( recentPosts, (post.time, post) )
        while recentPosts:
            _, post = heapq.heappop( recentPosts )
            feed.append( post.tweetId )
            if len(feed) == 10:
                return feed
            if post.next:
                nextPost = post.next
                heapq.heappush( recentPosts, (nextPost.time, nextPost) )
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        # update follower-followee in adj matrix
        # fetch their posts and add into feed
        if followerId == followeeId:
            return
        self.createUser( followerId )
        self.createUser( followeeId )
        if followeeId in self.following[ followerId ]:
            return # already following; do nothing
        
        self.following[ followerId ].add( followeeId )
        self.followers[ followeeId ].add( followerId )
        # print(self.following)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # update follower-followee in adj matrix
        if followerId == followeeId:
            return
        self.createUser( followerId )
        self.createUser( followeeId )
        if followeeId not in self.following[ followerId ]:
            return # already unfollowed; do nothing

        self.following[ followerId ].remove( followeeId )
        self.followers[ followeeId ].remove( followerId )
        # print(self.following)
 