# 🧹 Python Cache Cleaner

Um script Python simples e eficiente para limpar arquivos de cache do seu projeto Python.

## 📋 Descrição

Este script automatiza a remoção de arquivos temporários e diretórios de cache gerados pelo Python durante o desenvolvimento, mantendo seu projeto limpo e organizado.

## 🗑️ O que é removido

- **`__pycache__`** - Diretórios de cache de bytecode Python
- **`.pytest_cache`** - Cache de testes do pytest
- **`*.pyc`** - Arquivos de bytecode Python compilados
- **`*.pyo`** - Arquivos de bytecode otimizados
- **`.coverage`** - Arquivo de cobertura de testes

## 🚀 Como usar

### Método 1: Executar diretamente

```bash
# Torne o script executável
chmod +x clean.py

# Execute
./clean.py
```

### Método 2: Usar com Python

```bash
python clean.py
```

### Método 3: Adicionar como alias no seu shell

No seu `~/.bashrc` ou `~/.zshrc`:

```bash
alias cleanpy='python /caminho/para/clean.py'
```

## 📁 Estrutura do Script

```python
clean_python_cache()          # Função principal de limpeza
├── Remover diretórios       # __pycache__, .pytest_cache
└── Remover arquivos        # *.pyc, *.pyo, .coverage
```

## 🔧 Funcionalidades

- ✅ **Recursivo**: Limpa todos os subdiretórios do projeto
- ✅ **Seguro**: Usa try-except para evitar erros
- ✅ **Informativo**: Mostra contagem do que foi removido
- ✅ **Cross-platform**: Funciona em Linux, macOS e Windows
- ✅ **Não destrutivo**: Não remove código fonte, apenas cache

## 📊 Saída do Script

```
🗑️  Removido diretório: ./app/__pycache__
🗑️  Removido diretório: ./tests/__pycache__
⚠️  Erro ao remover ./some/protected/dir: [Permission denied]

✅ Limpeza concluída!
📁 Diretórios removidos: 2
📄 Arquivos removidos: 15
```

## 🛡️ Segurança

O script **NUNCA** remove:
- Arquivos `.py` (código fonte)
- Diretórios importantes do projeto
- Arquivos de configuração
- Banco de dados ou arquivos de dados

## 📌 Melhores Práticas

### 1. Adicione ao `.gitignore`
```gitignore
# Python cache
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/
.coverage
```

### 2. Execute antes de commits
```bash
# Adicione ao pre-commit hook
echo "python clean.py" >> .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### 3. Integre com makefile
```makefile
clean:
    python clean.py
    rm -rf build/ dist/ *.egg-info

.PHONY: clean
```

### 4. Configure no VS Code
No `.vscode/settings.json`:
```json
{
    "python.analysis.exclude": ["**/__pycache__", "**/.pytest_cache"]
}
```

## 🐛 Solução de Problemas

### Erro de permissão
```bash
# Execute com sudo (se necessário)
sudo python clean.py
```

### Script não executa
```bash
# Verifique permissões
ls -la clean.py

# Corrija permissões
chmod +x clean.py
```

### Cache reaparece
Isso é normal! O Python recria cache quando executa código. Considere:

1. **Ignorar no Git**: Certifique-se que está no `.gitignore`
2. **Configurar IDE**: Exclua das buscas da sua IDE
3. **Ambiente virtual**: O cache fica isolado no venv

## 🔄 Alternativas

### Usando find (Linux/macOS)
```bash
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
```

### Usando PowerShell (Windows)
```powershell
Get-ChildItem -Path . -Include __pycache__ -Recurse -Directory | Remove-Item -Recurse -Force
Get-ChildItem -Path . -Include *.pyc -Recurse -File | Remove-Item -Force
```

## 📚 Por que limpar cache?

1. **Reduz tamanho do projeto** - Arquivos de cache podem ser grandes
2. **Evita conflitos** - Entre diferentes versões do Python
3. **Mantém organização** - Projeto mais limpo para compartilhar
4. **Previne commits acidentais** - Cache não deve ir para o repositório
5. **Força recompilação** - Garante bytecode atualizado

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Crie um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ⚠️ Aviso

Este script é fornecido "como está", sem garantias. Sempre verifique o que será removido antes de executar em projetos importantes.

---
**Dica**: Execute regularmente para manter seu projeto Python limpo! 🚀
