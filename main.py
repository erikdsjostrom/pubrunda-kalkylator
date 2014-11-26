
from nations import *
from tsp_solver.greedy import solve_tsp


def main():
    path = []
    nation_name = ['Orvars', 'VG', 'GH', 'Hyttan', 'OG', 'Stocken',
                   'Wermlands', 'Glenns', 'Snerikes', 'Bettys',
                   'Svantes', 'Kronan', 'VDala']

    def make_symetric_matrix(nation_name):
        """A function that makes a symetric matrix of the
           distances between the nations"""
        matrix = []
        for i in range(len(nation_name)):
            row = []
            for j in range(len(nation_name)):
                row.append(nations[nation_name[i]][nation_name[j]][0])
            matrix.append(row)
        return matrix

    def readable_information(path_i):
        """Turns the information into something readable"""
        path_distance = 0
        path_time = 0
        for i in path_i:
            path.append(nation_name[i])

        for i in range(len(path) - 1):
                path_distance += nations[path[i]][path[i+1]][0]
                path_time += nations[path[i]][path[i+1]][1]
                # path_time += 30

        print(path)
        print(path_distance, " meters")
        print(path_time, " minutes")

    matrix = make_symetric_matrix(nation_name)  # Get the matrix

    path_i = solve_tsp(matrix)  # Solves the ts-problem

    readable_information(path_i)  # Get the information

if __name__ == '__main__':
    main()
