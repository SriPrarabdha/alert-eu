ontology = Ontology(
    # labels of the entities to be extracted. Can be a string or an object, like the following.
    labels=[
        {"Person": "Person name without any adjectives, Remember a person may be references by their name or using a pronoun"},
        {"Object": "Do not add the definite article 'the' in the object name"},
        {"Event": "Event event involving multiple people. Do not include qualifiers or verbs like gives, leaves, works etc."},
        "Place",
        "Document",
        "Organisation",
        "Action",
        {"Miscellanous": "Any important concept can not be categorised with any other given label"},
    ],
    # Relationships that are important for your application.
    # These are more like instructions for the LLM to nudge it to focus on specific relationships.
    # There is no guarentee that only these relationships will be extracted, but some models do a good job overall at sticking to these relations.
    relationships=[
        "Relation between any pair of Entities",
        ],
)