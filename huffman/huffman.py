import heapq
from collections import Counter

# Step 1: Count frequencies
def build_frequency_table(text):
    return Counter(text)

# Step 2: Build Huffman Tree
def build_huffman_tree(freq_table):
    # Heap stores list: [frequency, [[char, code], ...]]
    heap = [[freq, [[char, ""]]] for char, freq in freq_table.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        low1 = heapq.heappop(heap)
        low2 = heapq.heappop(heap)

        # Add prefix to all entries in both subtrees
        for pair in low1[1]:
            pair[1] = '0' + pair[1]
        for pair in low2[1]:
            pair[1] = '1' + pair[1]

        # Merge subtrees
        merged = [low1[0] + low2[0]] + [low1[1] + low2[1]]
        heapq.heappush(heap, merged)

    # Flatten final list to get {char: code}
    huffman_dict = {}
    for char, code in heap[0][1]:
        huffman_dict[char] = code
    return huffman_dict

# Step 3: Encode
def encode(text, code_map):
    return ''.join(code_map[char] for char in text)

# Step 4: Decode
def decode(encoded_text, code_map):
    reverse_map = {v: k for k, v in code_map.items()}
    decoded = ""
    code = ""
    for bit in encoded_text:
        code += bit
        if code in reverse_map:
            decoded += reverse_map[code]
            code = ""
    return decoded

# Step 5: Run directly
text = input("Enter text to compress: ")
freq_table = build_frequency_table(text)
print("\nCharacter Frequencies:")
for char, freq in freq_table.items():
    print(f"{char}: {freq}")

code_map = build_huffman_tree(freq_table)
print("\nGenerated Huffman Codes:")
for char, code in code_map.items():
    print(f"{char}: {code}")

encoded = encode(text, code_map)
print("\nEncoded Binary String:")
print(encoded)

decoded = decode(encoded, code_map)
print("\nDecoded Text:")
print(decoded)
