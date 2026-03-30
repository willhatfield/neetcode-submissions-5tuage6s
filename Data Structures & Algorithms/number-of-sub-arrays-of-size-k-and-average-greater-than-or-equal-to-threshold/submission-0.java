class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int sum = 0;
        int output = 0;

        for(int i = 0; i < arr.length; i++)    {
            int left = i - k;
            if(left >= 0)  {
                sum -= arr[left];
            } 
            
            sum += arr[i];
        
            if(i >= k - 1 && sum / k >= threshold) output++;
           
        }

        return output;
    }
}