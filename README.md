# 🚀 Automação de Cargas de Atualização de Preços - Bluesoft/Zanthus

Automação completa para geração de cargas de atualização de preços nos sistemas Bluesoft e Zanthus, utilizada pela rede de supermercados Mini Preço.

## 📌 Visão Geral
![Interface Screenshot](screenshot.png) *(adicione uma imagem da interface)*

Este software automatiza o processo de:
- Geração de arquivos de atualização de preços no Bluesoft
- Carga sequencial nos PDVs via Zanthus
- Atualização para todas as lojas da rede (Mini Preço e Salvados)
- Controle por grupos de lojas (estados específicos ou todas)

## ✨ Funcionalidades
- **Interface amigável** com seleção por grupos de lojas
- **Processo 100% automático** desde login até confirmação de conclusão
- **Verificação em tempo real** do status das cargas
- **Tratamento de erros** com repetição inteligente
- **Logs visuais** do progresso das operações

## ⚙️ Tecnologias Utilizadas
- **Python 3.8+**
- **Selenium WebDriver** (controle navegador)
- **Tkinter** (interface gráfica)
- **WebDriver Manager** (gerenciamento automático de drivers)

## 🛠️ Requisitos e Instalação

### Pré-requisitos
- Python 3.8 ou superior
- Google Chrome instalado
- Acesso aos sistemas com login e senha:
  - Bluesoft (https://erp.bluesoft.com.br/minipreco)
  - Zanthus (https://minipreco.zanthus.bluesoft.com.br)
