class Solution {
    public boolean isAnagram(String s, String t) {
        /* base case */
        if (s.length() != t.length()){
            return false;
        }
        
        /* Decleared array of ints of 0's */
        int[] count = new int[26];

        /* Iteration */
        for(int i = 0; i < s.length(); i++){
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        
        for (int cnt : count){
            if (cnt != 0){
                return false;
            }         
        }
        return true;
    }
}
