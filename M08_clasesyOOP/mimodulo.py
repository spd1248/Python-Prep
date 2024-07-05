class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def verifica_primo(self):
        '''
        Verifica si los números en la lista son primos.
        '''
        for i in self.lista:
            if self.__verifica_primo(i):
                print(f'El elemento {i} SÍ es un número primo')
            else:
                print(f'El elemento {i} NO es un número primo')

    def conversion_grados(self, origen, destino):
        '''
        Convierte los grados de la lista de un origen a un destino específico.
        '''
        for i in self.lista:
            conversion = self.__conversion_grados(i, origen, destino)
            if conversion is not None:
                print(f'{i} grados {origen} son {conversion} grados {destino}')

    def factorial(self):
        '''
        Calcula el factorial de los números en la lista.
        '''
        for i in self.lista:
            print(f'El factorial de {i} es {self.__factorial(i)}')

    def __verifica_primo(self, nro):
        if nro < 2:
            return False
        for i in range(2, int(nro ** 0.5) + 1):
            if nro % i == 0:
                return False
        return True

    def valor_modal(self, menor=True):
        '''
        Encuentra el valor modal (el más frecuente) en la lista.
        '''
        if len(self.lista) == 0:
            return None

        from collections import Counter
        conteo = Counter(self.lista)
        moda, maximo = conteo.most_common(1)[0]

        if menor:
            for elemento in conteo:
                if conteo[elemento] == maximo and elemento < moda:
                    moda = elemento
        else:
            for elemento in conteo:
                if conteo[elemento] == maximo and elemento > moda:
                    moda = elemento

        return moda, maximo

    def __conversion_grados(self, valor, origen, destino):
        if origen == destino:
            return valor

        if origen == 'celsius':
            if destino == 'farenheit':
                return (valor * 9 / 5) + 32
            elif destino == 'kelvin':
                return valor + 273.15
        elif origen == 'farenheit':
            if destino == 'celsius':
                return (valor - 32) * 5 / 9
            elif destino == 'kelvin':
                return ((valor - 32) * 5 / 9) + 273.15
        elif origen == 'kelvin':
            if destino == 'celsius':
                return valor - 273.15
            elif destino == 'farenheit':
                return ((valor - 273.15) * 9 / 5) + 32
        else:
            print('Parámetro de Origen incorrecto')
            return None

        print('Parámetro de Destino incorrecto')
        return None

    def __factorial(self, numero):
        if not isinstance(numero, int):
            return 'El número debe ser un entero'
        if numero < 0:
            return 'El número debe ser positivo'
        if numero == 0:
            return 1
        return numero * self.__factorial(numero - 1)

