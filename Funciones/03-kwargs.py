def get_product(**datos):
    # para acceder al parametro del argumento es necesaio poner el nombre del argumento en []
    print(datos["name"], datos["id"])


get_product(id="40",
            name="iphone",
            desc="Esto es un celular")
