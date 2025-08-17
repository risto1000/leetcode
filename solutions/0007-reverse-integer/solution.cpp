class Solution {
public:
    int reverse(int x) {
        long d=0,ret=0;
        while(x!=0){
            d=x%10;
            ret=ret*10+d;
            x=x/10;
        }
        if(ret>INT_MAX || ret<INT_MIN){
            return 0;
        }
        return ret;
    }
};
