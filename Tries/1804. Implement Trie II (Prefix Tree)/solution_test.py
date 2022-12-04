from solution import Trie


def test_trie():
  tri = Trie()
  tri.insert("apple")
  tri.insert("apple")
  assert tri.countWordsEqualTo("apple") == 2
  assert tri.countWordsStartingWith("app") == 2
  tri.erace("apple")
  assert tri.countWordsEqualTo("apple") == 1
  assert tri.countWordsStartingWith("app") == 1
  assert tri.hasPrefix("app") == True
  assert tri.hasPrefix("apple") == True
  tri.erace("apple")
  assert tri.countWordsEqualTo("apple") == 0
  assert tri.hasPrefix("app") == False
  assert tri.hasPrefix("apple") == False