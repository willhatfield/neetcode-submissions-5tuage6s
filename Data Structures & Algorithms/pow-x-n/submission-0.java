class Solution {
    public double myPow(double x, int n) {
        if(x == 0 || n == 1) return x;
        if(n == 0) return 1;
        
        double pow = myPow(x, Math.abs(n/2));
        double res;

        if(Math.abs(n % 2) == 1) res = pow*pow*x;
        else res = pow*pow;

        System.out.println(res);

        if(n > 0) return res;
        else    {
            return 1/res;
        }
    }
}
