'''
计算连续子数组的最大和
例如：
[2,1,2,3,1] 值为：3
[-1,-3,-4,-6] 值为-1
'''
public int FindGreatestSumOfSubArray(int[] array) {
        if(array.length<=0 || array==null){
            return 0;
        }
        int sumArray=0;
        int totalArray=array[0];
        for(int i=0;i<array.length;i++){
            if(sumArray<=0){
                sumArray=array[i];
            }else{
                sumArray += array[i];
            }
            if(sumArray>totalArray){
                totalArray=sumArray;
            }
        }
        return totalArray;
    }
