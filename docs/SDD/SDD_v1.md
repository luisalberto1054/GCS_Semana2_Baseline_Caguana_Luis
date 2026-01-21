# DESCRIPCIÓN DEL DISEÑO DE SOFTWARE (SDD)
## Aplicación de Turnos Básica – MVC con API REST (.NET)

---

## 1. Introducción

### 1.1 Propósito
El presente documento describe el diseño de la Aplicación de Turnos Básica, especificando la arquitectura, los componentes principales y las decisiones técnicas adoptadas. El SDD sirve como guía para la implementación del sistema conforme a los requerimientos definidos en el SRS.

### 1.2 Alcance
El diseño cubre el backend del sistema, desarrollado en C# .NET, que expone una API REST y gestiona la persistencia de datos mediante una base de datos relacional.

---

## 2. Arquitectura del Sistema

### 2.1 Estilo Arquitectónico
El sistema utiliza una arquitectura **MVC (Modelo – Vista – Controlador)**, separando claramente las responsabilidades:

- **Modelo**: Representa las entidades del negocio y el acceso a datos.
- **Controlador**: Gestiona las solicitudes HTTP y la lógica de la API REST.
- **Vista**: Puede ser una interfaz MVC o aplicaciones cliente que consuman la API.

### 2.2 Diagrama de Arquitectura (Conceptual)

Cliente → Controlador (API REST) → Servicio → Repositorio → Base de Datos

---

## 3. Componentes del Sistema

### 3.1 Controladores
Encargados de exponer los endpoints REST y recibir las solicitudes del cliente.

- `TurnosControlador`
  - RegistrarTurno()
  - ObtenerTurnos()
  - ObtenerTurnoPorId()
  - ActualizarEstadoTurno()

### 3.2 Servicios
Contienen la lógica de negocio del sistema.

- `TurnoServicio`
  - ValidarTurno()
  - CambiarEstadoTurno()
  - ListarTurnos()

### 3.3 Modelos
Representan las entidades del dominio.

- `Turno`
  - IdTurno
  - NumeroTurno
  - FechaRegistro
  - TipoAtencion
  - EstadoTurno

- `Usuario`
  - IdUsuario
  - NombreUsuario
  - Rol

### 3.4 Repositorios
Gestionan el acceso a la base de datos.

- `TurnoRepositorio`
  - GuardarTurno()
  - ObtenerTurnos()
  - ObtenerTurnoPorId()
  - ActualizarTurno()

---

## 4. Diseño de la Base de Datos

### 4.1 Entidad Turno
Tabla: **Turnos**

- IdTurno (int, PK)
- NumeroTurno (varchar)
- FechaRegistro (datetime)
- TipoAtencion (varchar)
- EstadoTurno (varchar)

### 4.2 Entidad Usuario
Tabla: **Usuarios**

- IdUsuario (int, PK)
- NombreUsuario (varchar)
- Rol (varchar)

---

## 5. Decisiones Técnicas

- El lenguaje de desarrollo será **C# con .NET**.
- Se utilizará **API REST** para la comunicación entre cliente y servidor.
- La persistencia de datos se realizará mediante una **base de datos relacional (SQL Server)**.
- Se adopta el patrón **Repositorio** para desacoplar la lógica de negocio del acceso a datos.
- Los nombres de clases, métodos y variables se definen en **español** para mantener coherencia con la documentación.

---

## 6. Consideraciones de Seguridad y Rendimiento

- Validación de datos en los controladores y servicios.
- Manejo de excepciones para evitar exposición de errores internos.
- Respuestas eficientes para cumplir con los tiempos establecidos en los requerimientos no funcionales.

---

## 7. Aprobación

El presente documento de diseño es aprobado como base para la implementación de la Aplicación de Turnos Básica.

---
