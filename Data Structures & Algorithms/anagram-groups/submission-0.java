class Solution {
    public List<List<String>> groupAnagrams(String[] strs){

Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            // Step 1: Sort characters in the string
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            // Step 2: Put into map
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(s);
        }

        // Step 3: Return values of the map as result
        return new ArrayList<>(map.values());
    }
}
