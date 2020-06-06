#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool validPalindrome(string s);

int main()
{
  string s = "abcde";
  validPalindrome(s);
  






}


bool validPalindrome(string s) {
  int length = s.length();
  string firstHalf = s.substr(0, length/2);
  string secondHalf = s.substr(length/2, length);
  cout << firstHalf + "\n" + secondHalf;

  reverse(secondHalf.begin(), secondHalf.end());

  cout << secondHalf;



  return false;
}
