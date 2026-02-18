https://www.mysql.com/downloads/

1) MySQL en Windows (server + Workbench)

Necesitas:

    * MySQL Server (el motor de BD)
    * MySQL Workbench (para ver tablas, hacer queries, modelar)

Pasos típicos:

1.- Instala MySQL Installer for Windows (incluye Server + Workbench).
2.- Durante la instalación:

    * Define password para root.
    * Deja el puerto 3306 (por defecto).
    * Habilita que corra como Windows Service (arranque automático).

3.- Verifica que está corriendo:
    
    * Abre Services (Servicios) y revisa MySQL80 (o similar) → “Running”.

4.- Prueba desde consola (si agregaste a PATH):

    * mysql --version
    * mysql -u root -p

GUI recomendada: MySQL Workbench (o DBeaver si quieres uno para todo).