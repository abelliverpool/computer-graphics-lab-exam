#question 3 

import numpy as np

def reconstruct_matrix(U, S, V):
    
    
    if S.shape[0] != S.shape[1]:
        raise ValueError("S must be a square matrix")

   
    reconstructed_matrix = U @ S @ V.T

    return reconstructed_matrix