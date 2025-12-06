# DeepAdSafe: Detecção de Fraudes em Anúncios com Deepfakes

## Projeto em Andamento

## Resumo
A proliferação de deepfakes em anúncios pagos transformou golpes online em um problema crescente.  
Este projeto propõe um sistema multimodal capaz de identificar manipulações audiovisuais e padrões linguísticos usados em anúncios fraudulentos.

---

## Índice
- [Resumo](#resumo)
- [1. Motivação](#1-motivação)
- [2. Objetivos](#2-objetivos)
- [3. Base Teórica](#3-base-teórica)
  - [3.1 Deepfakes](#31-deepfakes)
  - [3.2 Linguagem Natural](#32-linguagem-natural)
  - [3.3 Fusão Multimodal](#33-fusão-multimodal)
- [4. Metodologia](#4-metodologia)
- [5. Arquitetura](#5-arquitetura)
  - [5.1 Módulo Visual](#51-módulo-visual)
  - [5.2 Módulo de Linguagem](#52-módulo-de-linguagem)
  - [5.3 Fusão de Previsões](#53-fusão-de-previsões)
  - [5.4 API](#54-api)
  - [5.5 Dashboard](#55-dashboard)
- [6. Experimentos](#6-experimentos)
- [7. Resultados Esperados](#7-resultados-esperados)
- [8. Limitações](#8-limitações)
- [9. Ética](#9-ética)
- [10. Como Executar](#11-como-executar)
  - [10.1 Clonar o repositório](#111-clonar-o-repositório)
  - [10.2 Criar ambiente virtual](#112-criar-ambiente-virtual)
  - [10.3 Instalar dependências](#113-instalar-dependências)
  - [10.4 Executar API](#114-executar-api)
  - [10.5 Executar Dashboard](#115-executar-dashboard)
- [11. Licença](#12-licença)
- [Contribuições](#contribuições)

---


---

# 1. Motivação
Deepfakes baratearam a criação de golpes.  
Usuários comuns não conseguem distinguir o real do falso.  
Plataformas demoram para agir.  
Criminosos usam rostos de figuras públicas para aumentar a credibilidade.

Este projeto investiga tecnicamente esse cenário e propõe um mecanismo de detecção estruturado.

---

# 2. Objetivos

### Objetivo Geral
Desenvolver um pipeline completo para detecção automática de anúncios fraudulentos gerados com deepfakes.

### Objetivos Específicos
- Criar dataset curado de anúncios e deepfakes reais.  
- Implementar detector de manipulação visual.  
- Desenvolver classificador linguístico baseado em padrões de fraude.  
- Integrar previsões multimodais.  
- Disponibilizar API e dashboard.  
- Documentar métricas científicas.

---

# 3. Base Teórica

## 3.1 Deepfakes
Detecção baseada em:
- microexpressões  
- inconsistências de iluminação  
- sincronização labial  
- artefatos de compressão  

Modelos utilizados como baseline: XceptionNet, EfficientNet, Vision Transformers.

## 3.2 Linguagem Natural
Padrões clássicos de golpes:
- ganho rápido  
- urgência  
- falsa autoridade  
- persuasão emocional  

Modelos usados: BERT, DistilBERT e variantes.

## 3.3 Fusão Multimodal
Combinação entre:
- análise visual  
- análise textual  
- metadados do anúncio  

---

# 4. Metodologia

Pipeline geral:

- Coleta de anúncios e deepfakes

- Pré-processamento audiovisual

- Extração de features visuais

- Extração de features linguísticas

- Classificação multimodal

- Score de risco

- API + Dashboard

  
---

# 5. Arquitetura

## 5.1 Módulo Visual
Detector baseado em redes pré-treinadas com fine-tuning no dataset criado.

## 5.2 Módulo de Linguagem
Classificador de discurso enganoso utilizando transformers.

## 5.3 Fusão de Previsões
Modelo integrador que produz um `fraud_score`.

## 5.4 API
Endpoints REST para envio de vídeos, imagens e textos.

## 5.5 Dashboard
Interface para:
- visualização do nível de risco  
- explicabilidade (GradCAM / atenção)  
- histórico de anúncios analisados  

---

# 6. Experimentos

Métricas a serem avaliadas:
- AUC  
- F1-score  
- Precisão  
- Recall  
- Equal Error Rate (EER)

Também serão analisados:
- impacto da compressão dos vídeos  
- comparação entre modelos  
- erros recorrentes  

---

# 7. Resultados Esperados
- Detector eficaz de deepfakes em vídeos curtos.  
- Classificador textual preciso.  
- Pipeline funcional e replicável.  
- Ferramenta aplicável em pesquisas de segurança digital.

---

# 8. Limitações
- Deepfakes evoluem rapidamente.  
- Vídeos muito comprimidos podem reduzir acurácia.  
- Algoritmos das plataformas mudam com frequência.  

---

# 9. Ética
Este projeto segue:
- uso responsável de dados  
- anonimização  
- proibição total da criação de deepfakes para fins maliciosos  
- foco em pesquisa e proteção digital  

---


---

## 10. Como Executar

### 10.1 Clonar o repositório
```bash
git clone https://github.com/CarlosEduardo-01/DeepAdSafe.git
cd DeepAdSafe
```

### 10.2 Criar ambiente virtual

```bash
 python -m venv venv
 source venv/bin/activate   # Linux / macOS
 venv\Scripts\activate      # Windows (PowerShell)
```
### 10.3 Instalar dependências

```bash
pip install -r requirements.txt
```

### 10.4 Executar API

```bash
uvicorn src.api.main:app --reload
```

### 10.5 Executar Dashboard

```bash
python src/dashboard/app.py
```

### 11. Licença

MIT — com cláusula de proibição de uso malicioso.

### Contribuições

 Pull requests são bem-vindos desde que:

- tragam referência teórica;

- descrevam metodologia;

- forneçam resultados reproduzíveis;

- apresentem justificativa técnica.

### Contato / Autor

Nome: Carlos Eduardo Almeida do Nascimento

Email: cadueduvip01@gmail.com
