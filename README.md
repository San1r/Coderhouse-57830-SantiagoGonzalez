# Coderhouse-57830-SantiagoGonzalez

# Blog Santiago Gonzalez 57830

## Instalación

1. **Instalar el entorno virtual**:
    ```bash
    python -m venv env
    ```
   Para activar el entorno virtual:
    - En Windows:
      ```bash
      .\env\Scripts\activate
      ```
    - En macOS y Linux:
      ```bash
      source env/bin/activate
      ```

2. **Instalar Django**:
    ```bash
    pip install django
    ```

3. **Instalar Pillow**:
    ```bash
    pip install pillow
    ```
    **Nota:** Pillow se utiliza para manejar las imágenes en el proyecto, como la carga de imágenes en posts.

4. **Configurar la base de datos**:
    - Crea la base de datos con el comando:
      ```bash
      python manage.py migrate
      ```

5. **Crear un superusuario**:
    Para gestionar las imágenes de perfil y otros aspectos administrativos, debes crear un superusuario:
    ```bash
    python manage.py createsuperuser
    ```

6. **Ejecutar el servidor de desarrollo**:
    ```bash
    python manage.py runserver
    ```

## Funcionalidades del Sitio

- **Página de Inicio**: Muestra una lista de posts ordenados por fecha de publicación.
- **Crear Post**: Los usuarios autenticados pueden crear nuevos posts.
- **Ver Post**: Visualiza el contenido completo de un post y sus comentarios.
- **Comentar en Posts**: Los usuarios autenticados pueden dejar comentarios en los posts.
- **Editar Posts**: Los usuarios que crearon el post pueden editarlo.
- **Subir Imágenes**: Los usuarios pueden subir imágenes para sus posts.
- **Buscar Posts**: Utiliza un formulario de búsqueda para filtrar posts por fecha y autor.
- **Registro de Usuarios**: Los usuarios pueden registrarse y acceder al sitio.
- **Imagen de Perfil**: Los usuarios pueden gestionar su imagen de perfil a través del panel de administración.

## Gestión de Imágenes de Perfil

- Para gestionar la imagen de perfil, debes hacerlo a través del panel de administración utilizando el superusuario creado.

## Permisos de los Usuarios Registrados

- **Pueden:**
  - Crear, editar y eliminar sus propios posts.
  - Agregar comentarios a los posts.
  - Ver posts y comentarios.
  - Modificar su propia imagen de perfil desde el panel de administración.

- **No pueden:**
  - Crear o editar posts de otros usuarios.
  - Eliminar comentarios de otros usuarios.
  - Modificar la imagen de perfil de otros usuarios.

## Permisos de los Usuarios No Registrados

- **Pueden:**
  - Ver posts y comentarios.

- **No pueden:**
  - Crear, editar o eliminar posts.
  - Comentar en posts.
  - Modificar o gestionar imágenes de perfil.
  - Acceder a funciones administrativas o de gestión de contenido.

