import os
import subprocess
import time

def run_tests(test_directory, solution_file):
    test_files = [file for file in os.listdir(test_directory) if file.endswith('.txt')]

    for test_file in test_files:
        input_path = os.path.join(test_directory, test_file)
        output_path = os.path.join(test_directory, test_file.replace('.txt', '.out'))

        # Comando para executar a solução
        command = f"time python3 {solution_file} < {input_path}"
        
        # Executa a solução e captura a saída
        start_time = time.time()
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        end_time = time.time()

        # Calcula o tempo de execução em milissegundos
        execution_time_ms = (end_time - start_time)

        # Lê a solução esperada do arquivo de saída
        with open(output_path, 'r') as f:
            expected_output = f.read().strip()

        # Compara a saída gerada com a solução esperada
        if result.stdout.strip() == expected_output:
            result_message = "Passou"
        else:
            result_message = "Falhou"

        # Imprime o resultado do teste, o tempo de execução e se passou ou falhou
        print(f"Teste: {test_file}, Resultado: {result_message}, Tempo de execução: {execution_time_ms:.2f} ms")

if __name__ == "__main__":
    # Diretório onde os testes estão localizados
    test_directory = "tests"

    # Caminho para o arquivo da solução
    solution_file = "pipe2.py"

    run_tests(test_directory, solution_file)
