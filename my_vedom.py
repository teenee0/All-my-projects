import pandas as pd
import numpy as np
from statistics import mean


class Vedomost:

    def __init__(self, dis):

        self.dis = dis
        print(31 * "_")

    def put_list_of_students(self, student):

        self.student = student
        self.copstud = student.copy()
        self.data = pd.DataFrame(columns=self.dis, index=student)

        print(self.data)
        print(31 * "_")

    def add_one_student(self, std):

        self.std = std
        self.data.loc[std] = [np.nan] * self.data.shape[1]

        print(self.data)
        print(31 * "_")

    def add_one_sub(self, sub):

        self.sub = sub
        self.data[self.sub] = [np.nan] * self.data.shape[0]

        print(self.data)
        print(31 * "_")

    def add_mark(self, name, sub, value):

        self.value = value
        self.name = name
        self.sub = sub

        if (type(self.data.loc[self.name, self.sub]) == float) and (type(self.value) is list):  # nan []
            self.data.loc[self.name, self.sub] = [i for i in self.value]


        elif (type(self.data.loc[self.name, self.sub]) == float) and (type(self.value) != list):  # nan 4
            self.data.loc[self.name, self.sub] = [self.value]


        elif (type(self.data.loc[self.name, self.sub]) == list) and (type(self.value) == int):  # [] 4
            self.data.loc[self.name, self.sub].append(self.value)


        elif (type(self.data.loc[self.name, self.sub]) == int) and (type(self.value) == list):  # 4 []
            self.data.loc[self.name, self.sub].extend(self.value)


        elif (type(self.data.loc[self.name, self.sub]) == list) and (type(self.value) == list):  # [] []
            self.data.loc[self.name, self.sub].extend(self.value)

        print(self.data)
        print(31 * "_")

    def delete_mark(self, name, sub):

        self.name = name
        self.sub = sub

        a = input(f"Сколько из оценок {self.name}, по предмету {self.sub} вы хотите удалить?\n(Одну или все):  ")

        if a == "все":
            self.data.loc[self.name, self.sub] = np.nan

        elif a == "одну":
            print(f'Какую из данных (выберите от 0 до конца)\n{self.data.loc[self.name, self.sub]}')
            b = int(input())
            self.data.loc[self.name, self.sub].pop(b)

        print(self.data)
        print(31 * "_")

    def count(self):

        print(f'В ведомости {self.data.shape[0]} студентов')
        print(31 * "_")

    def names(self):

        index = self.data.index

        for i in index:
            print(i)
        print(31 * "_")

    def get_marks(self, name, sub):

        self.name = name
        self.sub = sub

        print(f'У ученика {self.name} данные оценки {self.data.loc[self.name, self.sub]}')
        print(31 * "_")

    def mean(self):

        self.data_mean = self.data.copy()

        for i in self.data_mean.columns:
            for j in self.data_mean.index:
                if type(self.data_mean.loc[j, i]) == list:
                    self.data_mean.loc[j, i] = int(mean(self.data_mean.loc[j, i]))

        print("средний балл", 31 * "_", self.data_mean, 31 * "_", sep="\n")

    def show(self):

        print(self.data)


print(f"""Методы данного класса :
              при присвоении указать предметы массивом
              .put_list_of_students() - ввести список из студентов (list)
              .add_one_student() - добавить одного студента (в ковычках)
              .add_mark() - добавить оценку (имя студента в ковычках, предмет в ковычках, оценка в виде массива либо просто числа)
              .delete_mark() - удалить оценку (имя студента в ковычках, предмет в ковычках, оценка в виде массива либо просто числа)
              .count() - количество студентов
              .add_one_sub() - добавить один предмет (в ковычках)
              .names() - студенты группы
              .mean() - средний балл
              .show() - вывод таблицы""")

a = Vedomost(["fizra", "mat", "python"])
a.put_list_of_students(["max", "angelina", "kristina", "artur"])

a.add_one_student("vadim")
a.add_mark("kristina", "mat", 44)
a.add_mark("angelina", "mat", [5 for i in range(4)])
a.add_mark("artur", "mat", [1, 2, 44])
a.add_mark("max", "mat", 44)
# a.delete_mark("artur","mat")
a.count()
a.names()
a.add_one_sub("diskra")
a.get_marks("artur", "mat")
a.mean()
a.show()