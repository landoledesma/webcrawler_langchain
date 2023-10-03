**Web Information Retriever 🦜**

---

### Descripción:
Este proyecto permite a los usuarios ingresar una URL y realizar una consulta sobre el contenido de esa URL. Utiliza la API de OpenAI para obtener respuestas relacionadas con el contenido de la página web proporcionada.

---

### Instalación:

1. Clona este repositorio:
   ```
   git clone [dirección_del_repositorio]
   ```
   
2. Instala las dependencias necesarias:
   ```
   pip install streamlit openai pydantic
   ```

3. Asegúrate de tener un archivo `.env` que contenga tu `OPENAI_API_KEY`.

---

### Uso:

1. Ejecuta el archivo principal:
   ```
   streamlit run [nombre_del_archivo].py
   ```

2. Se abrirá una interfaz de usuario en tu navegador. Ingresa la URL del sitio web sobre el cual tienes una pregunta.

3. Ingresa tu pregunta relacionada con el contenido de esa URL.

4. Presiona el botón "Get answer" para obtener la respuesta.

---

### Funcionalidades:

- **Extracción de nombre de dominio:** Extrae y muestra el nombre del dominio de la URL ingresada para confirmación.

- **Interfaz intuitiva:** Despliega la pregunta y obtiene respuestas directamente en la interfaz.

- **Integración con OpenAI:** Utiliza la API de OpenAI para obtener respuestas relacionadas con el contenido de la página web proporcionada.

---

### Contribución:

Siéntete libre de hacer fork y enviar pull requests. Todas las contribuciones son bienvenidas.

---

### Licencia:

MIT
