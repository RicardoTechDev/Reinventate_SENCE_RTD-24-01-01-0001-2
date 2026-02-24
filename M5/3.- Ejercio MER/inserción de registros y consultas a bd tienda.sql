-- =========================
-- 1) CÓDIGOS POSTALES
-- =========================
INSERT INTO public.codigos_postales (codigo_postal, localidad) VALUES
(1001, 'Santiago Centro'),
(1001, 'Santiago Centro'),
(1002, 'Providencia'),
(1003, 'Ñuñoa'),
(1004, 'La Florida'),
(1005, 'Maipú'),
(1006, 'Puente Alto'),
(2001, 'Concepción'),
(2002, 'Chillán'),
(2003, 'Los Ángeles'),
(2004, 'Talcahuano');

-- =========================
-- 2) CLIENTES
-- (Ojo: codigo_postal es UNIQUE en clientes, así que no lo repetimos)
-- =========================
INSERT INTO public.clientes
(dni, nombre, apellido, codigo_postal, direccion, telefono_fijo, telefono_celular, correo)
VALUES
('77777777-7','Felipe','Díaz',10012,'Las Eras 321',    NULL,'+56966666666','felipe.diaz@email.com'),
('11111111-1','Ana','Rojas', 1001,'Av. Principal 123', NULL,'+56911111111','ana.rojas@email.com'),
('22222222-2','Bruno','Pérez',1002,'Calle 2 #456',      NULL,'+56922222222','bruno.perez@email.com'),
('33333333-3','Carla','Soto', 1003,'Pasaje 9 #12',      NULL,'+56933333333','carla.soto@email.com'),
('44444444-4','Diego','Muñoz',1004,'Los Álamos 77',     NULL,'+56944444444','diego.munoz@email.com'),
('55555555-5','Elena','Vega', 1005,'Ruta 5 Km 10',      NULL,'+56955555555','elena.vega@email.com'),
('66666666-6','Felipe','Díaz',1006,'Las Flores 321',    NULL,'+56966666666','felipe.diaz@email.com');

-- =========================
-- 3) PRODUCTOS
-- =========================
INSERT INTO public.productos (id_producto, marca, talle, precio, stock) VALUES
(1,'Nike','M', 19990, 50),
(2,'Adidas','L', 17990, 40),
(3,'Puma','S', 15990, 35),
(4,'Reebok','M', 14990, 25),
(5,'New Balance','L', 22990, 30);

-- =========================
-- 4) PROVEEDORES
-- (Ojo: codigo_postal es UNIQUE en proveedores, así que no lo repetimos)
-- =========================
INSERT INTO public.proveedores
(id_proveedor, nro_puesto, nombre, apellido, codigo_postal, direccion, telefono_fijo, telefono_celular, correo)
VALUES
(1, 10, 'Mario','Fuentes', 2001,'Bodega Norte 100', NULL,'+56970000001','mario.fuentes@proveedor.com'),
(2, 12, 'Paula','Lagos',   2002,'Bodega Sur 200',   NULL,'+56970000002','paula.lagos@proveedor.com'),
(3, 15, 'Javier','Leiva',  2003,'Centro 300',       NULL,'+56970000003','javier.leiva@proveedor.com');

-- =========================
-- 5) VENTAS (FEBRERO 2026)
-- (fecha UNIQUE => todas distintas)
-- =========================
INSERT INTO public.ventas (id_venta, fecha, id_producto, dni, monto, forma_pago) VALUES
(1,  '2026-02-01 10:00:01-03', 1,'11111111-1',19990,'Tarjeta'),
(2,  '2026-02-01 12:15:02-03', 2,'11111111-1',17990,'Efectivo'),
(3,  '2026-02-02 09:05:03-03', 3,'11111111-1',15990,'Transferencia'),

(4,  '2026-02-03 11:20:01-03', 2,'22222222-2',17990,'Tarjeta'),
(5,  '2026-02-05 18:45:02-03', 5,'22222222-2',22990,'Tarjeta'),
(6,  '2026-02-06 10:10:03-03', 4,'22222222-2',14990,'Efectivo'),

(7,  '2026-02-07 14:30:01-03', 1,'33333333-3',19990,'Transferencia'),
(8,  '2026-02-08 16:00:02-03', 1,'33333333-3',19990,'Tarjeta'),
(9,  '2026-02-10 09:40:03-03', 3,'33333333-3',15990,'Efectivo'),

(10, '2026-02-10 12:00:01-03', 4,'44444444-4',14990,'Tarjeta'),
(11, '2026-02-11 17:25:02-03', 2,'44444444-4',17990,'Transferencia'),
(12, '2026-02-14 13:55:03-03', 5,'44444444-4',22990,'Tarjeta'),

(13, '2026-02-15 10:05:01-03', 3,'55555555-5',15990,'Efectivo'),
(14, '2026-02-16 19:20:02-03', 4,'55555555-5',14990,'Tarjeta'),
(15, '2026-02-18 08:35:03-03', 1,'55555555-5',19990,'Transferencia'),
(16, '2026-02-20 20:10:04-03', 5,'55555555-5',22990,'Tarjeta'),

(17, '2026-02-21 09:00:01-03', 2,'66666666-6',17990,'Efectivo'),
(18, '2026-02-22 11:15:02-03', 2,'66666666-6',17990,'Tarjeta'),
(19, '2026-02-24 16:40:03-03', 3,'66666666-6',15990,'Transferencia'),
(20, '2026-02-26 13:10:04-03', 1,'66666666-6',19990,'Tarjeta');

/*1) Detalle de ventas (JOIN clientes + productos + localidad)*/
SELECT
  v.id_venta,
  v.fecha,
  c.dni,
  c.nombre || ' ' || c.apellido AS cliente,
  p.marca,
  p.talle,
  v.monto,
  v.forma_pago,
  cp.localidad
FROM ventas v
JOIN clientes c        ON c.dni = v.dni /*Une cada venta con su cliente.*/
JOIN productos p       ON p.id_producto = v.id_producto /*Une cada venta con su producto.*/
/*Si el cliente sí tiene codigo_postal y existe en codigos_postales, trae cp.localidad.
Si el cliente no tiene código postal (NULL) o no existe en la tabla, 
igual mantiene la venta, pero cp.localidad queda NULL.*/
LEFT JOIN codigos_postales cp ON cp.codigo_postal = c.codigo_postal
ORDER BY v.fecha;/*Ordena el resultado por fecha (de más antigua a más nueva).*/
/*Si quisieras de más nueva a más antigua: ORDER BY v.fecha DESC.*/


/*2) Ventas del mes (Febrero 2026)*/
SELECT *            -- Selecciona todas las columnas de la tabla ventas
FROM ventas         -- Tabla principal (cada fila = 1 venta)
WHERE fecha >= '2026-02-01'::timestamptz  -- Desde el 1 de febrero 2026 (inclusive)
  AND
  -- Hasta el 1 de marzo 2026 (exclusive)
  -- (esto incluye TODO febrero, sin importar hora/minuto/segundo)
  fecha <  '2026-03-01'::timestamptz
ORDER BY fecha; -- Ordena las ventas por fecha (de más antigua a más nueva)


/*3) Total vendido a cliente en el mes (GROUP BY + JOIN)*/
SELECT
  c.dni,
  c.nombre || ' ' || c.apellido AS cliente,
  COUNT(*) AS cantidad_ventas,/*Contamos cuantas agrupadas por cliente (GROUP BY c.dni, c.nombre, c.apellido)*/
  SUM(v.monto) AS total_vendido
FROM ventas v
JOIN clientes c ON c.dni = v.dni
WHERE v.fecha >= '2026-02-01'::timestamptz
  AND v.fecha <  '2026-03-01'::timestamptz
GROUP BY c.dni, c.nombre, c.apellido/*Agrupamos para contar cuantas tiene el cliente*/
ORDER BY total_vendido DESC;


/*4) Top productos por ingresos (JOIN + SUM)*/
SELECT
  p.id_producto,
  p.marca,
  p.talle,
  COUNT(*) AS veces_vendido,
  SUM(v.monto) AS ingresos
FROM ventas v
JOIN productos p ON p.id_producto = v.id_producto
WHERE v.fecha >= '2026-02-01'::timestamptz
  AND v.fecha <  '2026-03-01'::timestamptz
GROUP BY p.id_producto, p.marca, p.talle
ORDER BY ingresos DESC;

/*5) Ventas por localidad (JOIN en cascada)*/
SELECT
  cp.localidad,
  COUNT(*) AS ventas,
  SUM(v.monto) AS total
FROM ventas v
JOIN clientes c ON c.dni = v.dni
LEFT JOIN codigos_postales cp ON cp.codigo_postal = c.codigo_postal
WHERE v.fecha >= '2026-02-01'::timestamptz
  AND v.fecha <  '2026-03-01'::timestamptz
GROUP BY cp.localidad
ORDER BY total DESC;

/*6) Clientes sin ventas en Febrero (LEFT JOIN)*/
SELECT
  c.dni,
  c.nombre || ' ' || c.apellido AS cliente
FROM clientes c
LEFT JOIN ventas v
  ON v.dni = c.dni
 AND v.fecha >= '2026-02-01'::timestamptz
 AND v.fecha <  '2026-03-01'::timestamptz
WHERE v.id_venta IS NULL
ORDER BY cliente;



SELECT c.*, cp.localidad
FROM clientes c
JOIN codigos_postales cp
  ON cp.codigo_postal = c.codigo_postal
WHERE cp.localidad = 'Santiago Centro';