class Matrix:
    def __init__(self, par_1):
        self.matrix_list = par_1

    def __str__(self):
        return 'Ваша матрица: \n' + '\n'.join(['\t'.join(map(str, line)) for line in self.matrix_list])

    def __add__(self, other):
        # return (list(map(
        #     lambda x, y: list(map(lambda z, w: z + w, x, y)),
        #     self.matrix_list, other)))
        new_list = []
        for i in range(len(self.matrix_list)):
            new_list.append(list(map(lambda x, y: x + y, self.matrix_list[i], other.matrix_list[i])))
        return new_list


List_a = [1, 2, 3], [4, 5, 6, ], [7, 8, 9], [10, 11, 12]
List_b = [0, 1, 2], [-3, 0, 3], [1, 1, 1], [-5, -6, 6]
matrix_a = Matrix(List_a)
print(matrix_a)
matrix_b = Matrix(List_b)
print(matrix_b)
sum_matrix = matrix_a + matrix_b
matrix_c = Matrix(sum_matrix)
print(matrix_c)
