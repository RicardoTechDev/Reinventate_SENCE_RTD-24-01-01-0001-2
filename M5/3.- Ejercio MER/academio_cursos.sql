/*
Modelo (4 tablas)
* estudiantes (entidad principal)
* credenciales (1 a 1 con estudiantes)
* cursos
* inscripciones (tabla puente: muchos a muchos)


Una institución educativa necesita almacenar información sobre:
* Estudiantes
* Credenciales de acceso al sistema
* Cursos disponibles
* Inscripciones en cursos

PARTE 1: CREACIÓN DEL MODELO
Debe crear máximo 4 tablas:

1) ESTUDIANTES
* id_estudiante (clave primaria autoincremental)
* nombre
* email (único)

2) CREDENCIALES
* id_estudiante (clave primaria y clave foránea)
* username (único)
* password_hash

Relación: 1 a 1 con estudiantes.
3) CURSOS
* id_curso (clave primaria autoincremental)
* nombre (único)

4) INSCRIPCIONES
* id_inscripcion (clave primaria autoincremental)
* id_estudiante (clave foránea)
* id_curso (clave foránea)
* fecha_inscripcion

Debe evitarse que un estudiante se inscriba dos veces al mismo curso.
*/

/*
PARTE 2: RELACIONES
* Definir correctamente claves foráneas.
* Aplicar restricciones UNIQUE donde corresponda.
* Respetar cardinalidades.
*/

/*
PARTE 3: CONSULTAS CON JOIN
1. Listar estudiantes con su username.
2. Listar cursos con cantidad de inscritos.
3. Listar estudiantes con sus cursos.
4. Mostrar estudiantes sin cursos.
*/

/*
PARTE 4: PRUEBA DE RESTRICCIONES
Intentar:
- Insertar dos credenciales para el mismo estudiante.
- Inscribir dos veces al mismo estudiante en el mismo curso
*/

/*crear una nueva base de datos*/
CREATE DATABASE ACADEMIA_CURSOS

/*1.- Crear tabla estudiantes*/
CREATE TABLE estudiantes (
	id_estudiante SERIAL PRIMARY KEY,
	nombre VARCHAR(150) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL /*email (único)*/
);

/*2.- Credenciales*/
CREATE TABLE credenciales (
	id_estudiante INT NOT NULL PRIMARY KEY
	REFERENCES estudiantes(id_estudiante) ON DELETE CASCADE,
	username VARCHAR(60) NOT NULL UNIQUE, /* username (único)*/
	password_hash VARCHAR(8) NOT NULL
);

/*3.- CURSOS*/
CREATE TABLE cursos (
	id_curso SERIAL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL UNIQUE /*nombre (único)*/
);


/*4.- INSCRIPCIONES */
CREATE TABLE inscripciones (
	id_inscripcion SERIAL PRIMARY KEY,
	id_estudiante INT NOT NULL
	REFERENCES estudiantes(id_estudiante) ON DELETE CASCADE,
	id_curso INT NOT NULL
	REFERENCES cursos(id_curso) ON DELETE CASCADE,
	fecha_inscripcion DATE NOT NULL DEFAULT CURRENT_DATE,
	/*Esto evita que un estudiante se inscriba 2 veces al mismo curso*/
	UNIQUE (id_estudiante, id_curso)
);

/*===================================*/
/*         DATOS DE PRUEBA           */
/*===================================*/
INSERT INTO estudiantes (nombre, email) VALUES 
('Ana Pérez', 'ana@gmail.com'),
('Bruno Díaz', 'bruno@gmail.com'),
('Carla Soto', 'carla@gmail.com'),
('Alex Salazar', 'alex@gmail.com')

SELECT * FROM estudiantes;

INSERT INTO credenciales (id_estudiante, username, password_hash) VALUES
(1, 'ana_user', 'hola1234'),
(2, 'bruno_user', 'hola1234'),
(3, 'carla_user', 'hola1234'),
(4, 'alex_user', 'hola1234');

SELECT * FROM credenciales;

INSERT INTO cursos (nombre) VALUES
('Fundamentos de Python'),
('SQL'),
('Python Avanzado'),
('Fundamentos de Django');

SELECT * FROM cursos;

INSERT INTO inscripciones (id_estudiante, id_curso) VALUES
(1, 1), /*Ana --> Fundamentos de Python */
(1, 2), /*Ana --> SQL */
(2, 2), /*Bruno --> SQL*/
(2, 3), /*Bruno --> Python Avanzado*/
(3, 1), /*Carla --> Fundamentos de Python */
(3, 4); /*Carla --> Fundamentos de Django*/

SELECT * FROM inscripciones ORDER BY id_inscripcion DESC;

/*
PRUEBA DE RESTRICCIONES
Intentar:
- Insertar dos credenciales para el mismo estudiante.
- Inscribir dos veces al mismo estudiante en el mismo curso
*/

/*Detail: Ya existe la llave (id_estudiante)=(*/
INSERT INTO credenciales (id_estudiante, username, password_hash) VALUES
(1, 'ana_user2', 'hola_2_');

/*Detail: Ya existe la llave (id_estudiante, id_curso)=(1, 1).*/
INSERT INTO inscripciones (id_estudiante, id_curso) VALUES
(1, 1); /*Ana --> Fundamentos de Python */


/*============================================================*/
/*consultas para relaciones*/

/*Todo los estudiantes con sus credenciales*/
/*Relación 1 a 1*/
SELECT * FROM estudiantes
INNER JOIN credenciales on credenciales.id_estudiante = estudiantes.id_estudiante;

INSERT INTO estudiantes (nombre, email) VALUES ('Elena', 'elena@gmail.com');
SELECT * FROM estudiantes;

/*Estudiante con sus inscripciones*/
/*Relación 1 a muchos*/
SELECT e.nombre, i.id_inscripcion, i.fecha_inscripcion
FROM estudiantes e
INNER JOIN inscripciones i ON i.id_estudiante = e.id_estudiante
ORDER BY e.nombre;

SELECT e.nombre AS estudiante, cu.nombre AS curso, i.id_inscripcion, i.fecha_inscripcion
FROM estudiantes e
INNER JOIN inscripciones i ON i.id_estudiante = e.id_estudiante
INNER JOIN cursos cu ON cu.id_curso = i.id_curso
ORDER BY e.nombre;

/*Estudiantes con cursos*/
/*Relación muchos a muchos*/
SELECT e.nombre AS estudiante, cu.nombre AS curso
FROM estudiantes e
INNER JOIN inscripciones i ON i.id_estudiante = e.id_estudiante
INNER JOIN cursos cu ON cu.id_curso = i.id_curso
ORDER BY e.nombre;

/*Cantidad de estudiantes por cursos*/
SELECT cu.nombre AS curso, COUNT(*) AS estudiantes_inscritos
FROM cursos cu
JOIN inscripciones i ON i.id_curso = cu.id_curso
GROUP BY cu.nombre;

/*Estudiantes sin cursos*/
SELECT e.nombre AS estudiante, COUNT(i.id_inscripcion) AS cursos_inscritos
FROM estudiantes e
LEFT JOIN inscripciones i ON i.id_estudiante = e.id_estudiante
GROUP BY e.id_estudiante, e.nombre; 






