package main

import "sort"

func sortPeopleOptimized(names []string, heights []int) []string {
	// distinct height
	name := map[int]string{}
	for i, h := range heights {
		name[h] = names[i]
	}
	sort.Sort(sort.Reverse(sort.IntSlice(heights)))

	for i, h := range heights {
		names[i] = name[h]
	}

	return names
}

type Person struct {
	name   string
	height int
}

func sortPeople(names []string, heights []int) []string {
	people := []Person{}
	for i, name := range names {
		people = append(people, Person{name: name, height: heights[i]})
	}

	sort.Slice(people, func(i, j int) bool {
		return people[i].height > people[j].height
	})

	for i, p := range people {
		names[i] = p.name
	}
	return names
}
