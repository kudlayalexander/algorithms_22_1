import time
from typing import Any


def fibonacci_rec(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Recursive implementation.
    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """

    """Комментарий от студентка
        Код написан в рукерсивной манере, время вычисления повышается,
        т.к. нашей программе нужно по новой пересчитывать каждое значение подаваймого числа.
        Решением может стать запоминание цепочки решения, но это скинеть только для тех, 
        кто уже есть в данном списке(кто проходил уже рекурсию) 
    """

    """Код - пример для решения задачи х2
         def fib(num,mass):
        if num == 0: 
            return 0
        elif num == 1:
            return 1
        if mass is not None:
            if num in mass:
                return mass[num]
            mass[num] = fib(num-1,mass)+fib(num-2,mass)
        return mass[num]

    def main():
        mass = {}
        for num in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
               987, 1597, 2584, 4181, 6765, 10946, 17711]:
            start = time.time()
            resul = self.fib(num,mass)
            end = time.time()
            print(resul, f"Time: {end-start}")
    """
    
    if num == 0: 
        return 0 
    elif num == 1:
        return 1 

    return fibonacci_rec(num-1)+fibonacci_rec(num-2)



  

def fibonacci_iter(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Iterative implementation.
    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    
    """Комментарий от студанта
        Функция реализована по итеративному принципу и выполняется куда быстрее, 
        чем рекурсия, однако!!! мы так - же имеем то, что есть и в функции с рекурсией! 
        все числа вычисляются по новой, это занимает вермя, да не много, каких-то мили-секунды, 
        но есть возможность убрать эти мили-секунды, если мы будем передавать не 1 параметр, а 3:
        :param num: Число, до которого нужно пройти
        :param pred_num: Число которое уже было
        :params pred,predpred: результаты предидущих вычислений.
        И тогда мы сможем ускорить наши вычисления, отбросив не нужные вычисления, 
        т.к. у нас уже есть результат тех чисел, которые меньше числа, которое нужно найти.
    """
    
    """Пример кода, который ускорит вычисление итеративного плана: 
    import time
    def fib(num,num_pred=2,pred=1,predpred=1):

        if num == 0: 
            return (0,0,1,1) 
        elif num == 1:
            return (1,1,1,1) 

        for i in range(num_pred,num):
            predpred,pred = pred,pred+predpred
        resul = (pred,predpred)
        return resul


    def main():
        now = 1 
        predpred = 1
        num_pred = 2
        for num in [10, 20, 30, 35,50]:
            start = time.time()
            resul = fib(num,num_pred,now,predpred)
            end = time.time()
            print(resul[0], f"Time: {end-start}")
            now = resul[0]
            predpred = resul[1]
            num_pred = num

    if __name__ == '__main__':
        main() 


    Результат будет : 
    10 : 0.0009975433349609375 
    20 : 0.0
    30 : 0.0
    35 : 0.0
    50 : 0.0
    """
    
    if num == 0: 
        return 0 
    elif num == 1:
        return 1 
    
    pred = 1
    predpred = 1

    for i in range(2,num):
        predpred,pred = pred,pred+predpred
    return pred

def determinant(matrix) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    flag_row = False
    for i in matrix:
        if len(matrix) != len(i):
            flag_row = True
    
    if flag_row: 
        raise Exception("parametr is not a square matrix") 

    if len(matrix) == 1: 
        return matrix[0][0]
    
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    else:
        param = []
        for item in range(len(matrix)-1):
            for row in range(item,len(matrix)):
                param.append(matrix[row][item])
                for colum in range(item,len(matrix[row])):
                    matrix[row][colum] = (matrix[row][colum]/param[len(param)-1])
            for row in range(item+1,len(matrix)):
                for colum in range(item,len(matrix[row])):
                    matrix[row][colum] = (matrix[item][colum]-matrix[row][colum]) 
        param.append(matrix[len(matrix)-1][len(matrix)-1])
        resul = 1
        for i in param:
            resul *=i
        return round(resul)
            



            


def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')


def main():
    for num in [10, 20, 30, 35]:
        print_exec_time(lambda x: print(x, fibonacci_iter(x)), x=num)

    # matrix =[[1, -2, 3],
    #               [-4, 5, -6],
    #               [7, -8, 9]]
    # print(f'determinant: {determinant(matrix)}')


if __name__ == '__main__':
    main()