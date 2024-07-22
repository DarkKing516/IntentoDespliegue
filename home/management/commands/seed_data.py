from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Cargar datos iniciales en la base de datos'

    def handle(self, *args, **kwargs):
        # SQL para eliminar todos los datos de las tablas
        sql_delete_roles = "DELETE FROM roles;"
        sql_delete_permisos = "DELETE FROM permisos;"
        sql_delete_roles_permisos = "DELETE FROM roles_permisos;"
        sql_delete_usuarios = "DELETE FROM usuarios;"

        # SQL para ajustar el tipo de columnas
        sql_alter_producto = """
        ALTER TABLE productos
        ALTER COLUMN estado_producto TYPE CHAR(1) USING estado_producto::CHAR(1),
        ALTER COLUMN estado_catalogo TYPE CHAR(1) USING estado_catalogo::CHAR(1);
        ALTER TABLE servicios
        ALTER COLUMN estado_servicio TYPE CHAR(1) USING estado_servicio::CHAR(1),
        ALTER COLUMN estado_catalogo TYPE CHAR(1) USING estado_catalogo::CHAR(1);
        """

        # SQL para insertar roles
        sql_roles = """
        INSERT INTO roles (id, nombre_rol, estado_rol) VALUES
        (1, 'Admin', 'A'),
        (2, 'Cliente', 'A'),
        (3, 'Moderador', 'I'),
        (4, 'Analista', 'A');
        """

        # SQL para insertar permisos
        sql_permisos = """
        INSERT INTO permisos (id, nombre_permiso, estado_permiso) VALUES
        (1, 'Listar Usuarios', 'A'),
        (2, 'Crear Usuarios', 'A'),
        (3, 'Editar Usuarios', 'A'),
        (4, 'Editar Rol Usuarios', 'A'),
        (5, 'Editar Estado Usuarios', 'A'),
        (6, 'Editar Perfil', 'A'),
        (7, 'Eliminar Usuarios', 'A'),
        (8, 'Listar Roles', 'A'),
        (9, 'Crear Roles', 'A'),
        (10, 'Editar Roles', 'A'),
        (11, 'Editar Estado Roles', 'A'),
        (12, 'Eliminar Roles', 'A'),
        (13, 'Listar Permisos', 'A'),
        (14, 'Editar Permisos', 'I'),
        (15, 'Editar Estado Permisos', 'A'),
        (16, 'Listar Productos', 'A'),
        (17, 'Crear Productos', 'A'),
        (18, 'Editar Productos', 'A'),
        (19, 'Eliminar Productos', 'A'),
        (20, 'Listar Tipo Productos', 'A'),
        (21, 'Crear Tipo Productos', 'A'),
        (22, 'Editar Tipo Productos', 'A'),
        (23, 'Eliminar Tipo Productos', 'A'),
        (24, 'Listar Servicios', 'A'),
        (25, 'Crear Servicios', 'A'),
        (26, 'Editar Servicios', 'A'),
        (27, 'Eliminar Servicios', 'A'),
        (28, 'Listar Tipo Servicios', 'A'),
        (29, 'Crear Tipo Servicios', 'A'),
        (30, 'Editar Tipo Servicios', 'A'),
        (31, 'Eliminar Tipo Servicios', 'A'),
        (32, 'Listar Pedidos', 'A'),
        (33, 'Listar Mis Pedidos', 'A'),
        (34, 'Crear Pedidos', 'A'),
        (35, 'Editar Pedidos', 'A'),
        (36, 'Editar Mis Pedidos', 'A'),
        (37, 'Eliminar Pedidos', 'A'),
        (38, 'Listar Reservas', 'A'),
        (39, 'Listar Mis Reservas', 'A'),
        (40, 'Crear Reservas', 'A'),
        (41, 'Editar Reservas', 'A'),
        (42, 'Editar Mis Reservas', 'A'),
        (43, 'Eliminar Reservas', 'A'),
        (44, 'Listar Ventas', 'A'),
        (45, 'Crear Ventas', 'A'),
        (46, 'Listar Mis Ventas', 'A'),
        (47, 'Crear Permisos', 'A'),
        (48, 'Eliminar Permisos', 'I'),
        (49, 'Editar Estado Pedidos', 'A'),
        (50, 'Editar Evidencia Pedidos', 'A'),
        (51, 'Editar Estado Tipo Productos', 'A'),
        (52, 'Editar Estado Productos', 'A'),
        (53, 'Editar Estado Catalogo Productos', 'A'),
        (54, 'Cambiar Imagen Productos', 'A'),
        (55, 'Cambiar Imagen Servicios', 'A'),
        (56, 'Editar Estado Servicio Catalogo', 'A'),
        (57, 'Editar Estado Servicio', 'A'),
        (58, 'Editar Estado Tipo Servicios', 'A');
        """

        # SQL para insertar roles_permisos
        sql_roles_permisos = """
        INSERT INTO roles_permisos (id, rol_id, permiso_id) VALUES
        (1, 1, 1),
        (2, 1, 2),
        (3, 1, 3),
        (4, 1, 4),
        (5, 1, 5),
        (6, 1, 6),
        (7, 1, 7),
        (8, 1, 8),
        (9, 1, 9),
        (10, 1, 10),
        (11, 1, 11),
        (12, 1, 12),
        (13, 1, 13),
        (16, 1, 16),
        (17, 1, 17),
        (18, 1, 18),
        (19, 1, 19),
        (20, 1, 20),
        (21, 1, 21),
        (22, 1, 22),
        (23, 1, 23),
        (24, 1, 24),
        (25, 1, 25),
        (26, 1, 26),
        (27, 1, 27),
        (28, 1, 28),
        (29, 1, 29),
        (30, 1, 30),
        (31, 1, 31),
        (32, 1, 32),
        (33, 1, 33),
        (34, 1, 34),
        (35, 1, 35),
        (36, 1, 36),
        (38, 1, 38),
        (39, 1, 39),
        (40, 1, 40),
        (41, 1, 41),
        (42, 1, 42),
        (43, 1, 43),
        (44, 1, 44),
        (45, 1, 45),
        (46, 1, 46),
        (134, 1, 49),
        (135, 1, 50),
        (136, 1, 51),
        (137, 1, 52),
        (138, 1, 53),
        (139, 1, 54),
        (140, 1, 55),
        (141, 1, 56),
        (142, 1, 57),
        (64, 2, 6),
        (68, 2, 33),
        (69, 2, 36),
        (70, 2, 39),
        (71, 2, 42),
        (72, 2, 46),
        (151, 4, 1),
        (152, 4, 2),
        (153, 4, 3),
        (154, 4, 4),
        (155, 4, 5),
        (196, 4, 6),
        (156, 4, 7),
        (82, 4, 8),
        (85, 4, 9),
        (86, 4, 10),
        (200, 4, 11),
        (201, 4, 12),
        (183, 4, 13),
        (185, 4, 15),
        (157, 4, 16),
        (158, 4, 17),
        (159, 4, 18),
        (160, 4, 19),
        (164, 4, 20),
        (166, 4, 21),
        (167, 4, 22),
        (168, 4, 23),
        (169, 4, 24),
        (172, 4, 25),
        (173, 4, 26),
        (174, 4, 27),
        (176, 4, 28),
        (180, 4, 29),
        (181, 4, 30),
        (182, 4, 31),
        (187, 4, 32),
        (188, 4, 33),
        (189, 4, 34),
        (190, 4, 35),
        (191, 4, 36),
        (192, 4, 37),
        (195, 4, 38),
        (197, 4, 39),
        (198, 4, 40),
        (199, 4, 41),
        (202, 4, 42),
        (203, 4, 43),
        (204, 4, 44),
        (205, 4, 45),
        (206, 4, 46),
        (184, 4, 47),
        (193, 4, 49),
        (194, 4, 50),
        (165, 4, 51),
        (163, 4, 52),
        (161, 4, 53),
        (162, 4, 54),
        (170, 4, 55),
        (171, 4, 56),
        (175, 4, 57),
        (186, 4, 58);
        """

        # SQL para insertar usuario admin
        # sql_usuario_admin = """
        # INSERT INTO usuarios VALUES
        # (1, 'ADMINISTRADOR', '1234', '5678', 'jhomai7020@gmail.com', 'Admin muy serio', 'pbkdf2_sha256$720000$6Ss3QHdg69DbXGaFcM7VwZ$A6OVIj5bW3zYIHcNv3aRv7pvBPNwqJdrN7cOxUzDV/0=', 'A', 1, 'user_images/iconosesion.jpg');
        # """
        sql_usuario_admin = """
        """



        # Añade esta línea en tu método handle
        with connection.cursor() as cursor:
            cursor.execute(sql_alter_producto)  # Ajusta el tipo de columnas

            # cursor.execute(sql_delete_roles_permisos)
            # cursor.execute(sql_delete_roles)
            # cursor.execute(sql_delete_permisos)
            # cursor.execute(sql_delete_usuarios)
        
            # cursor.execute(sql_roles)
            # cursor.execute(sql_permisos)
            # cursor.execute(sql_roles_permisos)
            # cursor.execute(sql_usuario_admin)  # Ejecuta la inserción del usuario admin

            
        self.stdout.write(self.style.SUCCESS('Datos iniciales cargados exitosamente.'))
