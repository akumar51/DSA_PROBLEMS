import click

class Solution:
    
    def sort012(self, arr, method):
        if method == 1:
            return self.sort012_count(arr)
        elif method == 2:
            return self.sort012_dutch_flag(arr)
    
    def sort012_count(self,arr):
        #get frequencies of numbers in the array and then use it to sort the array
        zero = arr.count(0)
        one = arr.count(1)
        two = len(arr) - zero - one
        
        arr[:zero] = [0] * zero
        arr[zero:zero + one] = [1] * one  
        arr[zero + one: ] =  [2] * two
        
        return arr

    def sort012_dutch_flag(self,arr):
        # dutch flag method
        #divide the array into four parts
        # 0 - low, low - mid, mid - high, high - n
        # move the variables low, mid and high
        # simultaneously sort and swap positions
        low = 0
        mid = 0
        high = len(arr) - 1
        while mid <=  high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1   
                
        return arr
    

@click.command()
@click.option('-m', '--method', type=click.INT, default=1, help='Sorting method: 1 for counting sort, 2 for Dutch National Flag algorithm')
def main(method):
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        arr = []
        while True:
            try:
                arr = [int(x) for x in input("Enter the array elements separated by space (only 0, 1, and 2): ").strip().split()]
                if all(elem in [0, 1, 2] for elem in arr):
                    break
                else:
                    print("Invalid input. Array elements must be 0, 1, or 2. Please try again.")
            except ValueError:
                print("Invalid input. Please enter integers separated by space.")
        ob = Solution()
        sorted_arr = ob.sort012(arr, method)
        print(' '.join(map(str, sorted_arr)))

if __name__ == '__main__':
    main()
    