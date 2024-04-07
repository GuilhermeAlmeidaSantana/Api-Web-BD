# Api-Web-BD
Repositorio para a atividade da api web para Banco de Dados I
Alunos: Guilherme Almeida e Rafael Miranda

O arquivo main.py possui a resolução completa da atividade 4 - parte 2. O nosso projeto se constitui de um schema de clínica com múltiplas tabelas.

Essa parte do projeto é composta por um CRUD que se conecta a um SGBD criado anteriormente. Do schema, as tabelas escolhidas foram:
  - Usuario (Tabela gerada por uma entidade)
  - Enfermidade (Tabela gerada por uma entidade)
  - Consultas (Tabela gerada por um relacionamneto)

O SGBD foi monitorado atravês do PGAdimin4 e a API foi testada atravês do Insomnia.

Como dito antes, o CRUD está funcional para as 3 tabelas, o framework Flask foi usado para a criação da API, enquanto que a conexão com SGBD foi feita pela biblioteca psycopg2. A entrada e saida dos dados está sendo feita através do JSON.
