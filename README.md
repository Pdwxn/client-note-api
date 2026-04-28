# Client Notes API

Backend de la aplicación Client Notes, una app tipo Notion enfocada en freelancers para gestionar clientes, proyectos y notas.

La API se encarga de la autenticación de usuarios, persistencia de datos y control de acceso a los recursos.

---

## 🧩 Features

- Autenticación de usuarios (JWT)
- CRUD completo de clientes
- CRUD completo de notas
- Relación entre entidades: `User → Client → Note`
- Filtrado y ordenamiento de resultados
- Aislamiento de datos por usuario

---

## 🏗️ Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT

---

## 🧠 Modelo de datos

- **User**
- **Client**
  - name, email, phone, company, tags
- **Note**
  - title, content, type (`idea`, `meeting`, `call`, `contract`)
  - relación con Client

---

## 🔐 Seguridad

- Autenticación basada en JWT
- Cada endpoint filtra por `request.user`
- Los usuarios solo pueden acceder a sus propios datos

Demo: https://client-notes-pink.vercel.app/

```python
def get_queryset(self):
    return Client.objects.filter(user=self.request.user)
