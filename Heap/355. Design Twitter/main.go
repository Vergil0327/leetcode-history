// https://leetcode.com/problems/design-twitter/
package main

import (
	"container/heap"
)

// Input
// ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
// [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
// Output
// [null, null, [5], null, null, [6, 5], null, [5]]

// Explanation
// Twitter twitter = new Twitter();
// twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
// twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
// twitter.follow(1, 2);    // User 1 follows user 2.
// twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
// twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
// twitter.unfollow(1, 2);  // User 1 unfollows user 2.
// twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.

/*
Input:
["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]

Output: [null,null,[5],null,null,[5,6],null,[5]]
Expected: [null,null,[5],null,null,[6,5],null,[5]]
*/

type FollowMap = map[int]any

type NewsFeed struct {
	tweetID   int
	timestamp int64

	// for optimized solution
	followeeId int
	nextIndex  int
}

// 10 most recent
type maxHeap []NewsFeed

func (h maxHeap) Len() int {
	return len(h)
}
func (h maxHeap) Less(i, j int) bool {
	return h[i].timestamp > h[j].timestamp
}
func (h maxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *maxHeap) Push(item interface{}) {
	*h = append(*h, item.(NewsFeed))
}
func (h *maxHeap) Pop() interface{} {
	old := *h
	length := len(old)
	item := old[length-1]
	*h = old[:length-1]
	return item
}

type Twitter struct {
	timestamp    int64
	userRelation map[int]FollowMap
	userNewsFeed map[int][]NewsFeed
}

func Constructor() Twitter {
	return Twitter{
		userRelation: make(map[int]FollowMap),
		userNewsFeed: make(map[int][]NewsFeed),
	}
}

func (this *Twitter) PostTweet(userId int, tweetId int) {
	// lazy init
	if _, ok := this.userNewsFeed[userId]; !ok {
		this.userNewsFeed[userId] = make([]NewsFeed, 0)
	}

	this.timestamp += 1
	this.userNewsFeed[userId] = append(this.userNewsFeed[userId], NewsFeed{tweetID: tweetId, timestamp: this.timestamp})
}

func (this *Twitter) GetNewsFeed(userId int) []int {
	total := []NewsFeed{}
	if len(this.userNewsFeed[userId]) > 0 {
		total = append(total, this.userNewsFeed[userId]...)
	}

	for followee := range this.userRelation[userId] {
		if newsFeeds := this.userNewsFeed[followee]; len(newsFeeds) > 0 {
			total = append(total, newsFeeds...)
		}
	}

	h := maxHeap(total)
	heap.Init(&h)

	result := []int{}
	for h.Len() > 0 && len(result) < 10 {
		result = append(result, heap.Pop(&h).(NewsFeed).tweetID)
	}

	return result
}

// explanation
func (this *Twitter) GetNewsFeedOptimize(userId int) []int {
	result := []int{}
	h := maxHeap([]NewsFeed{})

	// add user himself to his followees
	this.Follow(userId, userId)

	for followeeId := range this.userRelation[userId] {
		if len(this.userNewsFeed[followeeId]) > 0 {
			lastIdx := len(this.userNewsFeed[followeeId]) - 1
			latestFeed := this.userNewsFeed[followeeId][lastIdx]
			latestFeed.followeeId = followeeId
			latestFeed.nextIndex = lastIdx - 1

			h = append(h, latestFeed)
		}
	}

	heap.Init(&h)
	for h.Len() > 0 && len(result) < 10 {
		feed := heap.Pop(&h).(NewsFeed)
		result = append(result, feed.tweetID)

		if feed.nextIndex >= 0 {
			nextFeed := this.userNewsFeed[feed.followeeId][feed.nextIndex] // ! be aware of that nextFeed.nextIndex && nextFeed.followeeId are still not assigned
			nextFeed.followeeId = feed.followeeId
			nextFeed.nextIndex = feed.nextIndex - 1
			heap.Push(&h, nextFeed)
		}
	}

	return result
}

func (this *Twitter) lazyInitFollow(userId int) {
	if _, ok := this.userRelation[userId]; !ok {
		this.userRelation[userId] = make(FollowMap)
	}
}

func (this *Twitter) Follow(followerId int, followeeId int) {
	// lazy init
	this.lazyInitFollow(followerId)
	this.userRelation[followerId][followeeId] = struct{}{}
}

func (this *Twitter) Unfollow(followerId int, followeeId int) {
	if _, ok := this.userRelation[followerId]; !ok {
		return
	}
	delete(this.userRelation[followerId], followeeId)
}

/**
 * Your Twitter object will be instantiated and called as such:
 * obj := Constructor();
 * obj.PostTweet(userId,tweetId);
 * param_2 := obj.GetNewsFeed(userId);
 * obj.Follow(followerId,followeeId);
 * obj.Unfollow(followerId,followeeId);
 */
