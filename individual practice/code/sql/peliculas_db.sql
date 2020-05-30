create database if not exists peliculas_db;

use peliculas_db;

create table if not exists director(

	id_director int not null auto_increment,
    d_nombre varchar(50) not null,
    d_apellido varchar(50) not null,
    
    PRIMARY KEY (id_director)
)ENGINE=INNODB;

create table if not exists pelicula(

	id_pelicula int not null auto_increment,
    id_director int,
    p_nombre varchar(50) not null,
    p_año int,
    p_genero varchar(35),
    p_duracion int,
    p_clasificacion VARCHAR(4),
    p_lenguaje varchar(20),
    
    PRIMARY KEY (id_pelicula),
    
    CONSTRAINT fk_director FOREIGN KEY(id_director)
        REFERENCES director(id_director)
        ON DELETE SET NULL	
        ON UPDATE CASCADE
)ENGINE=INNODB;

create table if not exists sala(

	id_sala int not null auto_increment,
    s_num_sala int not null,
    s_asientos int not null,
    
    PRIMARY KEY (id_sala)
)ENGINE=INNODB;

create table if not exists asiento(

	id_asiento int not null auto_increment,
    id_sala int,
    a_numero int not null,
    a_fila varchar(4) not null,
    a_dispoible int not null,
    
    PRIMARY KEY (id_asiento),
    
    CONSTRAINT fk_sala FOREIGN KEY(id_sala)
        REFERENCES sala(id_sala)
        ON DELETE SET NULL	
        ON UPDATE CASCADE
)ENGINE=INNODB;

create table if not exists funcion(

	id_funcion int not null auto_increment,
    id_pelicula int,
    id_sala int,
    f_fecha date not null,
    f_hora time ,
    
    PRIMARY KEY (id_funcion),
    
    CONSTRAINT fk_pelicula FOREIGN KEY(id_pelicula)
        REFERENCES pelicula(id_pelicula)
        ON DELETE SET NULL	
        ON UPDATE CASCADE,
        
	CONSTRAINT fk_sala_funcion FOREIGN KEY(id_sala)
        REFERENCES sala(id_sala)
        ON DELETE SET NULL	
        ON UPDATE CASCADE
)ENGINE=INNODB;

create table if not exists usuario(

	id_user int not null auto_increment,
    u_nombre varchar(30) not null,
    u_apellidos varchar(30),

    PRIMARY KEY (id_user)
)ENGINE=INNODB;

create table if not exists administrador(

	id_admin int not null auto_increment,
    a_nombre varchar(30) not null,
    a_apellido varchar(30),
    a_alias varchar(30) not null,
    a_pass varchar(30),
    
    PRIMARY KEY (id_admin)
)ENGINE=INNODB;

create table if not exists compra(

	id_compra int not null auto_increment,
    c_total varchar(30),
    
    PRIMARY KEY (id_compra)
)ENGINE=INNODB;

create table if not exists boleto(

	id_boleto int not null auto_increment,
    id_user int,
    id_funcion int,
    id_sala int,
    id_asiento int, 
    b_costo int not null,
    
    PRIMARY KEY (id_boleto),
    
    CONSTRAINT fk_user_boleto FOREIGN KEY(id_user)
        REFERENCES usuario(id_user)
        ON DELETE SET NULL	
        ON UPDATE CASCADE,
	
    CONSTRAINT fk_funcion_boleto FOREIGN KEY(id_funcion)
        REFERENCES funcion(id_funcion)
        ON DELETE SET NULL	
        ON UPDATE CASCADE,
	
    CONSTRAINT fk_sala_boleto FOREIGN KEY(id_sala)
        REFERENCES sala(id_sala)
        ON DELETE SET NULL	
        ON UPDATE CASCADE,
	
    CONSTRAINT fk_asiento_boleto FOREIGN KEY(id_asiento)
        REFERENCES asiento(id_asiento)
        ON DELETE SET NULL	
        ON UPDATE CASCADE
)ENGINE=INNODB;

create table if not exists boleto_compra(

    id_boleto  int not null,
    id_compra int not null,
    
    primary key(id_boleto, id_compra),
    
	constraint fkbol_com foreign key(id_boleto)
		references boleto(id_boleto)
        on delete cascade
        on update cascade,
	constraint fkcomp_bol foreign key(id_compra)
		references compra(id_compra)
        on delete cascade
        on update cascade
    
)ENGINE=INNODB;