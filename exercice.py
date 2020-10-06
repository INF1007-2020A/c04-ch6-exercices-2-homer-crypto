#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    dictionnaire = {}
    for element in range(len(some_list)):
        dictionnaire[some_list[element]] = element
    """        
    for index, elem in enumerate(some_list):
       dictionnaire[elem] = index
    """
    return dictionnaire


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    my_list = []
    for c in colors:
        if c in cnames:
            hexa = cnames[c]
            my_tuple = (c, hexa)
            my_list.append(my_tuple)
            #ou my_list.append((c, cnames[c])) sans les ligne de hexa = ... et my_tuple = ... pour moins de ligne de code
        else:
            print(f"La couleurs {c} n'existe pas!")
    return my_list


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350
    """
    list_x = [entier for entier in range(10000) if entier <15 or entier > 350]
    """
    return [entier for entier in range(10000) if entier <15 or entier > 350]


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    for key, value in model_dict.items():
        err_quad = 0
        for elem in value:
            err_quad += (elem[0] - elem[1])**2

        model_dict[key] = err_quad/len(value)

    return model_dict


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
