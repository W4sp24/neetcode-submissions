class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer,Integer> hash = new Hashtable<>();
        int[] result  = new int[2];

        for(int i = 0 ; i < nums.length; i++){
            int element = nums[i];
            int x = target-element;
            if(hash.containsKey(x)){
                result[0]= hash.get(x);
                result[1] =i;
            }else{
                hash.put(element,i);
            }
        }  
        return result;


    }
}
