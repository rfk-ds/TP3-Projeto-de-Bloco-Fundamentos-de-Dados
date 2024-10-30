# TP3-Projeto-de-Bloco-Fundamentos-de-Dados

## Descrição
Este projeto implementa um sistema de gerenciamento de funcionários utilizando Python e SQLite. O sistema permite a manipulação de dados relacionados a funcionários, cargos, departamentos e dependentes, além de realizar diversas consultas analíticas.

## Estrutura do Banco de Dados
O banco de dados é composto por cinco tabelas principais:

- **Cargos**
- **Departamentos**
- **Funcionarios**
- **HistoricoSalarios**
- **Dependentes**

## Arquivos CSV Criados
O projeto gera os seguintes arquivos CSV para popular as tabelas do banco de dados:

- `cargos.csv`
- `departamentos.csv`
- `funcionarios.csv`
- `historico_salarios.csv`
- `dependentes.csv`

## Consultas Realizadas
O sistema realiza as seguintes consultas:

1. Listar individualmente as tabelas de Funcionários, Cargos, Departamentos, Histórico de Salários e Dependentes.
2. Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes.
3. Listar os funcionários que tiveram aumento salarial nos últimos 3 meses.
4. Listar a média de salário por departamento em ordem decrescente.
5. Listar qual departamento possui o maior número de dependentes.
6. Listar a média de idade dos filhos dos funcionários por departamento.
7. Listar qual estagiário possui filho.
8. Listar o funcionário que teve o salário médio mais alto.
9. Listar o analista que é pai de duas meninas.
10. Listar o analista que tem o salário mais alto e que ganhe entre 5000 e 9000.
