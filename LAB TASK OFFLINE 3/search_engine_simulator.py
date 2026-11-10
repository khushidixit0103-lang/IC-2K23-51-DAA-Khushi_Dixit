"""
Program: search_engine_simulator.py
Description: Search Engine Simulator:
             - Stores a predefined dictionary of >= 30 technical/academic words
             - Implements lookup via:
               1. Binary Search on sorted vocabulary list
               2. Hash Table with Separate Chaining
               3. Hash Table with Linear Probing
             - Custom polynomial rolling hash function
             - Reports search results and counts comparisons / probes for all three methods
Student: Khushi Dixit | Roll No: IC-2K23-51
Lab: DAA Offline Lab 3 (Section E.8)
"""

def custom_hash(key_str, table_size):
    """
    Polynomial rolling hash function:
    hash = sum(ord(char) * 31^i) % table_size
    """
    h = 0
    prime = 31
    for char in key_str:
        h = (h * prime + ord(char)) % table_size
    return h


# ====================================================
# 1. Hash Table with Separate Chaining
# ====================================================
class SeparateChainingHashTable:
    def __init__(self, size=17):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        idx = custom_hash(key, self.size)
        # Check if key already exists
        for item in self.table[idx]:
            if item[0] == key:
                item[1] = value
                return
        self.table[idx].append([key, value])

    def search(self, key):
        idx = custom_hash(key, self.size)
        probes = 0
        bucket = self.table[idx]
        for item in bucket:
            probes += 1
            if item[0] == key:
                return item[1], probes, idx
        return None, probes, idx


# ====================================================
# 2. Hash Table with Linear Probing
# ====================================================
class LinearProbingHashTable:
    def __init__(self, size=61):  # Sufficient capacity to avoid infinite loop
        self.size = size
        self.table = [None] * size

    def insert(self, key, value):
        idx = custom_hash(key, self.size)
        initial_idx = idx
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
            idx = (idx + 1) % self.size
            if idx == initial_idx:
                raise Exception("Hash table full!")
        self.table[idx] = (key, value)

    def search(self, key):
        idx = custom_hash(key, self.size)
        initial_idx = idx
        probes = 0
        while self.table[idx] is not None:
            probes += 1
            if self.table[idx][0] == key:
                return self.table[idx][1], probes, idx
            idx = (idx + 1) % self.size
            if idx == initial_idx:
                break
        return None, probes, idx


# ====================================================
# 3. Binary Search on Sorted Word List
# ====================================================
def binary_search_words(sorted_vocab, target_word):
    low = 0
    high = len(sorted_vocab) - 1
    comparisons = 0
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        mid_word, mid_doc = sorted_vocab[mid]
        if mid_word == target_word:
            return mid_doc, comparisons, mid
        elif mid_word < target_word:
            low = mid + 1
        else:
            high = mid - 1
    return None, comparisons, -1


def get_vocabulary():
    # 35 academic/algorithms words with mock doc_ids & frequencies
    return [
        ("algorithm",    {"doc_id": "DOC_01", "freq": 14}),
        ("array",        {"doc_id": "DOC_02", "freq": 28}),
        ("backtracking", {"doc_id": "DOC_03", "freq": 19}),
        ("binary",       {"doc_id": "DOC_04", "freq": 32}),
        ("bubble",       {"doc_id": "DOC_05", "freq": 8}),
        ("chaining",     {"doc_id": "DOC_06", "freq": 11}),
        ("collision",    {"doc_id": "DOC_07", "freq": 15}),
        ("complexity",   {"doc_id": "DOC_08", "freq": 22}),
        ("conquer",      {"doc_id": "DOC_09", "freq": 17}),
        ("database",     {"doc_id": "DOC_10", "freq": 9}),
        ("determinant",  {"doc_id": "DOC_11", "freq": 6}),
        ("divide",       {"doc_id": "DOC_12", "freq": 17}),
        ("dynamic",      {"doc_id": "DOC_13", "freq": 25}),
        ("fibonacci",    {"doc_id": "DOC_14", "freq": 12}),
        ("graph",        {"doc_id": "DOC_15", "freq": 30}),
        ("greedy",       {"doc_id": "DOC_16", "freq": 21}),
        ("hashing",      {"doc_id": "DOC_17", "freq": 26}),
        ("heap",         {"doc_id": "DOC_18", "freq": 18}),
        ("insertion",    {"doc_id": "DOC_19", "freq": 14}),
        ("knapsack",     {"doc_id": "DOC_20", "freq": 16}),
        ("linear",       {"doc_id": "DOC_21", "freq": 23}),
        ("matrix",       {"doc_id": "DOC_22", "freq": 27}),
        ("merge",        {"doc_id": "DOC_23", "freq": 20}),
        ("partition",    {"doc_id": "DOC_24", "freq": 10}),
        ("probing",      {"doc_id": "DOC_25", "freq": 13}),
        ("queue",        {"doc_id": "DOC_26", "freq": 15}),
        ("quick",        {"doc_id": "DOC_27", "freq": 24}),
        ("radix",        {"doc_id": "DOC_28", "freq": 7}),
        ("recursion",    {"doc_id": "DOC_29", "freq": 31}),
        ("selection",    {"doc_id": "DOC_30", "freq": 12}),
        ("sorting",      {"doc_id": "DOC_31", "freq": 45}),
        ("sparse",       {"doc_id": "DOC_32", "freq": 16}),
        ("stack",        {"doc_id": "DOC_33", "freq": 18}),
        ("traversal",    {"doc_id": "DOC_34", "freq": 22}),
        ("tree",         {"doc_id": "DOC_35", "freq": 29})
    ]


def query_search_engine(query, sorted_vocab, chain_hash, probe_hash):
    q = query.strip().lower()
    print(f"\n=======================================================")
    print(f"SEARCH QUERY: '{q}'")
    print(f"=======================================================")
    
    # 1. Binary search
    bs_val, bs_steps, bs_idx = binary_search_words(sorted_vocab, q)
    
    # 2. Hash with Separate Chaining
    ch_val, ch_steps, ch_idx = chain_hash.search(q)
    
    # 3. Hash with Linear Probing
    lp_val, lp_steps, lp_idx = probe_hash.search(q)
    
    print(f"{'Lookup Method':<26} | {'Found?':<8} | {'Document Info / Payload':<26} | {'Steps (Comparisons/Probes)'}")
    print("-" * 88)
    
    found_str_bs = "YES" if bs_val else "NO"
    payload_bs = f"Doc: {bs_val['doc_id']}, Freq: {bs_val['freq']}" if bs_val else "Not In Index"
    print(f"{'1. Binary Search':<26} | {found_str_bs:<8} | {payload_bs:<26} | {bs_steps} comparisons (Index {bs_idx})")
    
    found_str_ch = "YES" if ch_val else "NO"
    payload_ch = f"Doc: {ch_val['doc_id']}, Freq: {ch_val['freq']}" if ch_val else "Not In Index"
    print(f"{'2. Hash (Separate Chaining)':<26} | {found_str_ch:<8} | {payload_ch:<26} | {ch_steps} bucket probe(s) (Bucket {ch_idx})")
    
    found_str_lp = "YES" if lp_val else "NO"
    payload_lp = f"Doc: {lp_val['doc_id']}, Freq: {lp_val['freq']}" if lp_val else "Not In Index"
    print(f"{'3. Hash (Linear Probing)':<26} | {found_str_lp:<8} | {payload_lp:<26} | {lp_steps} slot probe(s) (Slot {lp_idx})")
    print("=" * 88)


def main():
    print("=" * 65)
    print("  DAA OFFLINE LAB 3: SEARCH ENGINE SIMULATOR")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)
    
    vocab = get_vocabulary()
    sorted_vocab = sorted(vocab, key=lambda x: x[0])
    
    # Initialize Hash Tables
    chain_table = SeparateChainingHashTable(size=17)
    probe_table = LinearProbingHashTable(size=67)
    
    for word, payload in vocab:
        chain_table.insert(word, payload)
        probe_table.insert(word, payload)
        
    print(f"Index successfully populated with {len(vocab)} distinct dictionary words.")
    
    while True:
        print("\n--- Search Engine Menu ---")
        print("1. Search for a word")
        print("2. Run automated multi-word test comparison")
        print("3. Display all indexed dictionary words")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            q = input("Enter word to search: ")
            query_search_engine(q, sorted_vocab, chain_table, probe_table)
            
        elif choice == "2":
            print("\n>>> Running Automated Multi-Word Comparison <<<")
            test_queries = ["algorithm", "hashing", "sorting", "quantum"]
            for tq in test_queries:
                query_search_engine(tq, sorted_vocab, chain_table, probe_table)
            print(">>> Automated Comparison Complete <<<")
            
        elif choice == "3":
            print("\nIndexed Words (Alphabetical):")
            for i, (w, p) in enumerate(sorted_vocab, 1):
                print(f"  {i:>2}. {w:<16} ({p['doc_id']})", end="\n" if i % 3 == 0 else " ")
            print()
            
        elif choice == "4":
            print("Exiting Search Engine Simulator.")
            break
        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
