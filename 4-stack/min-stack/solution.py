class MinStack:
    __stack: list[int]
    __sorted_elems_indexes: list[int]

    def __init__(self):
        self.__stack = []
        self.__sorted_elems_indexes = []

    def push(self, val: int) -> None:
        self.__stack.append(val)
        if (
            len(self.__sorted_elems_indexes) == 0
            or val <= self.__stack[self.__sorted_elems_indexes[-1]]
        ):
            self.__sorted_elems_indexes.append(len(self.__stack) - 1)

    def pop(self) -> None:
        if len(self.__stack) > 0:
            popped_index = len(self.__stack) - 1
            if self.__sorted_elems_indexes[-1] == popped_index:
                self.__sorted_elems_indexes.pop()
            self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__stack[self.__sorted_elems_indexes[-1]]
