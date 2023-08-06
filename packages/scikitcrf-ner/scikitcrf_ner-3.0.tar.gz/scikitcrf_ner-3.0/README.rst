====================================
Entity recognition using scikit CRF
====================================

^^^^^^^^^^^^^
Decscription
^^^^^^^^^^^^^

This is a simple python applicaion that uses `sklearn-crfsuite<https://sklearn-crfsuite.readthedocs.io/en/latest/>`_ for entity recognition using ``CRF``.

^^^^^^^^^^^^^
Installation
^^^^^^^^^^^^^

Install this package using pip by running the follwing command::

	pip install scikitcrf_ner

^^^^^^
Usage
^^^^^^

* import the package using::

	import scikitcrf_ner
* Train the model using::

	scikitcrf_ner.train("path\\to\\trainingfile.json")\
* Refer the sample training file(``sample_train.json``), the training file should be json formatted
* Predict the entities by::

	scikitcrf_ner.predict("Utterance")

^^^^^^^^^^^^
Sample code
^^^^^^^^^^^^

Refer this sample code::

	import scikitcrf-ner
	scikitcrf_ner.train("sample_train.json")
	entities = scikitcrf_ner.predict("show me some Indian restaurants")
	print(entites)

^^^^^^^^
License
^^^^^^^^
* ``MIT``
