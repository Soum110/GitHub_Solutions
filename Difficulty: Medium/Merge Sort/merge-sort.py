class Solution:
    
    def mergeSort(self, arr, l, r):
        if l >= r:
            return
        mid = (l + r) // 2    
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid+1, r)
        
        self.merge(arr, l, mid, r)
        
    def merge(self, arr, l, mid, r):
        i, j = l, mid+1
        temp = []
        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        
        while j <= r:
            temp.append(arr[j])
            j += 1
            
        for k in range(len(temp)):
            arr[l+k] = temp[k]