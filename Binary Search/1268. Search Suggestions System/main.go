package main

import (
	"sort"
	"strings"
)

func suggestedProducts(products []string, searchWord string) [][]string {
	sort.Strings(products)

	res := [][]string{}

	prefix := strings.Builder{}
	for _, ch := range searchWord {
		prefix.WriteRune(ch)

		idx := sort.Search(len(products), func(i int) bool {
			return products[i] >= prefix.String()
		})
		/*
			equivalent binary search implementation:
					l, r := 0, len(products)-1
					for l < r {
							mid := l + (r-l)/2
							if products[mid] < prefix.String() {
									l = mid+1
							} else {
									r = mid
							}
					}
					idx := l
		*/

		recom := []string{}
		for i := idx; i < len(products); i++ {
			if !strings.HasPrefix(products[i], prefix.String()) || len(recom) == 3 {
				break
			}
			recom = append(recom, products[i])
		}
		res = append(res, recom)
	}

	return res
}
