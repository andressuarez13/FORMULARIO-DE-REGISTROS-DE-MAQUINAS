import qrcode
import dearpygui.dearpygui as dpg

#ruta local
ruta_index = "zippy-beijinho-a14da6.netlify.app"

# --- Generar QR y guardarlo ---
img = qrcode.make("zippy-beijinho-a14da6.netlify.app")
img.save("qr_colores.png")

# --- Iniciar contexto DearPyGui ---
dpg.create_context()

# Registrar la textura (imagen QR)
with dpg.texture_registry():
    width, height, channels, data = dpg.load_image("qr_colores.png")
    qr_texture = dpg.add_static_texture(width, height, data)

# Ventana principal
with dpg.window(label="Visor QR", width=400, height=400):
    dpg.add_text("Código QR generado:")
    dpg.add_image(qr_texture)

#Configuración viewport ---
dpg.create_viewport(title="Generador de QR", width=350, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context() 