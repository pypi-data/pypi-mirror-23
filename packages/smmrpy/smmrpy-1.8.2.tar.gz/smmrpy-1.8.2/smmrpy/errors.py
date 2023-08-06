class InternalServerError(Exception):
    "Internal server problem which isn\'t your fault."
    pass

class IncorrectSubmissionVariables(Exception):
    "Incorrect submission variables were passed."
    pass

class IntentionalRestriction(Exception):
    "Intentional restriction. Could be low credits, disabled key, or banned key."
    pass

class SummarizationError(Exception):
    "There was an issue summarizing the article URL passed."
    pass
