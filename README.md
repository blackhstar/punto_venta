# Sistema de Punto de Venta (POS)

Un sistema completo de punto de venta desarrollado en Python con interfaz gráfica usando Tkinter.

## Características

- **Dashboard**: Vista general del sistema
- **Ventas**: Gestión de ventas y transacciones
- **Clientes**: Administración de clientes
- **Inventario**: Control de stock y productos
- **Reportes**: Generación de reportes y estadísticas

## Requisitos

- Python 3.8 o superior
- Pillow (PIL) para manejo de imágenes
- Tkinter (incluido con Python)

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/pos-system.git
cd pos-system
```

2. Instala las dependencias:
```bash
pip install Pillow
```

3. Ejecuta la aplicación:
```bash
python main.py
```

## Estructura del Proyecto

```
POS/
├── main.py          # Archivo principal
├── container.py     # Contenedor principal de la interfaz
├── dashboard.py     # Módulo del dashboard
├── ventas.py        # Módulo de ventas
├── clientes.py      # Módulo de clientes
├── inventario.py    # Módulo de inventario
├── reportes.py      # Módulo de reportes
├── login.py         # Módulo de autenticación
├── DBPOS.db         # Base de datos SQLite
└── src/
    └── img/         # Imágenes del proyecto
```

## Uso

1. Ejecuta `main.py` para iniciar la aplicación
2. Navega entre las diferentes secciones usando el menú lateral
3. Utiliza las funcionalidades específicas de cada módulo

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Versión

Versión actual: 1.0 