/*Creación de una tabla*/
CREATE TABLE cars (
  marca VARCHAR(255),
  modelo VARCHAR(255),
  anio INT
);

SELECT * FROM cars;

INSERT INTO cars (marca, modelo, anio)
VALUES ('Suzuki', 'Baleno', 2013);

INSERT INTO cars (marca, modelo, anio)
VALUES ('Ford', 'x2', 2000);

DROP TABLE cars;

SELECT modelo, anio FROM cars;

ALTER TABLE cars
ADD color VARCHAR(255);

UPDATE cars
SET color = 'red'
WHERE marca = 'Ford';

/*Modificando la columna anio--> cambiar de tipo INT a VARCHAR(4)*/
ALTER TABLE cars
ALTER COLUMN anio TYPE VARCHAR(4);

/*Cambiar la colorcolumna de VARCHAR(255)a VARCHAR(30)*/
ALTER TABLE cars
ALTER COLUMN color TYPE VARCHAR(30);

/*Eliminar la columna color*/
ALTER TABLE cars
DROP COLUMN color;

SELECT * FROM cars;

DELETE FROM cars
WHERE marca = 'Ford' AND modelo = 'x2' ;

/*Ejemplo con borrado por id*/
ALTER TABLE cars
ADD id INT;

UPDATE cars
SET id = 3
WHERE marca = 'Suzuki';

DELETE FROM cars
WHERE id = 3;
/*========================*/

UPDATE cars
SET id = 1
WHERE marca = 'Ford';

INSERT INTO cars (marca, modelo, anio, id)
VALUES ('Suzuki', 'Baleno', 2013, 2);

DROP TABLE cars;

/*========================== Nueva Tabla con otro formato ==============*/
CREATE TABLE roles (
	id_rol SERIAL NOT NULL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL UNIQUE,
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE usuarios (
	id_usuario SERIAL NOT NULL PRIMARY KEY,
	nombre VARCHAR(150) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	password VARCHAR(8) NOT NULL,
	id_rol INT NOT NULL REFERENCES roles(id_rol),
	created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
	updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

INSERT INTO roles (nombre) VALUES('Admin'), ('Cliente');
SELECT * FROM roles;

INSERT INTO usuarios (nombre, email, password, id_rol)
VALUES ('Sandra', 'Sandra.contacto@gmail.com', '1234', 1),
	   ('Luis', 'Luis.contacto@gmail.com', '1234', 2), 
	   ('Exequiel', 'Exequiel.contacto@gmail.com', '1234', 1);

SELECT * FROM usuarios;




