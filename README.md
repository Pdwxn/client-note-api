# Client Notes API

Client Notes API es el backend que alimenta la aplicación Client Notes. Se encarga de guardar, procesar y proteger todos los datos de clientes y notas de los usuarios.

## Qué hace la API

### Autenticación de usuarios
La API gestiona el registro de nuevos usuarios y su inicio de sesión. Cada usuario tiene su propia cuenta protegida con contraseña. Cuando inicias sesión, la API genera tokens de acceso que la app usa para identificarte en cada solicitud, sin necesidad de volver a escribir tu contraseña.

### Gestión de clientes
Cuando creas, editas o eliminas un cliente desde la app, la API procesa esa solicitud y guarda los cambios en la base de datos. Cada cliente está vinculado al usuario que lo creó, así que solo tú puedes ver y modificar tus clientes.

### Gestión de notas
Igual que con los clientes, la API guarda todas las notas que creas para cada cliente. Cada nota tiene un tipo (idea, reunión, llamada o contrato) y guarda el título y contenido que escribes. Solo tú puedes ver las notas de tus clientes.

### Seguridad
La API verifica en cada solicitud que estés autenticado y que tengas permiso para acceder a esos datos. Si no tienes sesión activa, rechaza la solicitud. Los datos de cada usuario están completamente aislados de los demás.

## Cómo funciona

La API está construida con Django REST Framework y usa una base de datos PostgreSQL o SQLite para guardar toda la información. Corre en un servidor y responde a las peticiones del frontend en formato JSON.