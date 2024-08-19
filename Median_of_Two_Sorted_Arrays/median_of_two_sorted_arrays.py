class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def partition(arr, pivot):
            less = [x for x in arr if x < pivot]
            equal = [x for x in arr if x == pivot]
            greater = [x for x in arr if x > pivot]
            return less, equal, greater

        def select(arr, k):
            if len(arr) <= 5:
                return sorted(arr)[k]

            # Dividir o array em grupos de 5 e encontrar a mediana de cada grupo
            medians = [sorted(arr[i:i + 5])[len(arr[i:i + 5]) // 2] for i in range(0, len(arr), 5)]

            # Encontrar a mediana das medianas de maneira recursiva
            pivot = select(medians, len(medians) // 2)

            less, equal, greater = partition(arr, pivot)

            if k < len(less):
                return select(less, k)
            elif k < len(less) + len(equal):
                return pivot
            else:
                return select(greater, k - len(less) - len(equal))

        def findKthElement(arr1, arr2, k):
            combined = arr1 + arr2
            return select(combined, k)

        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            return findKthElement(nums1, nums2, total_len // 2)
        else:
            return (findKthElement(nums1, nums2, total_len // 2 - 1) + findKthElement(nums1, nums2, total_len // 2)) / 2.0

