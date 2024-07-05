from nada_dsl import *
def nada_main():

    party1 = Party(name="Party1")

    # Define input matrices as secret integers
    matrix_a = [
        [SecretInteger(Input(name=f"a_{i}_{j}", party=party1)) for j in range(2)]
        for i in range(2)
    ]
    matrix_b = [
        [SecretInteger(Input(name=f"b_{i}_{j}", party=party1)) for j in range(2)]
        for i in range(2)
    ]

    # Perform matrix multiplication
    result_matrix = [
        [
            (matrix_a[i][0] * matrix_b[0][j]) + (matrix_a[i][1] * matrix_b[1][j])
            for j in range(2)
        ]
        for i in range(2)
    ]

    # Define the output
    outputs = []
    for i in range(2):
        for j in range(2):
            outputs.append(Output(result_matrix[i][j], name=f"result_{i}_{j}", party=party1))

    return outputs
