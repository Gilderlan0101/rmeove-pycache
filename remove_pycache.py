#!/usr/bin/env python3
import os
import shutil
import sys

def clean_python_cache():
    """Remove arquivos de cache do Python"""
    patterns = ['__pycache__', '.pytest_cache', '*.pyc', '*.pyo', '.coverage']
    dirs_removed = 0
    files_removed = 0

    for root, dirs, files in os.walk('.', topdown=False):
        # Remove diretórios __pycache__
        for dir_name in dirs:
            if dir_name == '__pycache__' or dir_name == '.pytest_cache':
                path = os.path.join(root, dir_name)
                try:
                    shutil.rmtree(path)
                    dirs_removed += 1
                    print(f"🗑️  Removido diretório: {path}")
                except Exception as e:
                    print(f"⚠️  Erro ao remover {path}: {e}")

        # Remove arquivos .pyc e .pyo
        for file_name in files:
            if file_name.endswith('.pyc') or file_name.endswith('.pyo'):
                path = os.path.join(root, file_name)
                try:
                    os.remove(path)
                    files_removed += 1
                except Exception as e:
                    print(f"⚠️  Erro ao remover {path}: {e}")

    print(f"\n✅ Limpeza concluída!")
    print(f"📁 Diretórios removidos: {dirs_removed}")
    print(f"📄 Arquivos removidos: {files_removed}")

if __name__ == '__main__':
    clean_python_cache()
