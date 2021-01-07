# Huffman Coding in python
import sys
import tkinter as tk
from tkinter import filedialog
choice = input("Hi! Your Choices Are : [Console : 1]  [File : 2]\nPlease Enter Your Choice :")
if choice == '1':
    string=input("Enter Your String :")
elif choice=='2' :
    root = tk.Tk()
    #root.withdraw()
    file_path = filedialog.askopenfilename()
    #root.mainloop()
    #root.destroy()
    with open(file_path,'r') as f :
        string=''.join(f.readlines())
       
if len(string)==1:
    print('0')
    exit(0)
# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])
print(' Char | Huffman code ')
print('----------------------')

for (char, frequency) in freq:
    print(char,'   |   ',huffmanCode[char])
    
output=''
for c in string:
    output=output+huffmanCode[c]
my_set=set()    
for item in string:
    my_set.add(item)
simple_coding_length=(len(bin(len(my_set)))-2)*len(string)
print(f"Huffman Code : {output}\tLength : {len(output)}")
print(f"Simple Coding Length : {simple_coding_length}")
print(f"Tafazol : {simple_coding_length-len(output)}")

