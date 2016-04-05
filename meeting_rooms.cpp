/*
Problem: Meeting Rooms
(https://leetcode.com/problems/meeting-rooms/)


Restating the question:

You are given a vector of integer ranges, [a0, a1). 
Your job is to essentially find whether or not ranges in the vector given
overlap with another one or not.

Two kinds of overlap are possible:
a0 b0 b1 a1 (complete overlap) a0 b0 a1 b1 (incomplete overlap)

To solve this question, we sort the vector by start times in O(nlogn) so that
we can put the vector into an ordered form to check for overlap as mentioned above.
By putting it into consecutive, ordered ranges, we can easily identify the 
forms of overlap which are based by its consecutive properties.

We check for overlap 1 by:
Checking if b's end time is before a's end time, thus overlap.

We check for overlap 2 by:
Checking if b's start time is before a's end time, thus overlap.
*/

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool compare(Interval i, Interval j) {
    return i.start < j.start;
}
bool canAttendMeetings(vector<Interval>& intervals) {   
    if (intervals.size() == 1) return true;
    sort (intervals.begin(), intervals.end(), compare);
    for (int i = 1; i < intervals.size(); i++) {
        if (intervals[i].end <= intervals[i-1].end || intervals[i].start < intervals[i-1].end) return false;
    }
    return true;
}

int main() {}