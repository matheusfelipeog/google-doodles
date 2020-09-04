<div align='center'>
    <img src='./logo-google-doodles.jpg' alt='Logo Google Doodle 1998' />
</div>

# Objetivo

O projeto irá mapear todos os **Doodles do Google**, partindo do doodle informado até o mais recente, e estruturando todos os dados em um arquivo **Json**. Também é possível realizar o download de todos os **Doodles** mapeados anteriormente no arquivo json em seu disco rígido.

# Instalação

O script foi desenvolvido em [Python 3.7](https://www.python.org/), podendo ter algumas alterações em versões anteriores da linguagem. Certifique-se de que o tenha instalado em seu ambiente.

Para executar o programa siga os passos abaixo para preparar seu ambiente com os requerimentos do script.

1. **Instalação das dependências via Pip**.

```
pip install -r requirements.txt
```

2. **Para mapear os doodles execute:**
```
python main.py
```
Caso queira iniciar o mapeamento de um doodle especifico para o mais atual, passe o nome contido na URL como argumento para a função `start` em [main.py](./main.py):
```Python
data = start("O doodle inicial aqui")

# Exemplo:
#   Para https://www.google.com/doodles/josephine-langs-205th-birthday 
# faça:
data = start("josephine-langs-205th-birthday")
```

3. **Para realizar o download dos doodles mapeados anteriormente, execute:**
```
python sample/download.py
```
O downloads dos doodles mapeados será feito e guardado no diretório [logos/](./data/logos).

# Contribuição

Caso queira realizar uma ou mais contribuições, siga:

* **Referente a código:**

   * Faça o `Fork` do repositório para a sua conta;
   * Realize o `clone` do repositório para seu ambiente. (`git clone https://github.com/SEU-USUARIO/google-doodles.git`)
   * Crie sua branch com `git checkout -b feature/nomeia-sua-contribuição`
   * Faça sua contribuição e commite todas alterações. (`git commit`)
   * Push para seu repositório (`git push origin feature/nomeia-sua-contribuição`) e logo em seguida faça o *Pull Request* para que seja analisado sua contribuição e mesclada com a master.

* **Outras:**

Caso tenha dicas de melhoria, encontre bugs ou queira reportar algo relacionado, abra uma Issue.

Toda Contribuição é bem vinda ;)

# Licença
Todo o código do projeto está sobe a licença [MIT](./LICENSE).
