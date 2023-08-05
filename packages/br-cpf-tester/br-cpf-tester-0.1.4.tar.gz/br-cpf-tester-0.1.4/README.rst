Brazilian CPF Tester  (WTTD training)
=====================================

*br-cpf-tester* This is a test implementatipon of the Brazilian CPF Validation as part of
the "Mão na Massa" proposal of the 4th module of Welcome to the Django
training (http://welcometothedjango.com.br/).

CPF is a document that identifies a taxpayer at the Federal Internal Revenue
Department. The CPF carries registration information supplied by the
individual and by the Federal Internal Revenue Department database.

This number is currently formated as XXX.XXX.XXX-DD where X are digits and D
are check digits.

.. image:: https://travis-ci.org/Jaimenms/python-br-cpf-tester.svg?branch=master
    :target: https://travis-ci.org/Jaimenms/python-br-cpf-tester

.. image:: https://landscape.io/github/Jaimenms/python-br-cpf-tester/master/landscape.svg?style=flat
   :target: https://landscape.io/github/Jaimenms/python-br-cpf-tester/master
   :alt: Code Health


Como desenvolver?
-----------------

#. Clone o repositório
#. Crie um virtualenv com Python 3.6.
#. Ative o virtualenv.
#. Instale as dependências
#. Execute os testes

.. code-block:: console

    git clone git@github.com:jaimenms/python-br-cpf-tester.git python brcpf
    cd brcpf
    python -m venv .brcpf
    source .brcpf/bin/activate
    pip install -r requirements.txt
    pytest

Como instalar?
--------------

.. code-block:: console

    pip install br-cpf-tester


Como utilizar dentro de um validator.py no django?
--------------------------------------------------

.. code-block:: python

    from django.core.exceptions import ValidationError
    from brcpftester import BrazilianCpfValidationTests

    def validate_cpf(value):
        cpf = BrazilianCpfValidationTests()
        cpf(value)
        for test in cpf.tests:
            raise ValidationError(cpf.GetMessage(test), test)
