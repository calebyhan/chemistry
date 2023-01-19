Documentation for chemistry-ch
===================================

**chemistry-ch** is a Python library for chemistry equations and forumulas.

Check out the `usage`_ section for further information, including
how to `installation`_ the project.

.. note::

   This project is under active development.

Contents
--------

.. contents:: Table of Contents
   :backlinks: none

Usage
=====

.. _installation:

Installation
------------

To use chemistry-ch, first install it using pip:

.. code-block:: console

   (.venv) $ pip install chemistry-ch

No dependencies are needed.

.. _functions:

Functions
----------------

chemistry-ch offers 3 sub-files as well as constants:

.. code-block:: Python

    import chemistry.conversions
    import chemistry.formulas
    import chemistry.periodic

.. _conversions:

Conversions
^^^^^^^^^^^^^^^

``chemistry.conversions.k_to_c(k)``
   Inputs kelvin and converts to celcius.

``chemistry.conversions.k_to_f(k)``
   Inputs kelvin and converts to fahrenheit.

``chemistry.conversions.c_to_k(c)``
   Inputs celcius and converts to kelvin.

``chemistry.conversions.c_to_f(k)``
   Inputs celcius and converts to fahrenheit.

``chemistry.conversions.f_to_k(k)``
   Inputs fahrenheit and converts to kelvin.

``chemistry.conversions.f_to_c(k)``
   Inputs fahrenheit and converts to celcius.

``chemistry.conversions.metric(num, pre1, pre2)``
   Inputs a value and starting prefix and final prefix to return converted value.

.. _formulas:

Formulas
^^^^^^^^^^^^^^^

``chemistry.forumulas.atomicWeight(weights)``
   Input 2D array of atomic weights and percentages to find overall atomic weight.

``chemistry.forumulas.molarity(molarity, moles, volume)``
   Input two of molarity, moles, and volume and outputs the third.

.. _periodic:

Periodic
^^^^^^^^^^^^^^^

NOTE: All inputs work in element symbol or number.

``chemistry.periodic.name(ele)``
   Input element and return element name.

``chemistry.periodic.number(ele)``
   Input element and return atomic number.

``chemistry.periodic.symbol(ele)``
   Input element and return symbol.

``chemistry.periodic.mass(ele)``
   Input element and return atomic mass.

``chemistry.periodic.elecConfig(ele)``
   Input element and return electron configuration.

``chemistry.periodic.position(ele)``
   Input element and return its position in (period, group).

``chemistry.periodic.elecNeg(ele)``
   Input element and return electronegativty.

``chemistry.periodic.atomRadius(ele)``
   Input element and return atomic radius.

``chemistry.periodic.ionRadius(ele)``
   Input element and return ionic radius.

``chemistry.periodic.standardState(ele)``
   Input element and return its standard state.

``chemistry.periodic.ionEnergy(ele)``
   Input element and return ionization energy.

``chemistry.periodic.elecAffinity(ele)``
   Input element and return electron affinity.

``chemistry.periodic.meltingPoint(ele)``
   Input element and return melting point.

``chemistry.periodic.boilingPoint(ele)``
   Input element and return boiling point.

``chemistry.periodic.block(ele)``
   Input element and return block

``chemistry.periodic.year(ele)``
   Input element and return year discovered

``chemistry.periodic.groupBlock(ele)``
   Input element and return group block

``chemistry.periodic.oxidationStates(ele)``
   Input element and return possible oxidation states in a list

``chemistry.periodic.molar_mass(molecule)``
   Input molecule and return molar mass.