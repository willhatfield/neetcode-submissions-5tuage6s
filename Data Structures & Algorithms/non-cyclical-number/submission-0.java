class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> seen = new HashSet<>();
        seen.add(n);
        while(true) {
            n = sumsquares(n);
            if(n == 1) {
                return true;
            } else if(seen.contains(n)) {
                return false;
            } else  {
                seen.add(n);
            }
        }
    }

    public int sumsquares(int n)    {
        int sum = 0;
        while(n != 0)   {
            sum += Math.pow((n % 10), 2);
            n = n / 10;
        }

        return sum;
    }
}
