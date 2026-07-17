# only need to print count after duplicate not number 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i,j=0,0
        c=0
        k=0
        while j<n:
            
            if nums[i]==nums[j]:
                c+=1
                if c<=2:
                    nums[k]=nums[j]
                    k+=1
                    j+=1
                
                else :
                    j+=1
            else :

                i=j
                c=0
        print(k)     
        return k

        




        



        
