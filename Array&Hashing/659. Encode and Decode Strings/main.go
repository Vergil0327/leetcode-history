package main

import (
	"fmt"
	"strconv"
)

/*
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
string encode(vector strs) {
  // ... your code
  return encoded_string;
}

Machine 2 (receiver) has the function:
vector decode(string s) {
  //... your code
  return strs;
}

So Machine 1 does:
string encoded_string = encode(strs);

and Machine 2 does:
vector strs2 = decode(encoded_string);

strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Note:
The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm. */

// input: ["lint", "code", "love", "you"]
// output: ["lint", "code", "love", "you"]
// Explanation:
// one possible encode method is "lint:;code:;love:;you"

// https://www.youtube.com/watch?v=B1k_sxOSgv8
func encode(list []string) string {
	result := ""
	for _, str := range list {
		str = fmt.Sprint(len(str)) + "#" + str
		result += str
	}

	return result
}

func decode(list string) []string {
	result, i := []string{}, 0

	for i < len(list) {
		j := i
		for list[j] != '#' {
			j += 1
		}
		length, _ := (strconv.ParseInt(list[i:j], 10, 32))
		result = append(result, list[j+1:j+1+int(length)])
		i = j + 1 + int(length)
	}

	return result
}
