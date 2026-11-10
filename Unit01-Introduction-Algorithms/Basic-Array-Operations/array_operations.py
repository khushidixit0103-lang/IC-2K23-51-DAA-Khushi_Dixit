"""
=============================================================================
  Course       : IC-709 B (Design & Analysis of Algorithms Lab)
  Unit         : Unit 01 - Introduction to Algorithms & Performance Analysis
  Experiment 1 : Basic Operations on Arrays
  Student      : Khushi Dixit
  Roll Number  : IC-2K23-51
=============================================================================
"""

from typing import List, Any, Optional, Tuple


class CustomArray:
    """
    Fixed-capacity array ADT demonstrating fundamental contiguous memory operations:
    Traversal, Insertion, Deletion, Search, and Update with explicit bounds checking.
    """

    def __init__(self, capacity: int = 20):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity: int = capacity
        self.size: int = 0
        self._data: List[Optional[Any]] = [None] * capacity

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def traverse(self) -> List[Any]:
        """Returns the current valid elements in order (O(n) time)."""
        return [self._data[i] for i in range(self.size)]

    def insert_at(self, index: int, value: Any) -> bool:
        """
        Inserts value at specified index shifting succeeding elements right (O(n) time).
        """
        if self.is_full():
            print(f"[Error] Array overflow: cannot insert {value}, capacity ({self.capacity}) reached.")
            return False
        if index < 0 or index > self.size:
            print(f"[Error] IndexOutOfBounds: cannot insert at index {index}. Valid range: [0, {self.size}].")
            return False

        # Shift elements right
        for i in range(self.size, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = value
        self.size += 1
        return True

    def append(self, value: Any) -> bool:
        """Appends value to the end of the array (O(1) amortized/constant)."""
        return self.insert_at(self.size, value)

    def delete_at(self, index: int) -> Optional[Any]:
        """
        Deletes and returns element at specified index shifting succeeding elements left (O(n) time).
        """
        if self.is_empty():
            print("[Error] Array underflow: cannot delete from an empty array.")
            return None
        if index < 0 or index >= self.size:
            print(f"[Error] IndexOutOfBounds: cannot delete at index {index}. Valid range: [0, {self.size - 1}].")
            return None

        deleted_val = self._data[index]
        # Shift elements left
        for i in range(index, self.size - 1):
            self._data[i] = self._data[i + 1]

        self._data[self.size - 1] = None
        self.size -= 1
        return deleted_val

    def delete_value(self, value: Any) -> bool:
        """Finds first occurrence of value and removes it."""
        idx = self.linear_search(value)
        if idx != -1:
            self.delete_at(idx)
            return True
        print(f"[Info] Value {value} not found in array; deletion skipped.")
        return False

    def update_at(self, index: int, new_value: Any) -> bool:
        """Updates value at index in-place (O(1) time)."""
        if index < 0 or index >= self.size:
            print(f"[Error] IndexOutOfBounds: cannot update at index {index}. Valid range: [0, {self.size - 1}].")
            return False
        self._data[index] = new_value
        return True

    def linear_search(self, target: Any) -> int:
        """Performs sequential search; returns index if found, else -1 (O(n) time)."""
        for i in range(self.size):
            if self._data[i] == target:
                return i
        return -1

    def find_min_max(self) -> Optional[Tuple[Any, Any]]:
        """Returns (min_value, max_value) in a single pass (O(n) time)."""
        if self.is_empty():
            return None
        curr_min = self._data[0]
        curr_max = self._data[0]
        for i in range(1, self.size):
            val = self._data[i]
            if val < curr_min:
                curr_min = val
            if val > curr_max:
                curr_max = val
        return curr_min, curr_max

    def reverse(self) -> None:
        """Reverses array elements in-place using two-pointer swapping (O(n) time, O(1) space)."""
        left = 0
        right = self.size - 1
        while left < right:
            self._data[left], self._data[right] = self._data[right], self._data[left]
            left += 1
            right -= 1


def run_demonstration():
    print("=" * 70)
    print("  DESIGN AND ANALYSIS OF ALGORITHMS LAB (IC-709 B)")
    print("  Unit 01 - Experiment 1: Basic Operations on Arrays")
    print("  Student: Khushi Dixit | Roll Number: IC-2K23-51")
    print("=" * 70)

    # 1. Initialize Array
    capacity = 10
    arr = CustomArray(capacity=capacity)
    print(f"\n[1] Initialized CustomArray with capacity = {capacity}.")
    print(f"    Current Size: {arr.size}, Elements: {arr.traverse()}")

    # 2. Append elements
    initial_values = [45, 12, 89, 34, 67]
    print(f"\n[2] Appending initial elements: {initial_values}")
    for val in initial_values:
        arr.append(val)
    print(f"    Array state after append: {arr.traverse()} (Size: {arr.size}/{arr.capacity})")

    # 3. Insert at specific indices
    print("\n[3] Insertion Demonstrations:")
    print("    - Inserting 99 at index 0 (Beginning)")
    arr.insert_at(0, 99)
    print(f"      State: {arr.traverse()}")

    print("    - Inserting 55 at index 3 (Middle)")
    arr.insert_at(3, 55)
    print(f"      State: {arr.traverse()}")

    print("    - Testing invalid insertion index 15 (Out of bounds)")
    arr.insert_at(15, 100)

    # 4. Search Operation
    print("\n[4] Linear Search Demonstrations:")
    targets = [55, 100]
    for target in targets:
        pos = arr.linear_search(target)
        if pos != -1:
            print(f"    - Target {target} FOUND at index {pos}.")
        else:
            print(f"    - Target {target} NOT FOUND in array.")

    # 5. In-Place Update
    print("\n[5] Update Operation:")
    print(f"    - Updating element at index 2 from {arr.traverse()[2]} to 777.")
    arr.update_at(2, 777)
    print(f"      State: {arr.traverse()}")

    # 6. Min and Max
    min_val, max_val = arr.find_min_max()
    print(f"\n[6] Extrema Inspection:")
    print(f"    - Minimum value : {min_val}")
    print(f"    - Maximum value : {max_val}")

    # 7. Deletion Operations
    print("\n[7] Deletion Demonstrations:")
    print(f"    - Deleting element at index 0 ({arr.traverse()[0]}):")
    del_val = arr.delete_at(0)
    print(f"      Removed: {del_val}, New State: {arr.traverse()}")

    print(f"    - Deleting value 34 by search-and-remove:")
    arr.delete_value(34)
    print(f"      New State: {arr.traverse()}")

    # 8. Array Reversal
    print("\n[8] In-Place Array Reversal:")
    print(f"    - Before: {arr.traverse()}")
    arr.reverse()
    print(f"    - After : {arr.traverse()}")

    # 9. Edge-Case Boundary Testing (Overflow)
    print("\n[9] Boundary Edge-Case Testing (Filling to Capacity):")
    fill_elements = [101, 102, 103, 104, 105, 106]
    for x in fill_elements:
        success = arr.append(x)
        if not success:
            break
    print(f"    Final Array State: {arr.traverse()} (Size: {arr.size}/{arr.capacity})")
    print("=" * 70)
    print("  Basic Array Operations execution completed successfully.")
    print("=" * 70)


if __name__ == "__main__":
    run_demonstration()
