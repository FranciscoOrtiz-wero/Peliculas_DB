from model.model import Model
from view.view import View
from datetime import date


class Controller:
    """
    **********************************
    *  A controller for a movies DB  *
    **********************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.login_menu()


    """
    *********************************
    *       General Controller      *
    *********************************
    """

    def login_menu(self):
        o = '0'
        while 0 != '3':
            self.view.login_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.user_menu()
            elif o == '2':
                self.admin_menu()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    # ********************* Admin menu *********************************
    def admin_login(self):
        # admin = self.model.read_admin_pass()
        self.view.login_user()
        self.view.ask('Alias: ')
        alias = input()
        self.view.ask('Password: ')
        password = input()
        login = self.model.admin_login(alias, password)
        # if alias == admin[3]:
        if type(login) == list:
            self.view.show_pelicula_header(' Bien venido: '+alias+' ')
            # self.view.show_a_pelicula(alias)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            if login == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA.')
        # else:
        #     self.view.error('EL ADMINISTRADOR NO EXISTE')
        return


    def admin_menu(self):
        self.admin_login()
        o = '0'
        while 0 != '9':
            self.view.main_menu_administrador()
            self.view.option('9')
            o = input()
            if o == '1':
                self.salas_menu()
            elif o == '2':
                self.asientos_menu()
            elif o == '3':
                self.peliculas_menu()
            elif o == '4':
                self.directores_menu()
            elif o == '5':
                self.funciones_menu()
            elif o == '6':
                self.gest_admin_menu()
            elif o == '7':
                self.boleto_menu()
            elif o == '8':
                self.gest_user_menu()
            elif o == '9':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    # ****************************** user menu *************************
    def user_menu(self):
        self.create_usuario()
        o = '0'
        while 0 != '3':
            self.view.options_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.boleto_menu()
            elif o == '2':
                self.boleto_user()
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return



    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals


    """
    *********************************
    *   Controller for salas        *
    *********************************
    """
    def salas_menu(self):
        o = '0'
        while o != '6':
            self.view.sala_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_sala()
            elif o == '2':
                self.read_sala()
            elif o == '3':
                self.read_all_salas()
            elif o == '4':
                self.update_sala()
            elif o == '5':
                self.delete_sala()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_sala(self):
        self.view.ask('Numero de sala: ')
        sala = input()
        self.view.ask('Numero de asientos: ')
        asientos = input()
        return [sala,asientos]

    def create_sala(self):
        num_sala, num_asientos = self.ask_sala()
        out = self.model.create_sala(num_sala, num_asientos)
        if out == True:
            self.view.ok(num_sala, 'se agrego número de sala')
        else:
            if out.errno == 1062:
                self.view.error('NÚMERO DE SALA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL NUMERO DE SALA. REVISA.')
        return

    def read_sala(self):
        self.read_all_salas()
        self.view.ask('ID sala: ')
        id_sala = input()
        sala = self.model.read_sala(id_sala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos de la sala '+id_sala+' ')
            self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA ESTA EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA.')
        return sala

    def read_all_salas(self):
        salas = self.model.read_all_salas()
        if type(salas) == list:
            self.view.show_sala_header(' Todas las salas ')
            for sala in salas:
                self.view.show_a_sala(sala)
                self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS SALAS. REVISA.')
        return

    def update_sala(self):
        self.read_all_salas()
        self.view.ask('iD sala: ')
        id_sala = input()
        sala = self.model.read_sala(id_sala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos de la sala '+id_sala+' ')
            self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA.')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_sala()
        fields, vals = self.update_lists(['s_num_sala', 's_asientos'], whole_vals)
        vals.append(id_sala)
        vals = tuple(vals)
        out = self.model.update_sala(fields, vals)
        if out == True:
            self.view.ok(id_sala, 'sala actualizada')
        else:
            self.view.error('NO SE PUEDE ACTUALIZAR LA SALA. REVISA')
        return

    def delete_sala(self):
        self.read_all_salas()
        self.view.ask('ID sala a borrar: ')
        id_sala = input()
        count = self.model.delete_sala(id_sala)
        # print(count)
        if count != 0:
            self.view.ok(id_sala, 'sala se borro')
        else:
            if count == 0:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA SALA. REVISA')
        return

    
    """
    *********************************
    *   Controller for asientos     *
    *********************************
    """
    def asientos_menu(self):
        o = '0'
        while o != '6':
            self.view.asiento_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_asiento()
            elif o == '2':
                self.read_asiento()
            elif o == '3':
                self.read_all_asientos()
            elif o == '4':
                self.update_asiento()
            elif o == '5':
                self.delete_asiento()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_asiento(self):
        self.read_all_salas()
        self.view.ask('ID sala: ')
        id_sala = input()
        self.view.ask('Número de asiento: ')
        numero = input()
        self.view.ask('Fila: ')
        fila = input()
        self.view.ask('Disponible: ')
        disponible = input()
        return [id_sala, numero, fila, disponible]

    def create_asiento(self):
        id_sala, numero, fila, disponible = self.ask_asiento()
        out = self.model.create_asiento(id_sala, numero, fila, disponible)
        if out == True:
            self.view.ok(numero, ' se agrego asiento')
        else:
            if out.errno == 1062:
                self.view.error('NÚMERO DE ASIENTO REPETIDO')
            else:
                print(out)
                self.view.error('NO SE PUDO AGREGAR EL NUMERO DE ASIENTO. REVISA.')
        return

    def read_asiento(self):
        self.read_all_asientos()
        self.view.ask('ID asiento: ')
        id_asiento = input()
        asiento = self.model.read_asiento(id_asiento)
        if type(asiento) == tuple:
            self.view.show_asiento_header(' Datos de los asientos '+id_asiento+' ')
            self.view.show_a_asiento(asiento)
            self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            if asiento == None:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
        return

    def read_all_asientos(self):
        asientos = self.model.read_all_asientos()
        if type(asientos) == list:
            self.view.show_asiento_header(' Todas los asientos')
            for asiento in asientos:
                self.view.show_a_asiento(asiento)
                self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS. REVISA.')
        return

    def update_asiento(self):
        self.read_all_asientos()
        self.view.ask('iD asiento: ')
        id_asiento = input()
        asiento = self.model.read_asiento(id_asiento)
        if type(asiento) == tuple:
            self.view.show_asiento_header(' Datos de los asiento '+id_asiento+' ')
            self.view.show_a_asiento(asiento)
            self.view.show_asiento_midder()
            self.view.show_asiento_footer()
        else:
            if asiento == None:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_asiento()
        fields, vals = self.update_lists(['id_sala', 'a_numero', 'a_fila', 'a_dispoible'], whole_vals)
        vals.append(id_asiento)
        vals = tuple(vals)
        out = self.model.update_asiento(fields, vals)
        if out == True:
            self.view.ok(id_asiento, 'asiento actualizado')
        else:
            self.view.error('NO SE PUEDE ACTUALIZAR EL ASIENTO. REVISA')
        return

    def delete_asiento(self):
        self.read_all_asientos()
        self.view.ask('ID asiento a borrar: ')
        id_asiento = input()
        count = self.model.delete_asiento(id_asiento)
        # print(count)
        if count != 0:
            self.view.ok(id_asiento, 'asiento se borro')
        else:
            if count == 0:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ASIENTO. REVISA')
        return
    

    """
    *********************************
    *   Controller for películas    *
    *********************************
    """
    def peliculas_menu(self):
        o = '0'
        while o != '7':
            self.view.pelicula_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_pelicula()
            elif o == '2':
                self.read_a_pelicula()
            elif o == '3':
                self.read_all_peliculas()
            elif o == '4':
                self.read_pelicula_nombre()
            elif o == '5':
                self.update_pelicula()
            elif o == '6':
                self.delete_pelicula()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_pelicula(self):
        self.read_all_directores()
        self.view.ask('ID Director: ')
        id_director = input()
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Año: ')
        año = input()
        self.view.ask('Genero: ')
        genero = input()
        self.view.ask('Duración: ')
        duracion = input()
        self.view.ask('Clasificación: ')
        clasificacion = input()
        self.view.ask('Lenguaje: ')
        lenguaje = input()
        return [id_director, nombre, año, genero, duracion, clasificacion, lenguaje]

    def create_pelicula(self):
        id_director, nombre, año, genero, duracion, clasificacion, lenguaje = self.ask_pelicula()
        out = self.model.create_pelicula(id_director, nombre, año, genero, duracion, clasificacion, lenguaje)
        if out == True:
            self.view.ok(nombre, ' se agregó')
        else:
            if out.errno == 1062:
                self.view.error('PELÍCULA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR LA PELÍCULA. REVISA.')
        return

    def read_a_pelicula(self):
        self.read_all_peliculas()
        self.view.ask('ID película: ')
        id_pelicula = input()
        pelicula = self.model.read_a_pelicula(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_pelicula_header(' Datos de la película '+id_pelicula+' ')
            self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELÍCULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELÍCULA. REVISA.')
        return

    def read_all_peliculas(self):
        peliculas = self.model.read_all_peliculas()
        if type(peliculas) == list:
            self.view.show_pelicula_header(' Todas las películas')
            for pelicula in peliculas:
                self.view.show_a_pelicula(pelicula)
                self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELÍCULAS. REVISA.')
        return

    def read_pelicula_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        peliculas = self.model.read_pelicula_nombre(nombre)
        if type(peliculas) == list:
            self.view.show_pelicula_header(' Películas con el nombre: '+nombre+' ')
            for pelicula in peliculas:
                self.view.show_a_pelicula_name(pelicula)
                self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER PELÍCULAS POR NOMBRE. REVISA')
        return

    def update_pelicula(self):
        self.read_all_peliculas()
        self.view.ask('iD película: ')
        id_pelicula = input()
        pelicula = self.model.read_a_pelicula(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_pelicula_header(' Datos de la película '+id_pelicula+' ')
            self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELÍCULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELÍCULA. REVISA.')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_pelicula()
        fields, vals = self.update_lists(['id_director', 'p_nombre', 'p_año', 'p_genero', 'p_duracion', 'p_clasificacion', 'p_lenguaje'], whole_vals)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_pelicula(fields, vals)
        if out == True:
            self.view.ok(id_pelicula, 'película actualizada')
        else:
            self.view.error('NO SE PUEDE ACTUALIZAR LA PELÍCULA. REVISA')
        return

    def delete_pelicula(self):
        self.read_all_peliculas()
        self.view.ask('ID película a borrar: ')
        id_pelicula = input()
        count = self.model.delete_pelicula(id_pelicula)
        # print(count)
        if count != 0:
            self.view.ok(id_pelicula, 'película se borro')
        else:
            if count == 0:
                self.view.error('LA PELÍCULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA PELÍCULA. REVISA')
        return
    

    """
    ********************************
    *   Controller for director    *
    ********************************
    """
    def directores_menu(self):
        o = '0'
        while o != '7':
            self.view.director_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_director()
            elif o == '2':
                self.read_director()
            elif o == '3':
                self.read_all_directores()
            elif o == '4':
                self.read_director_nombre()
            elif o == '5':
                self.update_director()
            elif o == '6':
                self.delete_director()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_director(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido: ')
        apellido = input()
        return [nombre, apellido]

    def create_director(self):
        nombre, apellido = self.ask_director()
        out = self.model.create_director(nombre, apellido)
        if out == True:
            self.view.ok(nombre, ' director se agregó')
        else:
            if out.errno == 1062:
                self.view.error('DIRECTOR REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL DIRECTOR. REVISA.')
        return

    def read_director(self):
        self.read_all_directores()
        self.view.ask('ID director: ')
        id_director = input()
        director = self.model.read_director(id_director)
        if type(director) == tuple:
            self.view.show_director_header(' Datos del director '+id_director+' ')
            self.view.show_a_pelicula(director)
            self.view.show_director_midder()
            self.view.show_director_footer()
        else:
            if director == None:
                self.view.error('EL DIRECTOR NO EXISTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA.')
        return

    def read_all_directores(self):
        directores = self.model.read_all_directores()
        if type(directores) == list:
            self.view.show_director_header(' Todos los directores')
            for director in directores:
                self.view.show_a_director(director)
                self.view.show_director_midder()
            self.view.show_director_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA.')
        return

    def read_director_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        directores = self.model.read_director_nombre(nombre)
        if type(directores) == list:
            self.view.show_director_header(' Director con el nombre: '+nombre+' ')
            for director in directores:
                self.view.show_a_director(director)
                self.view.show_director_midder()
            self.view.show_director_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA.')
        return

    def update_director(self):
        self.read_all_directores()
        self.view.ask('iD director: ')
        id_director = input()
        director = self.model.read_director(id_director)
        if type(director) == tuple:
            self.view.show_director_header(' Datos del director '+id_director+' ')
            self.view.show_a_director(director)
            self.view.show_director_midder()
            self.view.show_director_footer()
        else:
            if director == None:
                self.view.error('EL DIRECTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA.')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_director()
        fields, vals = self.update_lists(['d_nombre', 'd_apellido'], whole_vals)
        vals.append(id_director)
        vals = tuple(vals)
        out = self.model.update_director(fields, vals)
        if out == True:
            self.view.ok(id_director, 'director actualizado')
        else:
            self.view.error('NO SE PUEDE ACTUALIZAR EL DIRECTOR. REVISA')
        return

    def delete_director(self):
        self.read_all_directores()
        self.view.ask('ID director a borrar: ')
        id_director = input()
        count = self.model.delete_director(id_director)
        # print(count)
        if count != 0:
            self.view.ok(id_director, 'director se borro')
        else:
            if count == 0:
                self.view.error('EL DIRECTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA.')
        return
    

    """
    ********************************
    *   Controller for funciones   *
    ********************************
    """
    def funciones_menu(self):
        o = '0'
        while o != '6':
            self.view.funcion_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_funcion()
            elif o == '2':
                self.read_funcion()
            elif o == '3':
                self.read_all_funciones()
            elif o == '4':
                self.update_funcion()
            elif o == '5':
                self.delete_funcion()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_funcion(self):
        self.read_all_peliculas()
        self.view.ask('ID pelicula: ')
        id_pelicula = input()
        self.read_all_salas()
        self.view.ask('ID sala: ')
        id_sala = input()
        self.view.ask('Fecha (AAAA-MM-DD): ')
        fecha = input()
        self.view.ask('Hora (HH:MM): ')
        hora = input()
        return [id_pelicula, id_sala, fecha, hora]

    def create_funcion(self):
        id_pelicula, id_sala, fecha, hora = self.ask_funcion()
        out = self.model.create_funcion(id_pelicula, id_sala, fecha, hora)
        if out == True:
            self.view.ok(id_pelicula, id_sala+' '+fecha+' '+hora+' función se agregó')
        else:
            if out.errno == 1062:
                self.view.error('FUNCIÓN REPETIDA REPETIDO')
            else:
                print(out)
                self.view.error('NO SE PUDO AGREGAR LA FUNCIÓN. REVISA.')
        return

    def read_funcion(self):
        self.read_all_funciones()
        self.view.ask('ID función: ')
        id_funcion = input()
        funcion = self.model.read_funcion(id_funcion)
        if type(funcion) == tuple:
            self.view.show_funcion_header(' Datos de la función '+id_funcion+' ')
            self.view.show_a_funcion(funcion)
            self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            if funcion == None:
                self.view.error('LA FUNCIÓN NO EXISTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA FUNCIÓN. REVISA.')
        return

    def read_all_funciones(self):
        funciones = self.model.read_all_funciones()
        if type(funciones) == list:
            self.view.show_funcion_header(' Todas las funciones')
            for funcion in funciones:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA FUNCIÓN. REVISA.')
        return

    def update_funcion(self):
        self.read_all_funciones()
        self.view.ask('iD funcion: ')
        id_funcion = input()
        funcion = self.model.read_funcion(id_funcion)
        if type(funcion) == tuple:
            self.view.show_funcion_header(' Datos de la función '+id_funcion+' ')
            self.view.show_a_funcion(funcion)
            self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            if funcion == None:
                self.view.error('LA FUNCIÓN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA FUNCIÓN. REVISA.')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_funcion()
        fields, vals = self.update_lists(['id_pelicula', 'id_sala', 'f_fecha', 'f_hora'], whole_vals)
        vals.append(id_funcion)
        vals = tuple(vals)
        out = self.model.update_funcion(fields, vals)
        if out == True:
            self.view.ok(id_funcion, 'función actualizada')
        else:
            self.view.error('NO SE PUEDE ACTUALIZAR LA FUNCIÓN. REVISA')
        return

    def delete_funcion(self):
        self.read_all_funciones()
        self.view.ask('ID función a borrar: ')
        id_funcion = input()
        count = self.model.delete_funcion(id_funcion)
        # print(count)
        if count != 0:
            self.view.ok(id_funcion, 'función se borro')
        else:
            if count == 0:
                self.view.error('LA FUNCIÓN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA FUNCIÓN. REVISA.')
        return
    


    """
    *************************************
    *   Controller for gestion admin    *
    *************************************
    """
    def gest_admin_menu(self):
        o = '0'
        while o != '7':
            self.view.admin_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_administrador()
            elif o == '2':
                self.read_administrador()
            elif o == '3':
                self.read_all_administrador()
            elif o == '4':
                self.read_administrador_alias()
            elif o == '5':
                self.update_administrador()
            elif o == '6':
                self.delete_administrador()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_admin(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellidos: ')
        apellido = input()
        self.view.ask('Alias: ')
        alias = input()
        self.view.ask('Password: ')
        password = input()
        return [nombre, apellido, alias, password]

    def create_administrador(self):
        nombre, apellido, alias, password = self.ask_admin()
        out = self.model.create_administrador(nombre, apellido, alias, password)
        if out == True:
            self.view.ok(alias, ' se agregó')
        else:
            if out.errno == 1062:
                self.view.error('ADMINISTRADOR REPETIDA')
            else:
                print(out)
                self.view.error('NO SE PUDO AGREGAR EL ADMINISTRADOR. REVISA.')
        return

    def read_administrador(self):
        self.read_all_administrador()
        self.view.ask('ID administrador: ')
        id_admin = input()
        admin = self.model.read_administrador(id_admin)
        if type(admin) == tuple:
            self.view.show_admin_header(' Datos del administrador '+id_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA.')
        return

    def read_all_administrador(self):
        admins = self.model.read_all_administrador()
        if type(admins) == list:
            self.view.show_admin_header(' Todos los administradores')
            for admin in admins:
                self.view.show_a_admin(admin)
                self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA.')
        return

    def read_administrador_alias(self):
        self.view.ask('Alias: ')
        alias = input()
        admins_alias = self.model.read_administrador_alias(alias)
        if type(admins_alias) == list:
            self.view.show_admin_header(' Administradores con el alias: '+alias+' ')
            for admin_alias in admins_alias:
                self.view.show_a_admin(admin_alias)
                self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            self.view.error('PROBLEMA AL EL ADMINISTRADOR POR ALIAS. REVISA')
        return

    def update_administrador(self):
        self.read_all_administrador()
        self.view.ask('iD administrador: ')
        id_admin = input()
        admin = self.model.read_administrador(id_admin)
        if type(admin) == tuple:
            self.view.show_pelicula_header(' Datos del administrador '+id_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA.')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_admin()
        fields, vals = self.update_lists(['a_nombre', 'a_apellido', 'a_alias', 'a_pass'], whole_vals)
        vals.append(id_admin)
        vals = tuple(vals)
        out = self.model.update_administrador(fields, vals)
        if out == True:
            self.view.ok(id_admin, 'administrador actualizadado')
        else:
            self.view.error('NO SE PUEDE ACTUALIZAR EL ADMINISTRADOR. REVISA')
        return

    def delete_administrador(self):
        self.read_all_administrador()
        self.view.ask('ID administrador a borrar: ')
        id_admin = input()
        count = self.model.delete_administrador(id_admin)
        # print(count)
        if count != 0:
            self.view.ok(id_admin, 'administrador se borro')
        else:
            if count == 0:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ADMINISTRADOR. REVISA')
        return
    

    """
    *************************************
    *   Controller for gestion users    *
    *************************************
    """
    def gest_user_menu(self):
        o = '0'
        while o != '6':
            self.view.usuario_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_usuario()
            elif o == '2':
                self.read_usuario()
            elif o == '3':
                self.read_all_usuarios()
            elif o == '4':
                self.update_usuario()
            elif o == '5':
                self.delete_usuario()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_user(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellidos: ')
        apellidos = input()
        return [ nombre, apellidos]

    def create_usuario(self):
        nombre, apellidos = self.ask_user()
        out = self.model.create_usuario(nombre, apellidos)
        if out == True:
            self.view.ok(nombre, ' se agregó')
        else:
            if out.errno == 1062:
                self.view.error('USUARIO REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL USUARIO. REVISA.')
        return

    def read_usuario(self):
        self.read_all_usuarios()
        self.view.ask('ID usuario: ')
        id_user = input()
        user = self.model.read_usuario(id_user)
        if type(user) == tuple:
            self.view.show_usuario_header(' Datos del usuario '+id_user+' ')
            self.view.show_a_usuario(user)
            self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            if user == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
        return

    def read_all_usuarios(self):
        users = self.model.read_all_usuarios()
        if type(users) == list:
            self.view.show_usuario_header(' Todos los usuarios')
            for user in users:
                self.view.show_a_usuario(user)
                self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
        return

    def update_usuario(self):
        self.read_all_usuarios()
        self.view.ask('iD usuario: ')
        id_user = input()
        user = self.model.read_usuario(id_user)
        if type(user) == tuple:
            self.view.show_pelicula_header(' Datos de los asiento '+id_user+' ')
            self.view.show_a_usuario(user)
            self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            if user == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_user()
        fields, vals = self.update_lists(['u_nombre', 'u_apellidos'], whole_vals)
        vals.append(id_user)
        vals = tuple(vals)
        out = self.model.update_usuario(fields, vals)
        if out == True:
            self.view.ok(id_user, 'usuario actualizado')
        else:
            self.view.error('NO SE PUEDE ACTUALIZAR EL USUARIO. REVISA')
        return

    def delete_usuario(self):
        self.read_all_usuarios()
        self.view.ask('ID usuario a borrar: ')
        id_user = input()
        count = self.model.delete_usuario(id_user)
        # print(count)
        if count != 0:
            self.view.ok(id_user, 'usuario se borro')
        else:
            if count == 0:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL USUARIO. REVISA')
        return

    """
    *********************************
    *   Controller for compras      *
    *********************************
    """
    def compras_menu(self):
        o = '0'
        while o != '6':
            self.view.asiento_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_compra()
            elif o == '2':
                self.read_compra()
            elif o == '3':
                self.read_all_compra()
            elif o == '4':
                self.update_compra()
            elif o == '5':
                self.delete_compra()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_compra(self):
        self.view.ask('Total: ')
        # precio = self.read_a_boleto()
        # total = precio[5]
        total = input()   #this ------------------------------------
        return [total]

    def create_compra(self):
        total = self.ask_compra()
        out = self.model.create_compra(total)
        if out == True:
            self.view.ok(total, ' se agrego compra')
        else:
            if out.errno == 1062:
                self.view.error('ID DE COMPRA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR LA COMPRA. REVISA.')
        return

    def read_compra(self):
        self.read_all_compra()
        self.view.ask('ID compra: ')
        id_compra = input()
        compra = self.model.read_compra(id_compra)
        if type(compra) == tuple:
            self.view.show_compra_header(' Datos de la compra '+id_compra+' ')
            self.view.show_a_compra(compra)
            self.view.show_compra_midder()
            self.view.show_compra_footer()
        else:
            if compra == None:
                self.view.error('LA COMPRA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA COMPRA. REVISA.')
        return

    def read_all_compra(self):
        compras = self.model.read_all_compra()
        if type(compras) == list:
            self.view.show_compra_header(' Todas las compras')
            for compra in compras:
                self.view.show_a_compra(compra)
                self.view.show_compra_midder()
            self.view.show_compra_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA COMPRA. REVISA.')
        return

    def update_compra(self):
        self.read_all_compra()
        self.view.ask('iD compra: ')
        id_compra = input()
        compra = self.model.read_compra(id_compra)
        if type(compra) == tuple:
            self.view.show_compra_header(' Datos de la compra '+id_compra+' ')
            self.view.show_a_compra(compra)
            self.view.show_compra_midder()
            self.view.show_compra_footer()
        else:
            if compra == None:
                self.view.error('LA COMPRA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA COMPRA. REVISA.')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_compra()
        fields, vals = self.update_lists(['id_compra', 'c_total'], whole_vals)
        vals.append(id_compra)
        vals = tuple(vals)
        out = self.model.update_compra(fields, vals)
        if out == True:
            self.view.ok(id_compra, 'compra actualizada')
        else:
            self.view.error('NO SE PUEDE ACTUALIZAR LA COMPRA. REVISA')
        return

    def delete_compra(self):
        self.read_all_compra()
        self.view.ask('ID compra a borrar: ')
        id_compra = input()
        count = self.model.delete_compra(id_compra)
        # print(count)
        if count != 0:
            self.view.ok(id_compra, 'compra se borro')
        else:
            if count == 0:
                self.view.error('LA COMPRA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA COMPRA. REVISA')
        return

    """
    *************************************
    *   Controller for boleto menu   *
    *************************************
    """
    
    def boleto_menu(self):
        o = '0'
        while o != '6':
            self.view.boleto_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_boleto()
            elif o == '2':
                self.read_a_boleto()
            elif o == '3':
                self.update_boleto()
            elif o == '4':
                self.delete_boleto()
            elif o == '5':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_boleto(self):
        self.read_all_usuarios()
        self.view.ask('ID user: ')
        id_user = input()
        self.read_all_funciones()
        self.view.ask('ID funcion: ')
        id_funcion = input()
        self.read_all_salas()
        self.view.ask('ID sala: ')
        id_sala = input()
        self.read_all_asientos()
        self.view.ask('ID asiento: ')
        id_asiento = input()
        costo = 60
        return [id_user, id_funcion, id_sala, id_asiento, costo]

    def create_boleto(self):
        id_user, id_funcion, id_sala, id_asiento, costo = self.ask_boleto()
        out = self.model.create_boleto(id_user, id_funcion, id_sala, id_asiento, costo)
        if out == True:
            self.view.ok(id_user, 'agregó boleto')
        else:
            if out.errno == 1062:
                self.view.error('BOLETO REPETIDO')
            else:
                print(out)
                self.view.error('NO SE PUDO AGREGAR EL BOLETO. REVISA.')
        return

    def read_a_boleto(self):
        self.view.ask('ID boleto: ')
        id_boleto = input()
        boleto = self.model.read_a_boleto(id_boleto)
        if type(boleto) == tuple:
            self.view.show_boleto_header(' Datos del boleto '+id_boleto+' ')
            self.view.show_a_boleto(boleto)
            self.view.show_boleto_midder()
            self.view.show_boleto_footer()
        else:
            if boleto == None:
                self.view.error('EL BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL BOLETO. REVISA.')
        return boleto

    def update_boleto(self):
        self.view.ask('iD boleto: ')
        id_boleto = input()
        boleto = self.model.read_administrador(id_boleto)
        if type(boleto) == tuple:
            self.view.show_boleto_header(' Datos del boleto '+id_boleto+' ')
            self.view.show_a_boleto(boleto)
            self.view.show_boleto_midder()
            self.view.show_boleto_footer()
        else:
            if boleto == None:
                self.view.error('EL BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL BOLETO. REVISA.')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_boleto()
        fields, vals = self.update_lists(['id_user', 'id_funcion', 'id_sala', 'id_asiento', 'b_costo'], whole_vals)
        vals.append(id_boleto)
        vals = tuple(vals)
        out = self.model.update_boleto(fields, vals)
        if out == True:
            self.view.ok(id_boleto, 'boleto actualizadado')
        else:
            self.view.error('NO SE PUEDE ACTUALIZAR EL BOLETO. REVISA')
        return

    def delete_boleto(self):
        self.view.ask('ID boleto a borrar: ')
        id_boleto = input()
        count = self.model.delete_boleto(id_boleto)
        # print(count)
        if count != 0:
            self.view.ok(id_boleto, 'boleto se borro')
        else:
            if count == 0:
                self.view.error('EL BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL BOLETO. REVISA')
        return

    # --------------- boleto compra --------------------------------
    """
    *************************************
    *   Controller for boleto compra   *
    *************************************
    """    
    def create_boleto_compra(self, id_boleto):
        self.view.ask('ID compra: ')
        id_compra = input()
        if id_compra != '':
            compra = self.model.read_compra(id_compra)
            if type(compra) == tuple:
                self.view.show_compra_header(' Datos de la compra '+id_compra+' ')
                self.view.show_a_compra(compra)
                self.view.show_compra_footer()
                out = self.model.create_boleto_compra(id_boleto, id_compra)
                if out == True:
                    self.view.ok(id_boleto+' | '+id_compra, 'agrego a el boleto comprado')
                else:
                    if out.errno == 1062:
                        self.view.error('ESTÉ BOLETO YA FUE COMPRADO')
                    else:
                        self.view.error('NO SE PUDO AGREGAR EL BOLETO COMPRADO. REVISA')
            else:
                if compra == None:
                    self.view.error('LA COMPRA NO EXISTE')
                else:
                    self.view.error('NO SE PUDO AGREGAR LA COMPRA. REVISA')
        else:
            if compra == None:
                self.view.error('LA COMPRA  NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA COMPRA . REVISA')
        return id_compra 

    def add_boleto_compra(self):
        boleto = self.read_a_boleto()
        if type(boleto) == tuple:
            id_boleto = boleto[0]
            id_compra = ' '
            while id_compra != '':
                self.view.msg('---- Agregar boleto comprado (deja vacio el id de la compra para salir) ----')
                id_compra = self.create_boleto_compra(id_boleto)
            self.model.update_boleto_compra( id_boleto, id_compra)
        return

    def update_boleto_compra(self):
        boleto = self.read_a_boleto()
        if type(boleto) == tuple:
            id_boleto = boleto[0]
            id_compra = ' '
            while id_compra != '':
                self.view.msg('---- Modifica Boleto comprado (deja vacio el id del producto para salir) ----')
                self.view.ask('ID compra: ')
                id_compra = input()
                if id_compra != '':
                    boleto_compra = self.model.read_a_boleto_compra(id_boleto, id_compra)
                    if type(boleto_compra) == tuple:
                        whole_vals = [id_boleto, id_compra]
                        fields, vals = self.update_lists(['id_boleto','id_compra'], whole_vals)
                        vals.append(id_boleto)
                        vals = tuple(vals)
                        self.model.update_boleto_compra(fields, whole_vals)
                        self.view.ok(id_boleto, 'actualizo en el boleto')
                    else: 
                        if boleto_compra == None:
                            self.view.error('EL BOLETO NO ESTA COMPRADO')
                        else:
                            self.view.error('PROBLEMA AL ACTUALIZAR EL BOLETO COMPRADO. REVISA.')
        return

    def delete_boleto_compra(self):
        boleto = self.read_a_boleto()
        if type(boleto) == tuple:
            id_boleto = boleto[0]
            id_compra = ' '
            while id_compra != '':
                self.view.msg('---- Borra BOLETO COMPRADO (deja vacio el id del producto para salir) ---')
                self.view.ask('ID compra: ')
                id_compra = input()
                if id_compra != '':
                    boleto_compra = self.model.read_a_boleto_compra(id_boleto, id_compra)
                    count = self.model.delete_boleto_compra(id_boleto, id_compra)
                    if type(boleto_compra) == tuple and count != 0:
                        self.view.ok(id_boleto, 'boleto comprado eliminado')
                    else:
                        if boleto_compra == None:
                            self.view.error('EL BOLETO COMPRADO NO EXISTE')
                        else:
                            self.view.error('PROBLEMA AL BORRAR EL BOLETO COMPRADO. REVISA')
        return
            

    #/////////////////   USER OPTIONS   /////////////////////////////////////////
    """
    *************************************
    *   Controller for cartelera menu   *
    *************************************
    """
    
    def cartelera_menu(self):
        o = '0'
        while o != '6':
            self.view.cartelera_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.read_cartelera()
            elif o == '2':
                self.read_funcion_fecha()
            elif o == '3':
                self.read_funcion_hora()
            elif o == '4':
                self.read_funcion_peli_hora()
            elif o == '5':
                self.boleto_user()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def read_cartelera(self):
        carteleras = self.model.read_cartelera()
        if type(carteleras) == list:
            self.view.show_funcion_header(' Todas las funciones')
            for cartelera in carteleras:
                self.view.show_a_cartelera(cartelera)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA FUNCIÓN. REVISA.')
        return

    def read_funcion_fecha(self):
        self.view.ask('Funciones en el día: ')
        date = input()
        fechas = self.model.read_funcion_fecha(date)
        if type(fechas) == list:
            self.view.show_funcion_header(' Funciones con la fecha: '+date+' ')
            for fecha in fechas:
                self.view.show_a_funcion_fecha(fecha)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA FECHA. REVISA.')
        return

    def read_funcion_hora(self):
        self.view.ask('Hora (HH:MM): ')
        hour = input()
        horas = self.model.read_funcion_hora(date)
        if type(horas) == list:
            self.view.show_funcion_header(' Funciones con la hora: '+hour+' ')
            for hora in horas:
                self.view.show_a_funcion_hora(hora)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA HORA. REVISA.')
        return
    
    def read_funcion_peli_hora(self):
        self.view.ask('Nombre pelicula: ')
        n_peli = input()
        peliculas = self.model.read_funcion_peli_hora(n_peli)
        if type(peliculas) == list:
            self.view.show_funcion_header(' Horarios de la Pelicula: '+n_peli+' ')
            for pelicula in peliculas:
                self.view.show_a_funcion_hora(pelicula)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS HORARIOS DE LA PELICULA. REVISA.')
        return

    def boleto_user(self):
        self.create_boleto()
        return
    
    



    