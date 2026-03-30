class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashSet<Integer> window = new HashSet<>();

        for(int i = 0; i < nums.length; i++)    {
            if(window.contains(nums[i]))    {
                return true;
            }

            int left = i - k;
            if(left >= 0)   {
                window.remove(nums[left]);
            }

            window.add(nums[i]);
        }

        return false;
    }
}