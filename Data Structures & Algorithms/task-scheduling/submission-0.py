class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #heap to keep using max freq task
        #queue to keep cooldown of task until available to be put into queue

        #can also use counter which is hashmap under the hood

        arr = [0] * 26
        for task in tasks: 
            arr[ord(task) - ord('A')] += 1

        #maxHeap
        maxHeap = []
        for num in arr: 
            if num > 0:
                maxHeap.append(-num)
        heapq.heapify(maxHeap)

        #
        time = 0
        queue = deque() #[-arr[i], idleTime]

        while maxHeap or queue: 
            time += 1

            #if nothing ready skip all idles instead of cont iteration
            if not maxHeap:
                time = queue[0][1]
            #if heap not empty
            else:
                # add one because stored as neg in heap
                cnt = 1 + heapq.heappop(maxHeap)
                #if not zero add to queue for cooldown
                if cnt: 
                    # add count left and time next when ready
                    queue.append([cnt, time + n])
            #only need to check the front of the queue to put back into heap
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time
