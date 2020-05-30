class View:
    """
    ********************************
    *     A view for a movies DB   *
    ********************************
    """

    def start(self):
        print('============================')
        print('= ¡Bienvenido a Cinepolis! =')
        print('============================')

    def end(self):
        print('=================================')
        print('=        ¡Hasta la vista!       =')
        print('=================================')

    def login_menu(self):
        print('**********************************')
        print('* -- Menu de Inicio de secion -- *')
        print('**********************************')
        print('1. Usuario')
        print('2. Administrador')
        print('3. Salir')

    def main_menu_usuario(self):
        print('************************')
        print('* -- Menu Cartelera -- *')
        print('************************')
        print('1. Cartelera')
        print('2. Comprar Boleto')
        print('3. Salir')

    def main_menu_administrador(self):
        print('************************')
        print('* -- Menu Principal -- *')
        print('************************')
        print('1. Salas')
        print('2. Asientos')
        print('3. Películas')
        print('4. Directores')
        print('5. Funciones')
        print('6. Gestionar Administradores')
        print('7. Gestionar Usuarios')
        print('8. Boletos')
        print('9. Salir')

    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta de Nuevo')
    
    def ask(self, output):
        print(output, end='')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id)) + len(op) +24))
        print('+ ¡'+str(id)+' '+op+' correctamente! +')
        print('+'*(len(str(id)) + len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err) +4, '-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    def login_user(self):
        print('**********************************')
        print('* -- Menu Login Administrador -- *')
        print('**********************************')


    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    """
    ***************************************
    *     View for admin option salas     *
    ***************************************
    """
    def sala_menu(self):
        print('***********************')
        print('* -- Submenu Salas -- *')
        print('***********************')
        print('1. Agregar Sala')
        print('2. Mostrar Sala')
        print('3. Mostrar todas las Salas')
        print('4. Actualizar Sala')
        print('5. Borrar Sala')
        print('6. Regresar')

    def show_a_sala(self, record):
        print(f'{record[0]:<6}|{record[1]:<5}|{record[2]:<5}')

    def show_sala_header(self, header):
        print(header.center(78, '*'))
        print('id Sala '.ljust(6)+ '|'+'Numero de sala '.ljust(5)+'|'+'Num de asientos '.ljust(5))
        print('-'*78)

    def show_sala_midder(self):
        print('-'*78)

    def show_sala_footer(self):
        print('*'*78)

    
    """
    *****************************************
    *     View for admin option Asientos    *
    *****************************************
    """
    def asiento_menu(self):
        print('**************************')
        print('* -- Submenu Asientos -- *')
        print('**************************')
        print('1. Agregar asientos')
        print('2. Leer asiento')
        print('3. Leer todos los asiento')
        print('4. Actualizar asiento')
        print('5. Borrar asiento')
        print('6. Regresar')

    def show_a_asiento(self, record):
        print('ID asiento: ', record[0])
        print('ID Sala: ', record[1])
        print('Número de asiento: ', record[2])
        print('Fila: ', record[3])
        print('Disponible: ', record[4])

    def show_asiento_header(self, header):
        print(header.center(48, '*'))
        print('-'*48)

    def show_asiento_midder(self):
        print('-'*48)

    def show_asiento_footer(self):
        print('*'*48)
        
        
        
    """
    *****************************************
    *   View for admin option Directores    *
    *****************************************
    """
    def director_menu(self):
        print('****************************')
        print('* -- Submenu Directores -- *')
        print('****************************')
        print('1. Agregar director')
        print('2. Leer director')
        print('3. Leer todos los directores')
        print('4. Leer director por nombre')
        print('5. Actualizar director')
        print('6. Borrar director')
        print('7. Regresar')

    def show_a_director(self, record):
        print('ID Director: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido: ', record[2])

    def show_director_header(self, header):
        print(header.center(48, '*'))
        print('-'*48)

    def show_director_midder(self):
        print('-'*48)

    def show_director_footer(self):
        print('*'*48)

    
    
    """
    *****************************************
    *   View for admin option Películas     *
    *****************************************
    """
    def pelicula_menu(self):
        print('***************************')
        print('* -- Submenu Películas -- *')
        print('***************************')
        print('1. Agregar película')
        print('2. Leer película')
        print('3. Leer todas las películas')
        print('4. Leer películas por nombre')
        print('5. Actualizar película')
        print('6. Borrar película')
        print('7. Regresar')

    def show_a_pelicula(self, record):
        print('ID película: ', record[0] )
        print('ID Director: ', record[1] )
        print('Nombre: ', record[2])
        print('AÑo: ', record[3])
        print('Genero: ', record[4])
        print('Duracion (min): ', record[5])
        print('Clasificación: ', record[6])
        print('Lenguaje: ', record[7])
        
    def show_a_pelicula_name(self, record):
        print('ID Película: ', record[0])
        print('Nombre: ', record[2])
        print('Genero: ', record[4])
        print('Duracion: ', record[5], ' min')

    def show_pelicula_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_pelicula_midder(self):
        print('-'*53)

    def show_pelicula_footer(self):
        print('*'*53)

    
    """
    ***************************************
    *   View for admin option funciones   *
    ***************************************
    """
    def funcion_menu(self):
        print('***************************')
        print('* -- Submenu Funciones -- *')
        print('***************************')
        print('1. Agregar funcion')
        print('2. Leer funcion')
        print('3. Leer todas las funciones')
        print('4. Actualizar funcion')
        print('5. Borrar funcion')
        print('6. Regresar')

    def show_a_funcion(self, record):
        print('ID Funcion: ', record[0])
        print('ID Película: ', record[1])
        print('ID Sala: ', record[2])
        print('Fecha: ', record[3])
        print('Hora: ', record[4])

    def show_a_funcion_fecha(self, record):
        print('Pelicula: ', record[0])
        print('Fecha: ', record[1])

    def show_a_funcion_hora(self, record):
        print('Pelicula: ', record[0])
        print('Hora: ', record[2])

    def show_all_funcion_fecha_hora(self, record):
        print('Pelicula: ', record[0])
        print('Fecha: ', record[1])
        print('Fecha: ', record[2])

    def show_a_funcion_datos(self, record):
        print('ID Funcion: ', record[0])
        print('ID Pelicula: ', record[1])
        print('Pelicula: ', record[2])
        print('ID Sala: ', record[3])
        print('Sala: ', record[4])
        print('Fecha: ', record[5])
        print('Hora: ', record[6])
    

    def show_funcion_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_funcion_midder(self):
        print('-'*53)

    def show_funcion_footer(self):
        print('*'*53)


    """
    **********************************************
    *   View for admin option Gestionar Admins   *
    **********************************************
    """
    def admin_menu(self):
        print('********************************************')
        print('* -- Submenu Gestion de Administradores -- *')
        print('********************************************')
        print('1. Agregar administrador')
        print('2. Leer administrador')
        print('3. Leer todos los administrador')
        print('3. Leer administrador por alias')
        print('5. Actualizar administrador')
        print('6. Borrar administrador')
        print('7. Regresar')

    def show_a_admin(self, record):
        print('ID administrador: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido: ', record[2])
        print('Alias: ', record[3])

    def show_admin_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_admin_midder(self):
        print('-'*53)

    def show_admin_footer(self):
        print('*'*53)


    """
    **********************************************
    *   View for admin option Gestionar usuarios   *
    **********************************************
    """
    def usuario_menu(self):
        print('************************************')
        print('* -- Submenu Gestión de Usuario -- *')
        print('************************************')
        print('1. Agregar usuario')
        print('2. Leer usuario')
        print('3. Leer todos los usuarios')
        print('4. Actualizar usuario')
        print('5. Borrar usuario')
        print('6. Regresar')

    def show_a_usuario(self, record):
        print('ID usuario: ', record[0])
        print('Nombre: ', record[1])
        print('Apellidos: ', record[2])

    def show_usuario_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_usuario_midder(self):
        print('-'*53)

    def show_usuario_footer(self):
        print('*'*53)

    """
    ***********************
    *   View for compras  *
    ***********************
    """
    def compra_menu(self):
        print('*************************')
        print('* -- Submenu compras -- *')
        print('*************************')
        print('1. Agregar compra')
        print('2. Leer compra')
        print('3. Leer todas las compra')
        print('4. Actualizar compra')
        print('5. Borrar compra')
        print('6. Regresar')

    def show_a_compra(self, record):
        print('ID compra: ', record[0])
        print('Total: ', record[1])

    def show_compra_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_compra_midder(self):
        print('-'*53)

    def show_compra_footer(self):
        print('*'*53)
   

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    """
    *******************************
    *   View for user options   *
    *******************************
    """
    def options_menu(self):
        print('*****************************')
        print('* -- Submenu de opciones -- *')
        print('*****************************')
        print('1. Cartelera ')
        print('2. comprar boleto')
        print('3. Regresar')


    def show_options_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_options_midder(self):
        print('-'*53)

    def show_options_footer(self):
        print('*'*53)



    """
    *******************************
    *   View for user cartelera   *
    *******************************
    """
    def cartelera_menu(self):
        print('***************************')
        print('* -- Submenu Cartelera -- *')
        print('***************************')
        print('1. Leer cartelera')
        print('2. Leer cartelera por dias')
        print('3. Leer cartelera por horario')
        print('4. Leer horarios de una pelicula')
        print('5. Comprar Boleto')
        print('6. Regresar')

    def show_a_cartelera(self, record):
        print('ID Funcion: ', record[0])
        print('Película: ', record[1])
        print('Sala: ', record[2])
        print('Fecha: ', record[3])
        print('Hora: ', record[4])


    def show_cartelera_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_cartelera_midder(self):
        print('-'*53)

    def show_cartelera_footer(self):
        print('*'*53)


    """
    *******************************
    *   View for user boleto   *    chcar esta parte
    *******************************
    """
    def boleto_menu(self):
        print('*************************')
        print('* -- Submenu boleto -- *')
        print('*************************')
        print('1. Agregar boleto')
        print('2. Leer boleto')
        print('3. Actualizar boleto')
        print('4. Borrar boleto')
        print('5. Regresar')

    def show_a_boleto(self, record):
        print('ID boleto: ', record[0])
        print('ID user: ', record[1])
        print('ID funcion: ', record[2])
        print('ID sala: ', record[3])
        print('ID asiento: ', record[4])
        print('Costo: ', record[5])

    def show_boleto_header(self, header):
        print(header.center(53, '*'))
        print('-'*53)

    def show_boleto_midder(self):
        print('-'*53)

    def show_boleto_footer(self):
        print('*'*53)


    """
    *******************************
    *   View for boleto compra    * #checar esta parte
    *******************************
    """
    def show_a_boleto_compra(self, record):
        print(f'{record[0]:<5}|{record[1]:<20}|{record[2]:<20}|{record[3]:<11}|{record[4]:<9}|{record[5]:<11}')
        
    def show_boleto_compra_header(self):
        print('-'*81)
        print('ID'.ljust(5)+'|'+'Producto'.ljust(20)+'|'+'Marca'.ljust(20)+'|'+'Precio'.ljust(11)+'|'+'Cantidad'.ljust(9)+'|'+'Total'.ljust(11))
        print('-'*81)

    def show_boleto_compra_footer(self):
        print('-'*81)