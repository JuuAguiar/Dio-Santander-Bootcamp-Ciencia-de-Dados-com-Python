ETL com Python  

## 📌 Descrição do Projeto

Este projeto implementa um pipeline completo de ETL (Extract, Transform, Load) utilizando Python.  
Devido às limitações das APIs externas, todo o processo foi realizado com dados mockados, mantendo a lógica real de um fluxo de dados corporativo.

## 🧱 Etapas do Pipeline

### 🔹 Extract
- Leitura de IDs de usuários a partir de um arquivo CSV
- Filtragem de registros em um arquivo JSON simulado

### 🔹 Transform
- Geração de mensagens personalizadas com base no saldo do cliente
- Inserção dessas mensagens no campo `news` de cada usuário

### 🔹 Load
- Simulação de envio dos dados transformados
- Persistência do resultado final em arquivo JSON

## ✅ Resultados

- Pipeline ETL implementado com sucesso
- Carga de dados simulada corretamente
- Arquivos finais gerados
- Estrutura modular e reutilizável
