# ESPECIFICACIÓN DE REQUERIMIENTOS DE SOFTWARE (SRS)
## Aplicación de Turnos Básica – MVC con API REST (.NET)

---

## 1. Introducción

### 1.1 Propósito
El presente documento describe los requerimientos funcionales y no funcionales de la Aplicación de Turnos Básica, desarrollada bajo el patrón de arquitectura MVC y con una API REST implementada en C# .NET. Este SRS servirá como base para el análisis, diseño, desarrollo y validación del sistema.

### 1.2 Alcance
La aplicación permitirá la gestión de turnos de atención mediante servicios REST, incluyendo el registro, consulta y actualización de turnos. La información será almacenada en una base de datos relacional.

### 1.3 Definiciones, acrónimos y abreviaturas
- **API**: Interfaz de Programación de Aplicaciones  
- **MVC**: Modelo Vista Controlador  
- **SRS**: Especificación de Requerimientos de Software  
- **REST**: Transferencia de Estado Representacional  

---

## 2. Descripción General

### 2.1 Perspectiva del producto
El sistema será una aplicación backend que expone una API REST desarrollada en C# .NET, la cual podrá ser consumida por una interfaz MVC o por aplicaciones cliente externas.

### 2.2 Funciones del producto
- Registrar turnos de atención
- Consultar turnos registrados
- Actualizar el estado de los turnos
- Persistir la información en base de datos

### 2.3 Características de los usuarios
- **Administrador**: gestiona los turnos y su estado
- **Operador**: consulta y atiende turnos

---

## 3. Requerimientos Específicos

### 3.1 Requerimientos Funcionales

**REQ-1**  
El sistema debe permitir registrar un nuevo **Turno** mediante la API REST, almacenando datos como número de turno, fecha, tipo de atención y estado inicial.

**REQ-2**  
El sistema debe permitir consultar la lista de **Turnos** registrados, mostrando su número, fecha, tipo de atención y **EstadoTurno**.

**REQ-3**  
El sistema debe permitir actualizar el **EstadoTurno** de un turno (Pendiente, Atendido o Cancelado) a través de un endpoint REST.

**REQ-4**  
El sistema debe permitir obtener la información de un **Turno** específico mediante su identificador único.

---

### 3.2 Requerimientos No Funcionales

**REQ-5**  
La API REST debe responder a las solicitudes en un tiempo máximo de 3 segundos bajo condiciones normales de operación.

**REQ-6**  
El sistema debe garantizar la persistencia de la información utilizando una base de datos relacional compatible con C# .NET, como SQL Server.

---

## 4. Restricciones

- El sistema debe ser desarrollado en lenguaje C# utilizando .NET.
- La arquitectura del sistema debe seguir el patrón MVC.
- La comunicación debe realizarse mediante servicios REST.

---

## 5. Suposiciones y Dependencias

- Se asume la disponibilidad de un servidor para la ejecución de la API.
- Se asume que los usuarios cuentan con acceso a red para consumir los servicios.

---

## 6. Aprobación

El presente documento es aprobado como base para el desarrollo de la Aplicación de Turnos Básica.

---
