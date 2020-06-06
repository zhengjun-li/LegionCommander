/** bigO = number of digits
 * How to add elements to end of vectors array.push_back(num)
 * access vector indices - array.at(i)
 * 
 * 
 * 
 * */

class Solution {
public:
    int reverse(int x) {
        int current = x;
        int mod;

        vector<int> array;
        while(current > 0)
        {
            mod = current % 10;
            array.push_back(mod);
            current = (current - mod) / 10;
        }
        current = 0;
        for(int i = 0;i < array.size(); i++)
        {
            mod = current;
            int exp = array.size() - 1 - i;
            current = current + array.at(i)*(pow(10, exp));
            if (current - array.at(i)*(pow(10, exp)) != mod)
            {
                return 0;
            }

        }
        return current;

    }
};