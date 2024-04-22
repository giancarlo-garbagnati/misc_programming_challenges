<h2>Coding Exercise: Decoding a Message from a Text File</h2>

This was part of a technical assessment for an interview I took. The prompt was to create a function to decode a message from a .txt file and output the decoded message as a string. Each line of the encoded message .txt was a number followed by a space and a word. The decoded message would be formed by taking the words from specific indices based on if the index was the last (rightmost) number on each row if the numbers were arranged into a “pyramid” (sequentially and in ascending order).

For example, let’s say this is what’s in our encoded message .txt:
```
3 love
6 computers
2 dogs
4 cats
1 I
5 you
```

The pyramid that would be formed with these indices would look like this:
```
  1
 2 3
4 5 6
```

So you’d take the last (rightmost) number from each row and form a decoded message using those indices. In this example, indices [1,3,6] would be used to form the decoded message string: “I love computers”.

The prompt wasn’t specific if the input of the function was the file object read in or the string from reading the file object, so both solutions were implemented. Additionally, some assumptions had to be made: (1) all the indices were sequential from 1 to the last word’s index and (2) there were no duplicate indices. Also, the prompt wasn’t clear if we were to assume the pyramid was complete or if the solution had to accommodate “incomplete” pyramids, however my solution should cover both cases.

<h3>Solution:</h3>

My solution for this revolved around using the triangular number series equation (**(n+1)(n)/2 **) for the indices of the message. If the pyramid is "full" (and the message's word indices are all sequential numbers starting from 1), the highest index number in the message (ie the last word in the decoded message) can be used to solve for n in the triangular number series equation and determine the length of the message (ie how many rows there are in the pyramid). Then you can go back and fill in the rest of the message starting from 1 using the triangular number series equation to get the indices of each word (and using the last index's word as the last word in the message).

If the pyramid is incomplete, this wouldn't necessarily work. However if you take the result from the "solve for n using the max index" step (which won't be a whole number if the pyramid is incomplete) and get the ceiling of it, that should solve this issue.

<h4>Specific Solution</h4>

<details>
  <summary>Included is a sample encoded message .txt (“coding_qual_input.txt”). The solution for this should be:</summary>
  >“design all skill whole check deal wish visit now moment offer planet people electric lot huge system card current man way our parent wait”
</details>
