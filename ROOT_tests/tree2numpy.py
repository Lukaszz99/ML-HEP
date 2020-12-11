import ROOT as root
import numpy as np
import pandas as pd





tree = root.TTree('tree', 'tutorial') #class gbl.TTree

x = np.empty((1), dtype="float32")
y = np.empty((1), dtype="float32")
tree.Branch("x", x, "x/F")
tree.Branch("y", y, "y/F")

for i in range(4):
    x[0] = i
    y[0] = -i
    tree.Fill()

print("Tree content:\n{}\n".format(
    np.asarray([[tree.x, tree.y] for event in tree])))

for event in range(0, tree.GetEntries()):
    print(tree.Show(event))

    
array = tree.AsMatrix()
print("Tree converted to a numpy array:\n{}\n".format(array))

# Get numpy array and according labels of the columns
array, labels = tree.AsMatrix(return_labels=True)
print("Return numpy array and labels:\n{}\n{}\n".format(labels, array))

# Apply numpy methods on the data
print("Mean of the columns retrieved with a numpy method: {}\n".format(
    np.mean(array, axis=0)))

# Read only specific branches
array = tree.AsMatrix(columns=["x"])
print("Only the content of the branch 'x':\n{}\n".format(np.squeeze(array)))

array = tree.AsMatrix(exclude=["x"])
print("Read all branches except 'x':\n{}\n".format(np.squeeze(array)))

# Get an array with a specific data-type
array = tree.AsMatrix(dtype="int")
print("Return numpy array with data-type 'int':\n{}\n".format(array))


data, columns = tree.AsMatrix(return_labels=True)
df = pd.DataFrame(data=data, columns=columns)
print("Tree converted to a pandas.DataFrame:\n{}".format(df))