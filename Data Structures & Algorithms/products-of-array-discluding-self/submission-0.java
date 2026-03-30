class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] pp = new int[n];
        int[] sp  = new int[n];
        

        pp[0] = nums[0];
        sp[n - 1] = nums[n - 1];

        for(int i = 1; i < n; i++)   {
            pp[i] = nums[i] * pp[i - 1];
        }

        for(int i = n - 2; i >= 0; i--) {
            sp[i] = nums[i] * sp[i + 1];
        }

        int[] output = new int[n];
        // System.out.println(Arrays.toString(pp));
        // System.out.println(Arrays.toString(sp));

        output[0] = sp[1];
        output[n - 1] = pp[n - 2];

        for(int i = 1; i < n - 1; i++)   {
            output[i] = pp[i - 1] * sp[i + 1];
        }

        return output;
    
    }
}  
