import papermill as pm


pm.execute_notebook(
    './input.ipynb',
    './out/output.ipynb',
    parameters=dict(fecha_inicio='2021-01-01',fecha_fin='2021-05-07')
)
