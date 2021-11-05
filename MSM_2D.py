'''
Description

author: Ursa Ursic
November 2021

This code does stuff...
'''
import numpy as np
import matplotlib.pyplot as plt
import random

N = 10
initial_crystal = [[i, j] for i in range(-N, N, 1) for j in range(-N, N, 1)]

initial_crystal += [[i, j] for i in range(10, 12, 1) for j in range(-1, 2, 1)]
initial_crystal += [[i, j] for i in range(-14, -10, 1) for j in range(8, 12, 1)]

# initial_crystal = [[-1, -1], [0, -1], [0, -2], [-1, 0], [0,0], [0,1], [0,2], [1, 0], [1, 1], [2, 1]]

moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def borders(crystal):
    border = []
    binding_sites = []
    for element in crystal:
        if any([[element[0]+i, element[1]+j] not in crystal for (i, j) in moves]):
            border.append(element)
            for (i, j) in moves:
                if [element[0] + i, element[1] + j] not in crystal:
                    binding_sites.append([element[0] + i, element[1] + j])
    return border, binding_sites


def add_guanine(border, binding_sites):
    bound = random.choice(binding_sites)
    plt.plot(bound[0], bound[1], 'bs', markersize=10)
    border.append(bound)
    count = binding_sites.count(bound)
    for _ in range(count):
        binding_sites.remove(bound)
    for (i, j) in moves:
        if [bound[0] + i, bound[1] + j] not in border:
            binding_sites.append([bound[0] + i, bound[1] + j])
    return border, binding_sites


def main():
    plot = 1
    initial_crystal_arr = np.array(initial_crystal)
    border, binding_sites = borders(initial_crystal)

    for steps in range(40):
        border, binding_sites = add_guanine(border, binding_sites)
        border_arr = np.array(border)
        binding_sites_arr = np.array(binding_sites)

        if plot:
            # print(initial_crystal)
            plt.plot(initial_crystal_arr[:, 0], initial_crystal_arr[:, 1], 'sc', alpha=0.8, markersize=10)
            plt.plot(border_arr[:, 0], border_arr[:, 1], 'sr', alpha=0.5, markersize=10)
            plt.plot(binding_sites_arr[:, 0], binding_sites_arr[:, 1], 'sg', alpha=0.5, markersize=10)
            plt.axis("equal")
            # plt.xlim(-10, 10)
            # plt.ylim(-10, 10)
            plt.show()
            plt.close()


if __name__ == "__main__":
    main()




