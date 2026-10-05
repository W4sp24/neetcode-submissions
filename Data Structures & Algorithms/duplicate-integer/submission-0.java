
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Hashtable<Integer,Integer> hash = new Hashtable<>();
        
        for(int i = 0; i < nums.length; i++){
            
            int temp = nums[i];
            if(hash.containsKey(temp)){
                return true;
            }
            hash.put(temp, i);
  
        }

        return false;
    }
}