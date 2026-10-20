# Sistema de Gestión de Citas - Barbería
## Fase 3: Desarrollo Backend y Frontend

### 📋 Descripción del Proyecto

Este proyecto es un sistema completo de gestión de citas para barbería desarrollado con Django. Incluye sistema de autenticación, operaciones CRUD para todas las entidades del sistema, y una interfaz moderna y responsive utilizando Bootstrap 5.

### 🚀 Cómo Ejecutar el Proyecto

1. **Activar el entorno virtual** (si se utiliza):
   ```bash
   venv\Scripts\activate
   ```

2. **Ejecutar el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

3. **Acceder a la aplicación**:
   - Abrir el navegador en: `http://127.0.0.1:8000`
   - Registrar un nuevo usuario en `/registro/`
   - Iniciar sesión con las credenciales creadas

### 📁 Estructura del Proyecto

```
Fase3/
├── barberia_project/          # Configuración del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Configuración principal
│   ├── urls.py               # URLs principales
│   └── wsgi.py
├── citas/                    # Aplicación principal
│   ├── __init__.py
│   ├── admin.py              # Configuración del admin
│   ├── migrations/           # Migraciones de la base de datos
│   ├── models.py             # Modelos de datos
│   ├── templates/            # Plantillas HTML
│   ├── urls.py               # URLs de la aplicación
│   └── views.py              # Vistas y lógica de negocio
├── static/                   # Archivos estáticos
│   └── css/
│       └── custom.css        # Estilos personalizados
├── db.sqlite3               # Base de datos SQLite
├── manage.py                # Script de gestión de Django
└── README.md                # Este archivo
```

### 🎯 Funcionalidades Implementadas

#### Autenticación
- ✅ Registro de usuarios con validación de contraseñas
- ✅ Login/Logout funcional
- ✅ Protección de rutas con decoradores
- ✅ Gestión de sesiones

#### CRUD Clientes
- ✅ Listar clientes con búsqueda
- ✅ Crear nuevo cliente
- ✅ Editar cliente existente
- ✅ Eliminar cliente con confirmación

#### CRUD Barberos
- ✅ Listar barberos con búsqueda
- ✅ Crear nuevo barbero
- ✅ Editar barbero existente
- ✅ Eliminar barbero con confirmación

#### CRUD Servicios
- ✅ Listar servicios con búsqueda
- ✅ Crear nuevo servicio
- ✅ Editar servicio existente
- ✅ Eliminar servicio con confirmación

#### CRUD Citas
- ✅ Listar citas con búsqueda
- ✅ Crear nueva cita
- ✅ Editar cita existente
- ✅ Eliminar cita con confirmación
- ✅ Gestión de estados (Pendiente, Completada, Cancelada)

### 🎨 Características de la Interfaz

- Diseño responsive con Bootstrap 5.3
- Navegación intuitiva con iconos
- Tablas con información clara y estilizada
- Formularios validados
- Mensajes de feedback para el usuario
- Iconos visuales de Bootstrap Icons
- Colores diferenciados por sección
- Dashboard con estadísticas en tiempo real

### 🔐 Seguridad

- Validación de contraseñas de Django
- Protección CSRF en formularios
- Rutas protegidas para usuarios autenticados
- Gestión segura de sesiones

### 📊 Estructura de Datos

**Modelos implementados:**
- **Cliente**: nombre, apellido, teléfono, correo
- **Barbero**: nombre, apellido, teléfono, especialidad
- **Servicio**: nombre, descripción, precio, duración
- **Cita**: cliente, barbero, servicio, fecha, hora, estado, observaciones
- **Horario**: barbero, día_semana, hora_inicio, hora_fin

### 🌐 URLs Principales

- `/` - Login
- `/registro/` - Registro de usuarios
- `/logout/` - Cerrar sesión
- `/home/` - Dashboard principal
- `/clientes/` - Gestión de clientes
- `/barberos/` - Gestión de barberos
- `/servicios/` - Gestión de servicios
- `/citas/` - Gestión de citas
- `/admin/` - Panel de administración de Django

### 🔧 Tecnologías Utilizadas

- **Backend**: Django 5.x
- **Frontend**: Bootstrap 5.3
- **Base de Datos**: SQLite (para desarrollo)
- **Autenticación**: Django Auth System
- **Iconos**: Bootstrap Icons 1.10.0
- **Estilos**: CSS personalizado + Bootstrap

### 📸 Guía para Capturas de Pantalla (Fase 3)

#### Autenticación
1. **Registro**: Acceder a `/registro/` y capturar el formulario de registro
2. **Login**: Capturar la página de login en `/`
3. **Dashboard**: Capturar la página principal después de iniciar sesión en `/home/`
4. **Logout**: Capturar la página de login después de cerrar sesión

#### CRUD Operaciones (ejemplo con Clientes)
1. **Crear**: Acceder a `/clientes/crear/` y capturar el formulario de creación
2. **Leer**: Capturar la lista de clientes en `/clientes/`
3. **Actualizar**: Editar un cliente y capturar el formulario de edición
4. **Eliminar**: Eliminar un cliente y capturar el diálogo de confirmación

#### Interfaz Gráfica
1. **Página principal**: Capturar el dashboard con estadísticas
2. **Plantillas Django**: Abrir cualquier archivo `.html` en `citas/templates/` y mostrar el código Django
3. **Bootstrap**: Capturar la navegación responsive o componentes de Bootstrap

#### Código
1. **Vista principal**: Abrir `citas/views.py` y capturar una función importante (como `home` o `cliente_list`)
2. **Estructura**: Capturar la estructura de carpetas del proyecto

### 🎯 Conclusión

El sistema completo de gestión de citas para barbería ha sido desarrollado exitosamente con todas las funcionalidades requeridas para la Fase 3. Se implementó un sistema robusto de autenticación, operaciones CRUD completas para todas las entidades del sistema, y una interfaz moderna y responsive utilizando Django Templates y Bootstrap 5.

El proyecto sigue las mejores prácticas de desarrollo web con Django, incluyendo separación de responsabilidades, seguridad en la autenticación, y una experiencia de usuario intuitiva.