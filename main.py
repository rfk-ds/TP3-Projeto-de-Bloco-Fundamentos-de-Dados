import sqlite3
import csv

def conectar():
    return sqlite3.connect("banco_de_dados_tp.db")

def criar_tabelas(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cargos (
        id_cargo INTEGER PRIMARY KEY,
        nome_cargo TEXT NOT NULL,
        descricao_cargo TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Departamentos (
        id_departamento INTEGER PRIMARY KEY,
        nome_departamento TEXT NOT NULL,
        email_departamento TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Funcionarios (
        id_funcionario INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        data_admissao TEXT NOT NULL,
        id_cargo INTEGER,
        id_departamento INTEGER,
        salario_base REAL,
        FOREIGN KEY (id_cargo) REFERENCES Cargos (id_cargo),
        FOREIGN KEY (id_departamento) REFERENCES Departamentos (id_departamento)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS HistoricoSalarios (
        id_historico INTEGER PRIMARY KEY,
        id_funcionario INTEGER,
        mes_ano TEXT NOT NULL,
        salario REAL NOT NULL,
        FOREIGN KEY (id_funcionario) REFERENCES Funcionarios (id_funcionario)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Dependentes (
        id_dependente INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        sexo TEXT NOT NULL,
        id_funcionario INTEGER,
        FOREIGN KEY (id_funcionario) REFERENCES Funcionarios (id_funcionario)
    );
    """)
    
def limpar_tabelas(cursor):
    cursor.execute("DELETE FROM Dependentes;")
    cursor.execute("DELETE FROM HistoricoSalarios;")
    cursor.execute("DELETE FROM Funcionarios;")
    cursor.execute("DELETE FROM Departamentos;")
    cursor.execute("DELETE FROM Cargos;")


def inserir_dados_csv(cursor):
    cargos = ler_csv('cargos.csv')
    departamentos = ler_csv('departamentos.csv')
    funcionarios = ler_csv('funcionarios.csv')
    historico_salarios = ler_csv('historico_salarios.csv')
    dependentes = ler_csv('dependentes.csv')

    cursor.executemany("""
        INSERT INTO Cargos (nome_cargo, descricao_cargo)
        VALUES (?, ?)
    """, cargos)

    cursor.executemany("""
        INSERT INTO Departamentos (nome_departamento, email_departamento)
        VALUES (?, ?)
    """, departamentos)

    cursor.executemany("""
        INSERT INTO Funcionarios (nome, data_admissao, id_cargo, id_departamento, salario_base)
        VALUES (?, ?, ?, ?, ?)
    """, funcionarios)

    cursor.executemany("""
        INSERT INTO HistoricoSalarios (id_funcionario, mes_ano, salario)
        VALUES (?, ?, ?)
    """, historico_salarios)

    cursor.executemany("""
        INSERT INTO Dependentes (nome, data_nascimento, sexo, id_funcionario)
        VALUES (?, ?, ?, ?)
    """, dependentes)

def criar_csvs():
    print("Criando arquivos CSV...")

    cargos = [
        ['Desenvolvedor', 'Desenvolve e mantém sistemas'],
        ['Gerente', 'Gerencia equipes e projetos'],
        ['Analista', 'Analisa processos e propõe melhorias'],
        ['Designer', 'Cria designs e interfaces'],
        ['Suporte Técnico', 'Resolve problemas de TI e suporte'],
        ['Estagiário', 'Auxilia nas atividades diárias']
    ]
    
    departamentos = [
        ['TI', 'ti@empresa.com'],
        ['Recursos Humanos', 'rh@empresa.com'],
        ['Marketing', 'marketing@empresa.com'],
        ['Vendas', 'vendas@empresa.com'],
        ['Financeiro', 'financeiro@empresa.com']
    ]
    
    funcionarios = [
        ['João Silva', '2023-01-15', 1, 1, 5000.0],
        ['Maria Oliveira', '2023-02-20', 2, 2, 6000.0],
        ['Pedro Souza', '2022-11-05', 3, 3, 6300.0],
        ['Ana Costa', '2021-07-13', 4, 4, 7000.0],
        ['Luiz Pereira', '2020-08-21', 5, 5, 3000.0],
        ['Carlos Nunes', '2023-03-10', 6, 6, 1500.0],
        ['Alice Oliveira', '2023-04-25', 5, 7, 6500.0],
        ['Bruno Santos', '2023-05-30', 3, 8, 6700.0],
        ['Carla Dias', '2023-06-05', 1, 9, 5200.0],
        ['Nicolas lima', '2023-07-10', 2, 10, 6000.0]  
    ]
    
    historico_salarios = [
        [1, '2023-09', 5000.0], [1, '2023-08', 4800.0], [1, '2023-07', 4600.0],
        [2, '2023-09', 6000.0], [2, '2023-08', 6000.0], [2, '2023-07', 5800.0],
        [3, '2023-09', 6300.0], [3, '2023-08', 6300.0], [3, '2023-07', 6300.0],
        [4, '2023-09', 8000.0], [4, '2023-08', 7900.0], [4, '2023-07', 7800.0],
        [5, '2023-09', 3000.0], [5, '2023-08', 3000.0], [5, '2023-07', 3000.0],
        [6, '2023-09', 1500.0], [6, '2023-08', 1500.0], [6, '2023-07', 1500.0],
        [7, '2023-09', 6500.0], [7, '2023-08', 6500.0], [7, '2023-07', 6500.0],
        [8, '2023-09', 6700.0], [8, '2023-08', 6700.0], [8, '2023-07', 6700.0],
        [9, '2023-09', 5200.0], [9, '2023-08', 5200.0], [9, '2023-07', 5200.0],
        [10, '2023-09', 6000.0], [10, '2023-08', 6000.0], [10, '2023-07', 6000.0]
    ]
    
    dependentes = [
        ['Filho João', '2015-05-10', 'M', 1],
        ['Filha Maria', '2017-09-23', 'F', 1],
        ['Filho Pedro', '2016-12-01', 'M', 2],
        ['Filha Ana', '2019-03-14', 'F', 2],
        ['Filha Sofia', '2018-11-12', 'F', 3],
        ['Filho Miguel', '2019-06-15', 'M', 4],
        ['Filha Clara', '2020-02-10', 'F', 3],
        ['Filha Gabriela', '2022-09-23', 'F', 4],
        ['Filho Lucas', '2021-11-15', 'M', 5],  
        ['Filha Laura', '2022-05-01', 'F', 6]
    ]

    criar_csv('cargos.csv', ['nome_cargo', 'descricao_cargo'], cargos)
    criar_csv('departamentos.csv', ['nome_departamento', 'email_departamento'], departamentos)
    criar_csv('funcionarios.csv', ['nome', 'data_admissao', 'id_cargo', 'id_departamento', 'salario_base'], funcionarios)
    criar_csv('historico_salarios.csv', ['id_funcionario', 'mes_ano', 'salario'], historico_salarios)
    criar_csv('dependentes.csv', ['nome', 'data_nascimento', 'sexo', 'id_funcionario'], dependentes)

def criar_csv(nome_arquivo, cabecalho, dados):
    print(f"Criando arquivo {nome_arquivo}...")
    with open(nome_arquivo, mode='w', encoding='utf-8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(cabecalho)
        escritor.writerows(dados)
    print(f"{nome_arquivo} criado com sucesso!\n")


def ler_csv(nome_arquivo):
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        return [linha for linha in leitor if linha]

# 1. Listar individualmente as tabelas de: Funcionários, Cargos, Departamentos, Histórico de Salários e Dependentes em ordem crescente. # QUINTA CONSULTA PYTHON
def listar_tabelas(cursor):
    tabelas = ['Funcionarios', 'Cargos', 'Departamentos', 'HistoricoSalarios', 'Dependentes']
    for tabela in tabelas:
        cursor.execute(f"SELECT * FROM {tabela} ORDER BY 1")
        resultados = cursor.fetchall()
        print(f"\n-----Tabela: {tabela}-----\n")
        for linha in resultados:
            print(linha)
print("\n")

# 2. Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes.
def listar_funcionarios_com_dependentes(cursor):
    cursor.execute("""
    SELECT f.nome, c.nome_cargo, d.nome_departamento, 
           GROUP_CONCAT(dep.nome) AS dependentes
    FROM Funcionarios f
    JOIN Cargos c ON f.id_cargo = c.id_cargo
    JOIN Departamentos d ON f.id_departamento = d.id_departamento
    LEFT JOIN Dependentes dep ON f.id_funcionario = dep.id_funcionario
    GROUP BY f.id_funcionario
    ORDER BY f.nome;
    """)
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)
print("\n")

# 3. Listar os funcionários que tiveram aumento salarial nos últimos 3 meses.
def listar_funcionarios_aumento(cursor):
    cursor.execute("""
    SELECT f.nome, hs2.salario AS salario_atual
    FROM HistoricoSalarios hs1
    JOIN HistoricoSalarios hs2 ON hs1.id_funcionario = hs2.id_funcionario 
    AND hs1.mes_ano < hs2.mes_ano
    JOIN Funcionarios f ON f.id_funcionario = hs1.id_funcionario
    WHERE hs2.salario > hs1.salario 
    AND hs1.mes_ano >= '2023-07'
    AND hs2.mes_ano <= '2023-09'  -- Altere para a data final que você precisa
    GROUP BY f.nome, hs2.salario
    ORDER BY f.nome;
    """)
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)
print("\n")


# 4. Listar a média de salário por departamento em ordem decrescente.
def media_salario_por_departamento(cursor):
    cursor.execute("""
    SELECT d.nome_departamento, AVG(f.salario_base) AS media_salario
    FROM Departamentos d
    JOIN Funcionarios f ON d.id_departamento = f.id_departamento
    GROUP BY d.id_departamento
    ORDER BY media_salario DESC;
    """)
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)
print("\n")

# 5. Listar qual departamento possui o maior número de dependentes.
def departamento_maior_numero_dependentes(cursor):
    cursor.execute("""
    SELECT d.nome_departamento, COUNT(dep.id_dependente) AS num_dependentes
    FROM Departamentos d
    JOIN Funcionarios f ON d.id_departamento = f.id_departamento
    LEFT JOIN Dependentes dep ON f.id_funcionario = dep.id_funcionario
    GROUP BY d.nome_departamento
    ORDER BY num_dependentes DESC
    LIMIT 1;
    """)
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)
print("\n")

#CONSULTAS PYTHON

# 6. Listar a média de idade dos filhos dos funcionários por departamento.
def media_idade_filhos_por_departamento(funcionarios, dependentes):
    from datetime import datetime

    idade_por_departamento = {}

    for dep in dependentes:
        id_funcionario = int(dep[3])
        data_nascimento = datetime.strptime(dep[1], '%Y-%m-%d')
        idade = (datetime.now() - data_nascimento).days // 365

        for func in funcionarios:
            if int(func[2]) == id_funcionario:
                departamento = func[3]
                
                if departamento not in idade_por_departamento:
                    idade_por_departamento[departamento] = []
                idade_por_departamento[departamento].append(idade)
                break 

    media_idades = {dep: sum(idades) / len(idades) for dep, idades in idade_por_departamento.items()} if idade_por_departamento else {}

    print("\nMédia de Idade dos Filhos por Departamento:")
    for dep, media in media_idades.items():
        print(f"Departamento {dep}: {media:.0f} anos")

    return media_idades
print("\n")

# 7. Listar qual estagiário possui filho.
def estagiario_com_filhos(funcionarios, dependentes):
    estagiarios = [func for func in funcionarios if func[3] == '6']

    estagiario_com_filhos = []
    for estagiario in estagiarios:
        estagiario_id = estagiario[2]

        for dep in dependentes:
            if dep[3] == estagiario_id:
                estagiario_com_filhos.append(estagiario[0])

    if estagiario_com_filhos:
        for nome in estagiario_com_filhos:
            print(nome)
    else:
        print("Nenhum estagiário com filhos encontrado.")
print("\n")

# 8. Listar o funcionário que teve o salário médio mais alto. # QUINTA CONSULTA SQL
def funcionario_salario_medio_mais_alto(cursor):
    cursor.execute("""
    SELECT f.nome, AVG(h.salario) AS salario_medio
    FROM Funcionarios f
    JOIN HistoricoSalarios h ON f.id_funcionario = h.id_funcionario
    GROUP BY f.id_funcionario
    ORDER BY salario_medio DESC
    LIMIT 1;
    """)
    resultado = cursor.fetchone()
    print(resultado)
print("\n")

# 9. Listar o analista que é pai de 2 (duas) meninas.
def analista_pai_duas_meninas(funcionarios, dependentes):
    analistas = [func for func in funcionarios if func[3] == '3']

    for analista in analistas:
        analista_id = analista[2]
        
        filhas = [dep for dep in dependentes if dep[3] == analista_id and dep[2] == 'F']
        
        if len(filhas) == 2:
            print(analista[0])
print("\n")

# 10. Listar o analista que tem o salário mais alto e que ganhe entre 5000 e 9000.
def analista_salario_alto(funcionarios):
    analistas = [func for func in funcionarios if func[2] == '3' and 5000 <= float(func[4]) <= 9000]
    
    analista_mais_bem_pago = max(analistas, key=lambda x: float(x[4]))
    print(f"{analista_mais_bem_pago[0]} | Salário: {analista_mais_bem_pago[4]}.")

def main():
    conn = conectar()
    cursor = conn.cursor()
    
    criar_tabelas(cursor)
    limpar_tabelas(cursor)
    criar_csvs()
    inserir_dados_csv(cursor)
    
    print("------------------- CONSULTAS SQL -------------------")
    print("\n")
    
    print("1. Listar individualmente as tabelas de: Funcionários, Cargos, Departamentos, Histórico de Salários e Dependentes em ordem crescente.")
    listar_tabelas(cursor)
    print("\n")
    
    print("2. Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes.")
    listar_funcionarios_com_dependentes(cursor)
    print("\n")
    
    print("3. Listar os funcionários que tiveram aumento salarial nos últimos 3 meses.")
    listar_funcionarios_aumento(cursor)
    print("\n")
    
    print("4. Listar a média de salário por departamento em ordem decrescente.")
    media_salario_por_departamento(cursor)
    print("\n")
    
    print("5. Listar qual departamento possui o maior número de dependentes.")
    departamento_maior_numero_dependentes(cursor)
    print("\n")

    funcionarios = ler_csv('funcionarios.csv')
    dependentes = ler_csv('dependentes.csv')
    
    print("------------------- CONSULTAS PYTHON -------------------")
    print("\n")
    
    print("6. Listar a média de idade dos filhos dos funcionários por departamento.")
    media_idade_filhos_por_departamento(funcionarios, dependentes)
    print("\n")
    
    print("7. Listar qual estagiário possui filho.")
    estagiario_com_filhos(funcionarios, dependentes)
    print("\n")
    
    print("8. Listar o funcionário que teve o salário médio mais alto.")
    funcionario_salario_medio_mais_alto(cursor)
    print("\n")
    
    print("9. Listar o analista que é pai de 2 (duas) meninas.")
    analista_pai_duas_meninas(funcionarios, dependentes)
    print("\n")
    
    print("10. Listar o analista que tem o salário mais alto e que ganhe entre 5000 e 9000.")
    analista_salario_alto(funcionarios)
    print("\n")

    conn.commit()
    conn.close()

main()