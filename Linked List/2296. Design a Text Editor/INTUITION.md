# Intuition

we want add/remove element efficiently
=> what if we use linked list to store characters

```
head
Add: head -> ch1 -> ch2 -> ch3 -> ch4 -> ... -> ch
                                                ptr

delete: head -> ch1 -> ch2 -> ch3 -> ch4 -> ... -> ch''' -> del(ch'') -> del(ch') -> del(ch)
                                                          <-ptr

cursorLeft:  head -> ch1 -> ch2 -> ch3 -> ch4 -> ... -> ch
                                   ptr              <- ptr
                                   return last (10, len) characters
cursorRight:  head -> ch1 -> ch2 -> ch3 -> ch4 -> ... -> ch
                                   ptr->                ptr
                                   return last (10, len) characters
```

thus, we can maintain a linked list with a variable as cursor `self.cur`

- once we want to add text, we can insert characters before cursor

```
#: head
$: cursor

# -> [ch -> ch -> ch] -> $
         inserted
```

- once we want to delete text, we can delete characters before cursor

```
#: head
$: cursor

# -> [ch -> ch -> ch] -> $
         deleted
```

- once we want to move cursor to left/right

```
#: head
$: cursor

# -> ch -> ch -> ch -> $ -> ch -> ch -> ...
                    <- $ -> 
```

# Other Solution

we can also use **two deque** to maintain prefix before cursor and suffix after cursor

addText: append characters to prefix deque
deleteText: pop characters from prefix deque
cursorRight: append suf_deque.popleft() to pre_deque
cursorLeft:: appendleft pre_deque.pop() to suf_deque

*same idea, we can use two strings as prefix before cursor and suffix after cursor*

