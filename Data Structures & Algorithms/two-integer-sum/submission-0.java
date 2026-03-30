class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hm = new HashMap<>();

        for(int i = 0; i < nums.length; i++)    {
            int num = nums[i];
            int compl = target - num;
            if(hm.containsKey(compl))   {
                int[] sol = new int[2];
                int complIdx = hm.get(compl);
                sol[0] = complIdx;
                sol[1] = i;
                return sol;
            } else  {
                hm.put(num, i);
            }
        }

        return null;
    }
}
