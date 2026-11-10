"""
Course: IC-709 B - Design and Analysis of Algorithms Lab
Student: Khushi Dixit (Roll No: IC-2K23-51)
Unit 03: Greedy Method
Experiment: Fractional Knapsack

Problem Statement:
Given a set of N items, each with a weight w_i and a value v_i, and a knapsack of capacity W,
maximize the total value placed in the knapsack. Items can be broken into fractional amounts.
Greedy Choice: Select items with the highest value-to-weight ratio (v_i / w_i).
"""

class Item:
    def __init__(self, item_id, value, weight):
        self.item_id = item_id
        self.value = value
        self.weight = weight
        self.ratio = value / weight

    def __repr__(self):
        return f"Item({self.item_id}: v={self.value}, w={self.weight}, ratio={self.ratio:.2f})"


def fractional_knapsack(items, capacity):
    """
    Solves Fractional Knapsack using the Greedy strategy.
    
    Returns:
        tuple: (total_value, taken_fractions)
    """
    # Sort items by value-to-weight ratio in descending order
    sorted_items = sorted(items, key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    taken_details = []
    
    for item in sorted_items:
        if remaining_capacity == 0:
            break
            
        if item.weight <= remaining_capacity:
            # Take the whole item (fraction = 1.0)
            taken_fraction = 1.0
            total_value += item.value
            remaining_capacity -= item.weight
        else:
            # Take a fraction of the item
            taken_fraction = remaining_capacity / item.weight
            total_value += item.value * taken_fraction
            remaining_capacity = 0.0
            
        taken_details.append({
            "item_id": item.item_id,
            "value": item.value,
            "weight": item.weight,
            "ratio": item.ratio,
            "fraction": taken_fraction,
            "value_taken": item.value * taken_fraction,
            "weight_taken": item.weight * taken_fraction
        })
        
    return total_value, taken_details


def main():
    print("=" * 70)
    print("  IC-709 B: UNIT 3 - FRACTIONAL KNAPSACK (GREEDY STRATEGY)")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)
    
    # Test dataset
    items = [
        Item("Item 1", value=60, weight=10),
        Item("Item 2", value=100, weight=20),
        Item("Item 3", value=120, weight=30)
    ]
    knapsack_capacity = 50
    
    print(f"Knapsack Total Capacity (W): {knapsack_capacity}")
    print("Available Items:")
    for it in items:
        print(f"  {it.item_id} -> Value: {it.value}, Weight: {it.weight}, Ratio (v/w): {it.ratio:.2f}")
        
    max_val, details = fractional_knapsack(items, knapsack_capacity)
    
    print("\n--- Greedy Selection Schedule ---")
    total_w = 0.0
    for d in details:
        total_w += d["weight_taken"]
        print(f"  {d['item_id']}: Taken {d['fraction']*100:5.1f}% | Weight: {d['weight_taken']:5.1f} | Value Contribution: {d['value_taken']:6.2f}")
        
    print("-" * 70)
    print(f"  Total Weight Packed : {total_w:.2f} / {knapsack_capacity}")
    print(f"  Maximum Value Achieved: {max_val:.2f}")
    print("=" * 70)


if __name__ == "__main__":
    main()
