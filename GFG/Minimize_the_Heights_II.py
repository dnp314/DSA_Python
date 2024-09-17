#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        
        arr.sort()
        n=len(arr)
        mini=arr[0]
        maxi=arr[n-1]
        res=maxi-mini
        
        for i in range(1,n):
            
            mini = min(arr[0]+k,arr[i]-k)
            maxi = max(arr[n-1]-k,arr[i-1]+k)
            if(mini<0):
                continue
            res = min(res,maxi-mini)
            
            
            
        return res
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends