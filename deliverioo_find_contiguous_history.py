'''
We have some clickstream data that we gathered on our client's website. 
Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. 
The histories are in chronological order, and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input 
and returns the longest contiguous sequence of URLs that appears in both.

Sample input:

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

Sample output:

findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
findContiguousHistory(user0, user2) => [] (empty)
findContiguousHistory(user0, user0) => ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
findContiguousHistory(user2, user1) => ["a"] 
findContiguousHistory(user5, user2) => ["a"]
findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]

n: length of the first user's browsing history
m: length of the second user's browsing history
'''


import unittest

def findContiguousHistory(user1, user2, pointer1=0, pointer2=0):
  histories =[[ 0, 0, []]]
  ans = []
  while histories:
    pointer1, pointer2, history = histories.pop()
    if pointer1<len(user1) and pointer2<len(user2):
      if user1[pointer1]==user2[pointer2]:
        history.append(user1[pointer1])
        pointer1+=1
        pointer2+= 1
        if len(ans)<len(history):
          ans = history
        histories.append([pointer1, pointer2, history])
      else:
        histories.append([pointer1+1, pointer2, []])
        histories.append([pointer1, pointer2+1,[]])
  return ans


class TestFind(unittest.TestCase):
  def setUp(self) -> None:
      self.user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
      self.user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
      self.user2 = ["a", "/one", "/two"]
      self.user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
      self.user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
      self.user5 = ["a"]
      self.user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

  def test_all_scenarios(self):
    assert findContiguousHistory(self.user0,self.user1) == ["/pink", "/register", "/orange"]
    assert findContiguousHistory(self.user0, self.user2) == [] 
    assert findContiguousHistory(self.user0, self.user0) == ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
    assert findContiguousHistory(self.user2, self.user1) == ["a"] 
    assert findContiguousHistory(self.user5, self.user2) == ["a"]
    assert findContiguousHistory(self.user3, self.user4) == ["/plum", "/blue", "/tan", "/red"]
    assert findContiguousHistory(self.user4, self.user3) == ["/plum", "/blue", "/tan", "/red"]
    assert findContiguousHistory(self.user3, self.user6) == ["/tan", "/red", "/amber"]


if __name__=="__main__":
  unittest.main()










# Note: built-in functions like the Python difflib module should not be used as solutions to this problem

counts = [
    "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "5,com.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,mobile.sports",
    "1,google.co.uk" 
]


def calculateClicksByDomain(counts):
  result = {}
  for item in counts:
    number, domain = item.split(',')
    subdomains = domain.split('.')
    for i in range(len(subdomains)):
      subdomain = '.'.join(subdomains[i:])
      if subdomain in result:
        result[subdomain] += int(number)
      else:
        result[subdomain] = int(number)
  return result

#print(calculateClicksByDomain(counts))