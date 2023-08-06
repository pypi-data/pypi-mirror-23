=============
PyCEPCorreios
=============


.. image:: https://img.shields.io/travis/mstuttgart/pycep-correios/develop.svg?style=flat-square
    :target: https://travis-ci.org/mstuttgart/pycep-correios

.. image:: https://img.shields.io/coveralls/mstuttgart/pycep-correios/develop.svg?style=flat-square
    :target: https://coveralls.io/github/mstuttgart/pycep-correios?branch=develop

.. image:: https://landscape.io/github/mstuttgart/pycep-correios/develop/landscape.svg?style=flat-square
    :target: https://landscape.io/github/mstuttgart/pycep-correios/develop

.. image:: https://img.shields.io/requires/github/mstuttgart/pycep-correios.svg?style=flat-square
    :target: https://requires.io/github/mstuttgart/pycep-correios/requirements/?branch=develop
    :alt: Requirements Status

.. image:: https://img.shields.io/pypi/v/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/pyversions/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/l/pycep-correios.svg?style=flat-square
    :target: https://github.com/mstuttgart/pycep-correios/blob/develop/LICENSE

API para consulta de CEP diretamente do *webservice* dos Correios.

Features
--------
* Consulta de dados do endereço de um CEP
* Formatacao de CEP
* Validação de estrutura do CEP

Documentação
------------

Para mais detalhes sobre a PyCEPCorreios, por gentileza, consulte a documentação oficial:

* Documentação online: https://pycep-correios.readthedocs.io.
* Documentação PDF: https://media.readthedocs.org/pdf/pycep-correios/stable/pycep-correios.pdf

Instalação
----------
O PyCEP Correios pode ser facilmente instalado com o comando a seguir:

.. code:: bash

    pip install pycep-correios

Atualmente, a PyCEPCorreios possui suporte para Python 2.7+ e 3.3+.

Como usar
---------

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios.
Veja os exemplos a seguir:

.. code-block:: python

    >>> import pycep_correios

    >>> endereco = pycep_correios.consultar_cep('37503130')
    >>> print(endereco)
    {
        'bairro': 'Santo Antônio',
        'cep': '37503130',
        'cidade': 'Itajubá',
        'end': 'Rua Geraldino Campista',
        'id': '0',
        'uf': 'MG',
        'complemento': '',
        'complemento2': '- até 214/215',
    }

Aviso de *bugs*, dúvidas e sugestões
------------------------------------
Para dúvidas, sugestões e relatórios de *bugs*, por gentileza, crie uma *issue*:

- Issue Tracker: https://github.com/mstuttgart/pycep-correios/issues

Créditos
--------

Copyright (C) 2016-2017 por Michell Stuttgart Faria


=========
Histórico
=========

2.2.0 (2017-07-16)
------------------

* Melhorias no metodo de formatar_cep, que agora passou a utilizar expressão regular para verificar se o CEP é formado por caracteres.
* A função *formatar_cep* agora passa a lançar a exceção *Value Error* quando o CEP não possui estrutura válida https://github.com/mstuttgart/pycep-correios/pull/22
* Adicionado novas exceções ExcecaoPyCEPCorreios, Timeout, MultiploRedirecionamento, FalhaNaConexao. Consultar documentacao para exemplos de utilização delas. close https://github.com/mstuttgart/pycep-correios/issues/25
* Adicionado ambientes de *Homologação* e *Producao*. Facilitando realizar consultas utilizadas para testes. close https://github.com/mstuttgart/pycep-correios/issues/24
* Melhorias na organização da API.

2.1.1 (2017-06-30)
------------------

* Correção de erros de unicode com python2.7

2.1.0 (2017-06-29)
------------------

* Adicionado suporte para Python 2.7+
* Ajustes e correções na documentação

2.0.0 (2017-06-20)
------------------

* Atualização do código da PyCEPCorreios, deixando-a mais facil de ser utilizada
* Remoção das exceções antigas, deixando apenas a Exceção padrão da lib
* Remoção da classe PyCEPCorreios
* Alteração dos *imports* da lib para facilitar seu uso e diminuir tamanho dos *imports*
* Adicionado documentação com Sphinx
* Adicionado testes com TOX
* Adicionado método de validação de CEP e formatação de CEP

1.1.7 (2017-05-09)
------------------

* [FIX] Corrigido erro `jinja2.exceptions.TemplateNotFound: consultacep.xml`
* [FIX] Erro durante instalação da PyCEPCorreios via pip
* [FIX] Atualizado código de exemplo no README.rst
* [FIX] Atualizado exemplos na documentação

1.1.6 (2017-05-08)
------------------

* [FIX] Correção de bug durante instalação. #15
* [FIX] Correção de template xml ausente no pacote do modulo
* [FIX] Melhorias gerais no código e correções de bugs

1.1.1 (2017-02-08)
------------------

* Melhorias gerais no código
* XML schema utilizando Jinja2

1.0.1 (2016-08-03)
------------------

* Simplificação da classes Exceptions
* Organização do código de teste
* Utilização do mock para test

1.0.0 (2016-07-31)
------------------

* API migrada para Python 3. Python 2.7 não será mais suportado
* Substituição da lib *suds* pela lib *requests* para realizar as requisições

0.0.2 (2016-05-09)
------------------

* `setup.py` com número de versão atualizado e dependência corrigidas.

0.0.1 (2016-05-05)
------------------

* Versão inicial.
* Permite busca no webservice dos correios dos dados de um CEP fornecido.


