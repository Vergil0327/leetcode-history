package main

// we don't need another hashmap for deadends
func openLockConcise(deadends []string, target string) int {
	visited := map[string]bool{}
	for _, deadend := range deadends {
		visited[deadend] = true
	}

	turns := 0
	queue := []string{"0000"}
	for len(queue) > 0 {
		for _, node := range queue {
			queue = queue[1:]

			if node == target {
				return turns
			}

			if visited[node] {
				continue
			}

			visited[node] = true

			for i := 0; i < 4; i++ {
				plus1 := string('0' + (node[i]-'0'+1)%10)
				minus1 := string('9' - ('9'-node[i]+1)%10)

				queue = append(queue, node[:i]+plus1+node[i+1:])
				queue = append(queue, node[:i]+minus1+node[i+1:])
			}
		}

		turns += 1
	}

	return -1
}

func openLock(deadends []string, target string) int {
	deadendsMap := map[string]bool{}
	for _, deadend := range deadends {
		deadendsMap[deadend] = true
	}

	visited := map[string]bool{}
	turns := 0
	queue := []string{"0000"}
	for len(queue) > 0 {
		for _, node := range queue {
			queue = queue[1:]

			if _, ok := deadendsMap[node]; ok {
				continue
			}

			if node == target {
				return turns
			}

			if visited[node] {
				continue
			}

			visited[node] = true

			for i := 0; i < 4; i++ {
				plus1 := string('0' + (node[i]-'0'+1)%10)
				minus1 := string('9' - ('9'-node[i]+1)%10)

				queue = append(queue, node[:i]+plus1+node[i+1:])
				queue = append(queue, node[:i]+minus1+node[i+1:])
			}
		}

		turns += 1
	}

	return -1
}

// explanation: https://www.youtube.com/watch?v=Pzg3bCDY87w
func openLockNeetcode(deadends []string, target string) int {
	visited := map[string]bool{}
	for _, deadend := range deadends {
		visited[deadend] = true
	}

	turns := 0
	queue := []string{"0000"}
	for len(queue) > 0 {
		for _, node := range queue {
			queue = queue[1:]

			if node == target {
				return turns
			}

			if visited[node] {
				continue
			}

			for i := 0; i < 4; i++ {
				plus1 := string('0' + (node[i]-'0'+1)%10)
				minus1 := string('9' - ('9'-node[i]+1)%10)

				if next := node[:i] + plus1 + node[i+1:]; !visited[next] {
					visited[node] = true
					queue = append(queue, next)
				}
				if next := node[:i] + minus1 + node[i+1:]; !visited[next] {
					visited[node] = true
					queue = append(queue, next)
				}
			}
		}

		turns += 1
	}

	return -1
}
