from mysql  import connector

class Model:
    """"
    ***********************************************************
    A data model with Mysql for buying a ticket for a movie. 
    ***********************************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()


    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()



    """
    ******************************
    *       Director methods     *
    ******************************
    """
    def create_director(self, nombre, apellido):
        try:
            sql = 'INSERT INTO director (`d_nombre`, `d_apellido`) VALUES (%s, %s)'
            vals = (nombre, apellido)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_director(self, id_director):
        try:
            sql =  'SELECT * FROM director WHERE id_director = %s'
            vals = (id_director,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_directores(self): 
        try:
            sql =  'SELECT * FROM director'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_director_nombre(self, nombre):
        try:
            sql =  'SELECT * FROM director WHERE d_nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
            
    def update_director(self, fields, vals):
        try:
            sql = 'UPDATE director SET '+','.join(fields)+' WHERE id_director = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_director(self, id_director):
        try:
            sql =  'DELETE FROM director WHERE id_director = %s'
            vals = (id_director,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ******************************
    *       Pelicula methods     *
    ******************************
    """
    def create_pelicula(self, id_director, nombre, año, genero, duracion, clasificacion, lenguaje):
        try:
            sql = 'INSERT INTO pelicula (`id_director`, `p_nombre`, `p_año`, `p_genero`, `p_duracion`, `p_clasificacion`, `p_lenguaje`) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            vals = ( id_director, nombre, año, genero, duracion, clasificacion, lenguaje )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_pelicula(self, id_pelicula):
        try:
            sql = 'SELECT * FROM pelicula WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_all_peliculas(self):   
        try:
            sql =  'SELECT * FROM pelicula'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_pelicula_nombre(self, nombre):
        try:
            sql =  'SELECT * FROM pelicula WHERE p_nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def update_pelicula(self, fields, vals):
        try:
            sql = 'UPDATE pelicula SET '+','.join(fields)+' WHERE id_pelicula = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_pelicula(self, id_pelicula):
        try:
            sql =  'DELETE FROM pelicula WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ******************************
    *       Sala methods     *
    ******************************
    """
    def create_sala(self, num_sala, asientos):
        try:
            sql = 'INSERT INTO sala (`s_num_sala`, `s_asientos`) VALUES (%s, %s)'
            vals = (num_sala, asientos)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_sala(self, id_sala):
        try:
            sql =  'SELECT * FROM sala WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_salas(self): 
        try:
            sql =  'SELECT * FROM sala'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
            
    def update_sala(self, fields, vals):
        try:
            sql = 'UPDATE sala SET '+','.join(fields)+' WHERE id_sala = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_sala(self, id_sala):
        try:
            sql =  'DELETE FROM sala WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    
    """
    ******************************
    *       Asientos methods     *
    ******************************
    """
    def create_asiento(self, id_sala, numero, fila, disponible):
        try:
            sql = 'insert into asiento (`id_sala`, `a_numero`, `a_fila`, `a_dispoible`) values (%s, %s, %s, %s);'
            vals = ( id_sala, numero, fila, disponible)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_asiento(self, id_asiento):
        try:
            sql =  'SELECT * FROM asiento WHERE id_asiento = %s'
            vals = (id_asiento,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_asientos(self): 
        try:
            sql =  'SELECT * FROM asiento'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_asientos_sala(self, id_sala): 
        try:
            sql =  'SELECT asiento.id_asiento, sala.id_sala, asiento.a_numero, asiento.a_fila, asiento.a_disponible FROM Sala JOIN asiento On sala.id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
            
    def update_asiento(self, fields, vals):
        try:
            sql = 'UPDATE asiento SET '+','.join(fields)+' WHERE id_asiento = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_asiento(self, id_asiento):
        try:
            sql =  'DELETE FROM asiento WHERE id_asiento = %s'
            vals = (id_asiento,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ******************************
    *       Funcion methods     *
    ******************************
    """
    def create_funcion(self, id_pelicula, id_sala, fecha, hora):
        try:
            sql = 'insert into funcion (`id_pelicula`, `id_sala`, `f_fecha`, `f_hora`) values (%s, %s, %s, %s)'
            vals = (id_pelicula, id_sala, fecha, hora)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_funcion(self, id_funcion):
        try:
            sql =  'SELECT * FROM funcion WHERE id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_funciones(self): 
        try:
            sql =  'SELECT * FROM funcion'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_cartelera(self): 
        try:
            sql =  'SELECT funcion.id_funcion, pelicula.p_nombre, sala.s_num_sala, funcion.f_fecha, funcion.f_hora FROM funcion JOIN pelicula ON pelicula.id_pelicula = funcion.id_pelicula JOIN sala ON funcion.id_sala = sala.id_sala'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def read_funcion_fecha(self, fecha): 
        try:
            sql =  'SELECT pelicula.p_nombre, funcion.f_fecha FROM funcion JOIN pelicula ON pelicula.id_pelicula = funcion.id_pelicula AND DAY(funcion.f_fecha) = %s'
            vals = (fecha,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_funcion_hora(self, hora): 
        try:
            sql =  'SELECT pelicula.p_nombre, funcion.f_hora FROM funcion JOIN pelicula ON pelicula.id_pelicula = funcion.id_pelicula AND funcion.f_hora = %s '
            vals = (hora,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_funcion_peli_hora(self, pelicula): 
        try:
            sql =  'SELECT pelicula.p_nombre, funcion.f_fecha, funcion.f_hora FROM funcion JOIN pelicula ON pelicula.id_pelicula = funcion.id_pelicula and pelicula.p_nombre = %s'
            vals = (pelicula,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_funcion_datos(self): 
        try:
            sql =  'SELECT funcion.id_funcion, pelicula.id_pelicula, pelicula.p_nombre, sala.id_sala, sala.s_num_sala, funcion.f_fecha, funcion.f_hora FROM funcion JOIN pelicula ON pelicula.id_pelicula = funcion.id_pelicula JOIN sala ON funcion.id_sala = sala.id_sala'
            self.cursor.execute(sql,)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

            
    def update_funcion(self, fields, vals):
        try:
            sql = 'UPDATE funcion SET '+','.join(fields)+' WHERE id_funcion = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_funcion(self, id_funcion):
        try:
            sql =  'DELETE FROM funcion WHERE id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err




    """
    ******************************
    *       User methods     *
    ******************************
    """
    def create_usuario(self, nombre, apellidos):
        try:
            sql = 'INSERT INTO usuario (`u_nombre`, `u_apellidos`) VALUES (%s, %s)'
            vals = (nombre, apellidos)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_usuario(self, id_user):
        try:
            sql =  'SELECT * FROM usuario WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_usuarios(self): 
        try:
            sql =  'SELECT * FROM usuario'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
            
    def update_usuario(self, fields, vals):
        try:
            sql = 'UPDATE usuario SET '+','.join(fields)+' WHERE id_user = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_usuario(self, id_user):
        try:
            sql =  'DELETE FROM usuario WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err



    """
    ******************************
    *       Admin methods     *
    ******************************
    """
    def admin_login(self, alias, password):
        try:
            sql =  'SELECT * FROM administrador WHERE a_alias = %s and a_pass = %s'
            vals = (alias, password)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def create_administrador(self, nombre, apellido, alias, password):
        try:
            sql = 'INSERT INTO administrador (`a_nombre`, `a_apellido`, `a_alias`, `a_pass`) VALUES (%s, %s, %s, %s)'
            vals = (nombre, nombre, apellido, alias, password)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_administrador(self, id_admin):
        try:
            sql =  'SELECT * FROM administrador WHERE id_admin = %s'
            vals = (id_admin,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_administrador(self): 
        try:
            sql =  'SELECT * FROM administrador'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_administrador_alias(self, alias):
        try:
            sql =  'SELECT * FROM administrador WHERE a_alias = %s'
            vals = (alias)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_admin_pass(self, alias, password):
        try:
            sql =  'SELECT * FROM administrador WHERE a_alias = %s AND a_pass = %s'
            vals = (alias)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
            
    def update_administrador(self, fields, vals):
        try:
            sql = 'UPDATE administrador SET '+','.join(fields)+' WHERE id_admin = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_administrador(self, id_admin):
        try:
            sql =  'DELETE FROM administrador WHERE id_admin = %s'
            vals = (id_admin,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err



    """
    ******************************
    *       Compra methods     *
    ******************************
    """
    def create_compra(self, total):
        try:
            sql = 'INSERT INTO compra (`c_total`) VALUES (%s)'
            vals = (total)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_compra(self, id_compra):
        try:
            sql =  'SELECT * FROM compra WHERE id_compra = %s'
            vals = (id_compra,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_compra(self): 
        try:
            sql =  'SELECT * FROM compra'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
            
    def update_compra(self, fields, vals):
        try:
            sql = 'UPDATE compra SET '+','.join(fields)+' WHERE id_compra = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_compra(self, id_compra):
        try:
            sql =  'DELETE FROM compra WHERE id_compra = %s'
            vals = (id_compra,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ******************************
    *   Boleto methods    *
    ******************************
    """

    def create_boleto(self, id_user, id_funcion, id_sala, id_asiento, costo):
        try:
            sql = 'insert into boleto (`id_user`,`id_funcion`,`id_sala`,`id_asiento`,`b_costo`) values (%s, %s, %s, %s, %s)'
            # print(sql)
            vals = ( id_user, id_funcion, id_sala, id_asiento, costo)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_boleto(self, id_boleto):
        try:
            sql =  'SELECT * FROM boleto WHERE id_boleto = %s'
            vals = (id_boleto,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err  

    def read_funciones_datos(self):
        try:
            sql =  'SELECT funcion.id_funcion, pelicula.id_pelicula, pelicula.p_nombre, sala.id_sala, sala.s_num_sala, funcion.f_fecha, funcion.f_hora FROM funcion JOIN pelicula ON pelicula.id_pelicula = funcion.id_pelicula JOIN sala ON funcion.id_sala = sala.id_sala'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
 

    def update_boleto(self, fields, vals):
        try:
            sql = 'UPDATE boleto SET '+','.join(fields)+' WHERE id_boleto = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_boleto(self, id_boleto):
        try:
            sql =  'DELETE FROM boleto WHERE id_boleto = %s'
            vals = (id_boleto,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    
    """
    ******************************
    *   boleto-compra methods    *
    ******************************
    """

    def create_boleto_compra(self, id_boleto, id_compra):
        try:
            sql = 'SELECT INTO boleto_compra (`id_boleto`,`id_compra`) VALUES (%s, %s)'
            vals = ( id_boleto, id_compra)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return id_boleto
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_boleto_compra(self, id_boleto, id_compra):
        try:
            sql =  'SELECT boleto.*, compra.c_total FROM boleto_compra JOIN compra ON boleto_compra.id_compra = compra.id_compra and boleto_compra.id_boleto = %s '
            vals = (id_boleto, id_compra)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err  

    def read_boletod_compra(self, id_boleto):
        try:
            sql =  'SELECT boleto.*, compra.c_total FROM boleto_compra JOIN compra ON boleto_compra.id_compra = compra.id_compra and boleto_compra.id_boleto = boleto.id_boleto '
            vals = (id_boleto)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err  

    def update_boleto_compra(self, fields, vals):
        try:
            sql = 'UPDATE boleto_compra SET '+','.join(fields)+' WHERE id_boleto = %s and id_compra = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_boleto_compra(self, id_boleto, id_compra):
        try:
            sql =  'DELETE FROM boleto_compra WHERE id_boleto = %s and id_compra = %s'
            vals = (id_boleto, id_compra)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    