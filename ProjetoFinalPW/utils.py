import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_grafico():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagem_png = buffer.getvalue()
    grafico = base64.b64encode(imagem_png)
    grafico = grafico.decode('utf-8')
    buffer.close()
    return grafico

def get_plot(primeira,segunda):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title('Média das Avaliações do Site')
    plt.plot(primeira, segunda)
    plt.xticks(rotation=45)
    plt.primeiralabel('Tema')
    plt.segundalabel('Cotação')
    plt.tight_layout()
    grafico = get_grafico()
    return grafico