class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> hms = new HashMap<>();
        HashMap<Character, Integer> hmt = new HashMap<>();

        if(s.length() != t.length()) return false;

        int l = s.length();
        for(int i = 0; i < l; i++)  {
            Character cs = s.charAt(i);
            Character ts = t.charAt(i);

            if(hms.containsKey(cs)) {
                int count = hms.get(cs);
                hms.remove(cs);
                hms.put(cs, ++count);
            } else  {
                hms.put(cs, 1);
            }

            if(hmt.containsKey(ts)) {
                int count = hmt.get(ts);
                hmt.remove(ts);
                hmt.put(ts, ++count);
            } else  {
                hmt.put(ts, 1);
            }
        }

        return hms.equals(hmt);
    }
}
