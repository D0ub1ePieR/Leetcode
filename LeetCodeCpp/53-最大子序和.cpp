class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int len=nums.size();
        if (len==1)
           return nums[0]; 
        int left,right,m;
        vector<int> n1,n2;
        int i;
        for (i=0;i<len/2;i++)
            n1.push_back(nums[i]);
        for (i=len/2;i<len;i++)
            n2.push_back(nums[i]);
        left=this->maxSubArray(n1);
        right=this->maxSubArray(n2);
        int s1,s2,max1=0,max2=0;
        s1=nums[len/2-1];
        s2=nums[len/2];
        for (i=len/2-1;i>=0;i--)
        {
            max1+=nums[i];
            if (max1>s1)
                s1=max1;
        }
        for (i=len/2;i<len;i++)
        {
            max2+=nums[i];
            if (max2>s2)
                s2=max2;
        }
        m=s1+s2;
        if (m<left)
            m=left;
        if (m<right)
            m=right;
        return m; 
    }
};
