# Implement a prototype of a friend recommendation system for a social media application.

# There are n users indexed from 0 to n-1, and m friends represented as a 2d array, friendships,
# where the ith friendship is a connection between users friendships[i][0] and friendships[i][1].

# User x is suggested as a friend to user y if x and y are not friends
# and nave the maximum number of common friends, i.e, a friend of both x and y.
# If there are multiple possible such users x, the one with the minimum index is suggested.

# Given n and friendships, for each of the n users,
# find the index of the friend that should be recommended to them.
# If there is no recommendation available, report -1.

from collections import defaultdict

def getRecommendedFriends(n, friendships):
    # Write your code here
    friends_of = [set() for _ in range(n)]
    for u, v in friendships:
        friends_of[u].add(v)
        friends_of[v].add(u)
    
    recommendations = []

    for i in range(n):
        if not friends_of[i]:
            recommendations.append(-1)
            continue
        
        max_common = 0
        max_index = -1
        count_mutual = defaultdict(int)

        for friend in friends_of[i]:
            for person in friends_of[friend]:
                if person != i and person not in friends_of[i]:
                    count_common[person] += 1

        for person, count in count_common:
            if count > max_common or (count == max_common and person < max_index):
                max_common = count
                max_index = index
        
        recommendations.append(max_index)
    
    return recommendations