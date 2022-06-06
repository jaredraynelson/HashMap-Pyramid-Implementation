'''
CREATED BY: JARED RAY NELSON
DATE: 6-21-2021

THIS FILE CONTAINS A CLASS HASHMAP WHICH USES
THE HASHING TO BETTER ACCESS DATA. THIS IS
INTENDED TO BE SIMILAR TO DICTIONARY ADT.
'''

from math import ceil

class HashMap():
    '''
    CREATES A DICTIONARY TYPE ADT WHICH
    ALLOWS THE USER TO STORE DATA AND
    RETRIEVE THE DATA FAST.
    '''
    def __init__(self):
        '''
        TAKES NO PARAMETERS:
        CREATES CAPACITY VALUE,
        SIZE VALUE WILL BE ZERO
        BECASUE INITIALLY IT WILL
        HAVE NO ELEMENTS. IT WILL
        HAVE A LYST OF LYSTS STRUCTURE.
        '''
        self.capacity_value = 7
        self.size_value = 0
        self.arr = [[] for i in range(self.capacity_value)]


    def __setitem__(self, key, val):
        '''
        USES THE NOTATION OF t[key] = val
        SAME ASS ADD.
        '''
        hash_value = self.get_hash_value(key)
        found = False
        for idx, element in enumerate(self.arr[hash_value]):
            if len(element) ==2 and element[0] == key:
                self.arr[hash_value][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[hash_value].append((key,val))


    def set(self, key, value):
        '''
        THIS SIMPLY POINTS TO THE ADD.
        '''
        self.add(key,value)


    def __getitem__(self, key):
        '''
        SAME AS .get BUT THIS USES
        t[key] TO ACCESS THE VALUES.
        '''
        hash_value = self.get_hash_value(key)
        if self.arr[hash_value] == []:
            return False
        for element in self.arr[hash_value]:
            if element == []:
                raise KeyError
            elif isinstance(key,tuple):
                if element[0][0] == key[0] and element[0][1] == key[1]:
                    return element[1]
            else:
                # CASE THAT IT'S AN INT OR STRING
                if element[0] == key:
                    return element[1]
        return False

    def __delitem__(self, key):
        '''
        ALLOWS FOR del (key) TO REMOVE THE
        VALUE FROM THE HASHMAP
        '''
        self.size_value -= 1
        hash_value = self.get_hash_value(key)
        for index, element in enumerate(self.arr[hash_value]):
            if element[0] == key:
                self.arr[hash_value][index] = []
                return
        raise KeyError


    def size(self):
        '''
        RETURNS THE SIZE
        '''
        return self.size_value


    def capacity(self):
        '''
        RETURNS THE HASHMAP'S
        CAPACITY
        '''
        return self.capacity_value


    def remove(self, key):
        '''
        REMOVES A VALUE FROM THE
        HASHMAP
        '''
        self.size_value -= 1
        hash_value = self.get_hash_value(key)
        for index, element in enumerate(self.arr[hash_value]):
            if element[0] == key:
                self.arr[hash_value][index] = []
                return
        raise KeyError


    def get_hash_value(self, key):
        '''
        DOES THE COMPUTING POWER & RETURNS
        THE HASHVALUE OR MODULUS DIVIDE OF
        STRING OR TUPLE
        '''
        if isinstance(key,int):
            return key % self.capacity_value
        elif isinstance(key,tuple):
            return ceil((key[0]+key[1])/2) % self.capacity_value
        else:
            hash_value = 0
            key = str(key)
            for char in key:
                hash_value += ord(char)
            return hash_value % self.capacity_value


    def add(self, key, val):
        '''
        ADD A KEY AND VALUE TO THE HASHMAP
        '''
        hash_value = self.get_hash_value(key)
        self.size_value += 1
        found = False
        for idx, element in enumerate(self.arr[hash_value]):
            if len(element) ==2 and element[0] == key:
                self.arr[hash_value][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[hash_value].append((key,val))
        self.size_check()


    def size_check(self):
        '''
        MAKES SURE THE SIZE OF THE HASHMAP IS
        ALWAYS ENOUGH FOR THE DATA.
        '''
        if (self.size_value/self.capacity_value) >= 0.8:
            self.capacity_value = (self.capacity_value * 2) - 1
            for i in range(self.capacity_value-len(self.arr)):
                self.arr.append([])


    def get(self, key):
        '''
        FINDS A VALUE AND RETURNS THE
        ELEMENTS VALUE.
        '''
        hash_value = self.get_hash_value(key)
        if self.arr[hash_value] == []:
            raise KeyError
        for element in self.arr[hash_value]:
            if element == []:
                raise KeyError
            elif isinstance(key,tuple):
                if element[0][0] == key[0] and element[0][1] == key[1]:
                    return element[1]
            else:
                # CASE THAT IT'S AN INT OR STRING
                if element[0] == key:
                    return element[1]
        return False


    def find(self, key):
        '''
        FINDS A VALUE AND RETURNS THE
        ELEMENTS VALUE.
        '''
        hash_value = self.get_hash_value(key)
        if self.arr[hash_value] == []:
            return False
        for element in self.arr[hash_value]:
            if element == []:
                raise KeyError
            elif isinstance(key,tuple):
                if element[0][0] == key[0] and element[0][1] == key[1]:
                    return element[1]
            else:
                # CASE THAT IT'S AN INT OR STRING
                if element[0] == key:
                    return element[1]
        return False

    def clear(self):
        '''
        RESETS THE HASHMAP TO THE ORIGINAL VALUES.
        '''
        self.capacity_value = 7
        self.arr = [[] for i in range(self.capacity_value)]
        self.size_value = 0



    def keys(self):
        '''
        PRINTS OUT THE KEY VALUES IN
        HASHMAP.
        '''
        lyst = []
        for column in self.arr:
            if column is not []:
                for item in column:
                    if item is not None:
                        lyst.append(item[0])
        return lyst
