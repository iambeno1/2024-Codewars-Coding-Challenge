/*
Codewars Coding Challenge 

Day 86/366

Remove exclamation marks

Write function RemoveExclamationMarks which removes all exclamation marks from a given string.


https://www.codewars.com/kata/57a0885cbb9944e24c00008e/train/java
 */

class Solution {
    static String removeExclamationMarks(String s) {
        return s.replace("!", "");
    }
}
