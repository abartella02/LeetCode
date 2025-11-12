/*
 * Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
 * and return an array of the non-overlapping intervals that cover all the intervals in the input.
 *
 *
 * Example 1:
 * Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
 * Output: [[1,6],[8,10],[15,18]]
 * Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
 *
 */


/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {

    intervals.sort((a, b) => (
        a[0]===b[0]
        ? a[1]-b[1] // if first elements are equal, sort by second elements
        : a[0]-b[0]
    ))

    let i = 1
    while(i < intervals.length){
        cur = intervals[i-1]
        next = intervals[i]

        if(cur[0] < next[0] && cur[1] > next[1]){
            // cur fully contains next
            intervals[i] = intervals[i-1]
            intervals[i-1] = null
        } else if(cur[1] >= next[0]){
            // cur and next overlap
            intervals[i][0] = intervals[i-1][0]
            intervals[i-1] = null
        }
        i++
    }
    return intervals.filter((a) => a !== null)
};