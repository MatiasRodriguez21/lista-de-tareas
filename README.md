# 📝 Lista de Tareas con Interfaz Gráfica

¡Bienvenido a tu gestor de tareas! Este proyecto es una aplicación de escritorio sencilla hecha en Python, que permite organizar tus actividades diarias a través de una interfaz gráfica amigable.

## 🚀 Características
- **Agregar tareas** con nombre, categoría y fecha límite.
- **Marcar tareas como completadas** y desmarcarlas si es necesario.
- **Guardar y cargar tareas** automáticamente en un archivo `tasks.json`.
- Interfaz personalizable con íconos y colores amigables.

## 🛠 Tecnologías utilizadas
- **Python 3.x**
- **Tkinter** para la interfaz gráfica
- **Pillow** para manejo de imágenes
- **ttkthemes** para temas visuales
- **JSON** para almacenamiento de datos

## 📂 Estructura del Proyecto
```
LISTA_TAREAS/
├── .venv/                # Entorno virtual (ignorado en Git)
├── logos/                # Íconos de la UI
│   ├── add_icon.png
│   ├── complete_icon.png
│   ├── delete_icon.png
│   ├── save_icon.png
│   ├── uncomplete_icon.png
├── .gitignore            # Archivos y carpetas a ignorar por Git
├── main.py               # Código principal de la aplicación
├── tasks.json            # Almacenamiento de las tareas
```

## 📥 Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/lista_tareas.git
   cd lista_tareas
   ```
2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv .venv
   # Activar en Windows
   .venv\Scripts\activate
   # Activar en Mac/Linux
   source .venv/bin/activate
   ```
3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Uso
Ejecuta el programa con:
```bash
python main.py
```

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas! Puedes abrir un issue para sugerencias o enviar un pull request con mejoras.

## 📜 Licencia
Este proyecto está bajo la Licencia MIT. ¡Usa, modifica y distribuye libremente!

---

¿Qué te parece? ¿Algo que quieras ajustar o agregar? ¡Lo afinamos juntos! 🚀😊

