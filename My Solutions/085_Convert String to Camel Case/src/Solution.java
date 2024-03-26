/*
Codewars Coding Challenge 

Day 85/366

Level 6kyu java

Convert string to camel case

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"



import java.lang.StringBuilder;
class Solution{

  static String toCamelCase(String s){
    return "";
  }
}

https://www.codewars.com/kata/517abf86da9663f1d2000003/train/java

 */

// My Solution

import java.lang.StringBuilder;

class Solution{

  static String toCamelCase(String s){

    String[] words = s.split("[-_]");
    StringBuilder result = new StringBuilder(words[0]);

    for(int i = 1; i < words.length; i++){
      result.append(Character.toUpperCase(words[i].charAt(0)));
      result.append(words[i].substring(1));
    }
    return result.toString();
  }

  public static void main(String[] args) {
    // Test cases
    System.out.println(toCamelCase("the-stealth-warrior")); // Output: theStealthWarrior
    System.out.println(toCamelCase("The_Stealth_Warrior")); // Output: TheStealthWarrior
    System.out.println(toCamelCase("The_Stealth-Warrior")); // Output: TheStealthWarrior
  }
}
