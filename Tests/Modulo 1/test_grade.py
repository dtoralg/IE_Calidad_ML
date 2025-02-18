import nbformat
import papermill as pm

def test_ejercicio():
    notebook_filename = "ejercicio.ipynb"
    output_filename = "output.ipynb"
    
    # Ejecuta el notebook y genera el output
    pm.execute_notebook(notebook_filename, output_filename)
    
    # Abre el notebook de salida
    with open(output_filename) as f:
        nb = nbformat.read(f, as_version=4)
    
    # Busca en las celdas una salida esperada
    found = False
    for cell in nb.cells:
        # Comprueba si la celda tiene salidas y si alguna contiene el texto esperado
        for output in cell.get("outputs", []):
            if "La clave común 'cliente_id' fue encontrada" in output.get("text", ""):
                found = True
                break
        if found:
            break

    assert found, "No se encontró la salida esperada sobre la clave común en el notebook."
