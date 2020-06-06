/** bigO = n
 * Floyd's Tortoise and Hare
 * You will need to iterate TWICE.
 * First time, when you guys meet, you won't know the length of the cycle, or how long
 * the uncycled path will be. Only where you met here for the first time. Then you can
 * do a couple of different things to figure out loop length. Such as walking until
 * you guys meet again. OR, you can start from beginning and walk till you meet: why that works
 * 
 * Say: x = length before cycle
 * y = cycle length
 * m = meeting point (number of steps from cycle beginning)
 * n = number of loops hare did before meeting turtle
 * if hare and turtle meets at m, that means hare traveled m+x+n*y
 * and turtle traveled m+x
 * 
 * The hare and turtle meeting means that m+x is a multiple of y! *this is the key concept*
 * 
 * 
 * 
 * So we send another turtle starting from the beginning while the old turtle starts walking again. 
 * The turtles will meet once the new turtle has walked x
 * Why: if the old turtle walked m+x, he will just go back to m. If the new turtle walks m+x he will also
 * be at m. But if they only walk x, then they will BOTH be short of meeting m by m. 
 * So they will actually be at the beginning of the cycle. 
 * 
 * So how does this solve this problem:
 * We can pretend the array and its values are actually a sequence function that has a cycle.
 * f(i) = A[i]. The 'next' step, is the number in the index of i.
 * By running the entire array with 2 pointers, you will find that they will meet at a index. 
 * Then you can figure out where that cycle begins.
 * 
 * The beginning of that cycle will be the duplicate number!
 * 
 * Why is it that where we 'enter' the cycle is always the duplicate number?:
 * It is important to remember that given the nature of the array, there will be a duplicate number. We
 * have to find it. The reason that the duplicate number is always the start of the cycle is because we
 * have to arrive at that index twice. And the only way is by the same number. The first time, as we are traversing
 * x, we will reach the cycle beginning of the duplicate number d. Then we will keep traversing, somewhere along the line,
 * another index will supply us with the same element d. This causes us to go BACK to the cycle beginning, therefore finishing
 * the cycle for the first time. The ONLY way for a cycle to exist, is if there are duplicate elements pointing us to the same index. 
 * 
 **/
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int rabbit = nums[nums[0]];
        int turtle = nums[0];

        while(rabbit != turtle)
        {
            rabbit = nums[nums[rabbit]];
            turtle = nums[turtle];
        }

        rabbit = 0;

        while(rabbit != turtle)
        {
            rabbit = nums[rabbit];
            turtle = nums[turtle];
        }

        return rabbit;
    }
};
