from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Ruta donde se guardará el Excel
EXCEL_FILE = "registros.xlsx"

@app.route("/guardar", methods=["POST"])
def guardar():
    try:
        data = request.get_json()

        # Si no existe el archivo, se crea con encabezados
        if not os.path.exists(EXCEL_FILE):
            df = pd.DataFrame(columns=[
                "Fecha", "Documento", "Funcional", "Tiempo",
                "Responsable", "Cargo", "Firma", "Observaciones", "Firma2"
            ])
            df.to_excel(EXCEL_FILE, index=False)

        # Cargar Excel existente
        df = pd.read_excel(EXCEL_FILE)

        # Agregar nueva fila
        nueva_fila = pd.DataFrame([{
            "Fecha": data.get("fecha"),
            "Documento": data.get("documento"),
            "Funcional": data.get("funcional"),
            "Tiempo": data.get("tiempo"),
            "Responsable": data.get("responsable"),
            "Cargo": data.get("cargo"),
            "Firma": data.get("firma"),
            "Observaciones": data.get("observaciones"),
            "Firma2": data.get("firma2")
        }])

        df = pd.concat([df, nueva_fila], ignore_index=True)

        # Guardar de nuevo el Excel
        df.to_excel(EXCEL_FILE, index=False)

        return jsonify({"status": "success", "message": "Datos guardados correctamente en Excel"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
