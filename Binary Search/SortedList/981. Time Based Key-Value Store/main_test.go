// https://leetcode.com/problems/time-based-key-value-store/
package main

import (
	"fmt"
	"testing"
)

// ["TimeMap","set","set","get","get","get","get","get"]
// [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
// Expected: [null,null,null,"","high","high","low","low"]
func TestTimeMap_Set(t *testing.T) {
	m := Constructor()
	m.Set("foo", "bar", 1)

	rslt1 := m.Get("foo", 1)
	fmt.Println("rslt:", rslt1)
	rslt2 := m.Get("foo", 3)
	fmt.Println("rslt:", rslt2)

	// fmt.Println("result:", rslt)
	t.Errorf("TimeMap.Get() = %v", 1)
	// t.Errorf("TimeMap.Get() = %v", m.Get("foo", 3))
	// fmt.Printf("------------------------------")
}
