import json
import os

# Define la ruta del archivo JSON donde se guardarán los productos
# Es buena práctica definirla una vez para evitar errores de tipeo
RUTA_ARCHIVO_PRODUCTOS = 'productos.json'

def _cargar_productos():
    """
    Función interna para cargar los productos desde el archivo JSON.
    Si el archivo no existe o está vacío, devuelve una lista vacía.
    """
    if not os.path.exists(RUTA_ARCHIVO_PRODUCTOS) or os.path.getsize(RUTA_ARCHIVO_PRODUCTOS) == 0:
        # Si el archivo no existe o está vacío, inicializa con productos predeterminados o una lista vacía
        # Puedes decidir si quieres iniciar con productos predefinidos o siempre con una lista vacía.
        # Para esta implementación, si no hay archivo, empieza con una lista vacía.
        # Si quieres que inicie con los productos que tenías antes:
        # return [
        #     {"codigoProd": 123, "nombre": "Pan", "precio": 2000.00},
        #     {"codigoProd": 124, "nombre": "Leche", "precio": 1800.00},
        #     {"codigoProd": 125, "nombre": "Huevos", "precio": 4000.00},
        #     {"codigoProd": 126, "nombre": "Queso los 100g", "precio": 800.00},
        #     {"codigoProd": 127, "nombre": "Arroz", "precio": 2200.00},
        # ]
        return []
    try:
        with open(RUTA_ARCHIVO_PRODUCTOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Esto maneja el caso de que el JSON no sea válido (por ejemplo, corrupto)
        print(f"Advertencia: El archivo {RUTA_ARCHIVO_PRODUCTOS} está corrupto. Se iniciará con una lista vacía.")
        return []
    except Exception as e:
        print(f"Error al cargar productos: {e}. Se iniciará con una lista vacía.")
        return []

def _guardar_productos(productos):
    """
    Función interna para guardar la lista actual de productos en el archivo JSON.
    """
    with open(RUTA_ARCHIVO_PRODUCTOS, 'w', encoding='utf-8') as f:
        # indent=4 para que el JSON sea legible, ensure_ascii=False para caracteres especiales
        json.dump(productos, f, indent=4, ensure_ascii=False)

# Inicializar el archivo si no existe o está vacío con los productos de ejemplo
# Esto solo se ejecuta la primera vez que el script es importado o corrido
if not os.path.exists(RUTA_ARCHIVO_PRODUCTOS) or os.path.getsize(RUTA_ARCHIVO_PRODUCTOS) == 0:
    productos_iniciales = [
        {"codigoProd": 123, "nombre": "Pan", "precio": 2000.00},
        {"codigoProd": 124, "nombre": "Leche", "precio": 1800.00},
        {"codigoProd": 125, "nombre": "Huevos", "precio": 4000.00},
        {"codigoProd": 126, "nombre": "Queso los 100g", "precio": 800.00},
        {"codigoProd": 127, "nombre": "Arroz", "precio": 2200.00},
    ]
    _guardar_productos(productos_iniciales)


# --- Funciones públicas para interactuar con los productos ---

def obtener_todos_los_productos():
    """
    Devuelve la lista completa de productos.
    Otros módulos deben usar esta función para obtener los datos más recientes.
    """
    return _cargar_productos()

def agregar_producto(codigo, nombre, precio):
    """
    Agrega un nuevo producto a la lista y lo guarda.
    """
    productos_actuales = _cargar_productos()
    
    # Verificar si el código ya existe para evitar duplicados
    if any(str(p['codigoProd']) == str(codigo) for p in productos_actuales):
        # Es importante comparar como string si los códigos pueden ser numéricos o string
        return False, f"Error: El producto con código '{codigo}' ya existe."
    
    nuevo_producto = {
        "codigoProd": int(codigo), # Asegura que el código sea un entero
        "nombre": nombre,
        "precio": float(precio)    # Asegura que el precio sea un flotante
    }
    productos_actuales.append(nuevo_producto)
    _guardar_productos(productos_actuales)
    return True, f"Producto '{nombre}' agregado exitosamente."

def modificar_producto(codigo, nuevo_nombre=None, nuevo_precio=None):
    """
    Modifica un producto existente por su código y guarda los cambios.
    """
    productos_actuales = _cargar_productos()
    encontrado = False
    for producto in productos_actuales:
        if str(producto['codigoProd']) == str(codigo): # Comparar como string
            if nuevo_nombre is not None:
                producto['nombre'] = nuevo_nombre
            if nuevo_precio is not None:
                producto['precio'] = float(nuevo_precio)
            encontrado = True
            break
    
    if encontrado:
        _guardar_productos(productos_actuales)
        return True, f"Producto con código '{codigo}' modificado exitosamente."
    else:
        return False, f"Error: No se encontró ningún producto con el código '{codigo}'."

def eliminar_producto(codigo):
    """
    Elimina un producto por su código y guarda los cambios.
    """
    productos_actuales = _cargar_productos()
    productos_filtrados = [p for p in productos_actuales if str(p['codigoProd']) != str(codigo)] # Comparar como string
    
    if len(productos_filtrados) < len(productos_actuales):
        _guardar_productos(productos_filtrados)
        return True, f"Producto con código '{codigo}' eliminado exitosamente."
    else:
        return False, f"Error: No se encontró ningún producto con el código '{codigo}'."

def buscar_producto_por_codigo(codigo):
    """
    Busca y devuelve un producto por su código.
    """
    productos_actuales = _cargar_productos()
    for producto in productos_actuales:
        if str(producto['codigoProd']) == str(codigo): # Comparar como string
            return producto
    return None # Si no se encuentra el producto