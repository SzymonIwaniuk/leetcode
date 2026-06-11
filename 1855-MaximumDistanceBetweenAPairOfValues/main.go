func maxDistance(nums1 []int, nums2 []int) int {
	i, j, res := 0, 0, 0

	// for i, n1 := range nums1 {
	//     idx := bSearch(i, l-1, nums2, n1)
	//     if idx != -1 {
	//         res = max(res, idx - i)
	//     }
	// }

	// return res

	for i < len(nums1) && j < len(nums2) {
		if nums2[j] >= nums1[i] {
			res = max(res, j-i)
			j++
		} else {
			i++
			if i > j {
				j = i
			}
		}

	}

	return res
}

// func bSearch(l int, r int, arr []int, num int) int {
//     ans := -1

//     for l <= r {
//         mid := l + (r - l) / 2
//         if arr[mid] >= num {
//             ans = mid
//             l = mid + 1
//         } else {
//             r = mid - 1
//         }
//     }

//     return ans
// }
