import subprocess
import json

def describe_image_with_llava(image_path):
    """
    Descreve uma imagem usando o modelo LLava do Ollama.

    Args:
        image_path (str): Caminho para a imagem a ser descrita.

    Returns:
        str: Descrição gerada pelo modelo LLava.
    """
    try:
        # Comando para descrever a imagem usando o Ollama
        command = [
            "ollama", "run", "llava",
            f"--image={image_path}"
        ]

        # Executando o comando e capturando a saída
        result = subprocess.run(command, capture_output=True, text=True)

        # Verificando se o comando foi executado com sucesso
        if result.returncode != 0:
            raise Exception(f"Erro ao executar o Ollama: {result.stderr}")

        # Parse da resposta JSON
        output = json.loads(result.stdout)
        description = output.get('description', 'Nenhuma descrição gerada.')

        return description

    except Exception as e:
        return f"Erro ao descrever a imagem: {str(e)}"

# Exemplo de uso
image_path = "caminho/para/sua/imagem.jpg"
descricao = describe_image_with_llava(image_path)
print(f"Descrição da imagem: {descricao}")
