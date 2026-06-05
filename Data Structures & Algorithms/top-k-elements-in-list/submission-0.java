class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Stores # of times each number showed up
        Map<Integer, Integer> map = new HashMap<>();
        // Each index of freq is where list of those ints is stored
        // that is repeated x times. 
        List<Integer>[] freq = new List[nums.length + 1];

        // initalize each indice to a empty ArrayList
        for (int i = 0; i < freq.length; i++){
            freq[i] = new ArrayList<>();
        }
        // add each int in num to HashMap and add 1 to its value
        // set 0 if map has no key @ int and make value 0 + 1
        for (int n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        // put the value (freq of #) into a bucket and the key int 
        // that had that frequency
        for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }
        // length of k ints with most frequency
        int[] result = new int[k];
        int index = 0;
        // loops through bucket and adds numbers - terminates index = k
        for (int i = freq.length - 1; i > 0 && index < k; i--){
            for (int n : freq[i]){
                result[index] = n;
                index++;
                if (index == k){
                    return result;
                }
            }
        }
        return result;



    }
}
