class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int p=m+n;
        double[] nums3 = new double [p];
        int k = 0;
        for (int num : nums1) {
            nums3[k++] = num;
        }

        for (int num : nums2) {
            nums3[k++] = num;
        }
        Arrays.sort(nums3);
        double median = 0;
        if (p%2==0){
            median = (nums3[p/2 - 1] + nums3[p/2]) / 2.0;
        }
        else if (p%2!=0){
            median = nums3[p/2];
        }
        return median;
    }
}