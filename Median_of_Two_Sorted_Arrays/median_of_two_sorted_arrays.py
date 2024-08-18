class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def partition(arr, pivot):
            less = [x for x in arr if x < pivot]
            greater = [x for x in arr if x > pivot]
            return less, greater

        def select(arr, k):
            if len(arr) < 5:
                return sorted(arr)[k]

            medians = [sorted(arr[i:i + 5])[len(arr[i:i + 5])] for i in range(0, len(arr), 5)]

            # Encontrar a mediana das medianas 
            pivot = select(medians, len(medians) // 2)

            # Particiona baseado no pivot
            less, greater = partition(arr, pivot)

            if k < len(less):
                return select(less, k)
            else:
                return select(greater, k - len(less))

        def findKthElement(arr1, arr2, k):
            combined = arr1 + arr2
            return select(combined, k)

        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            return findKthElement(nums1, nums2, total_len)
        else:
            return (findKthElement(nums1, nums2, total_len) + findKthElement(nums1, nums2, total_len // 2)) / 2.0