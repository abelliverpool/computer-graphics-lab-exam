#question 2 
import numpy as np

def compute_cross_product(vector1, vector2):
    
    # Check if the vectors have the correct dimensions
    if len(vector1) != 3 or len(vector2) != 3:
        raise ValueError("Both vectors must have 3 elements")

    # Compute the cross product using the determinant formula
    cross_product = np.array([
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0]
    ])

    return cross_product

# Create two 3D vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Compute the cross product
cross_product = compute_cross_product(vector1, vector2)

print(cross_product)

