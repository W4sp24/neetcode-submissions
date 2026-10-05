class Solution {
    public boolean isAnagram(String s, String t) {
        if(t.length()!=s.length()){
                return false;
            }
        HashMap<Character, Integer> map = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            char character = s.charAt(i);
            if(map.containsKey(character)){
                int value = map.get(character);
                map.put(character,++value);
            }else{
                map.put(character, 1);
            }

            char character2 = t.charAt(i);
            if(map.containsKey(character2)){
                int value = map.get(character2);
                map.put(character2, --value);
            }else {
                map.put(character2, -1);
                }
        }

        for(int value : map.values()){
            if(value!=0){
                return false;
            }
        }

        return true;
    }
}
