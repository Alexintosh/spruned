class SprunedException(Exception):
    pass


class ServiceException(SprunedException):
    pass


class HTTPClientException(SprunedException):
    pass


class SpentTxOutException(SprunedException):
    pass


class InvalidPOWException(SprunedException):
    pass


class SourcesDisagreementException(SprunedException):
    pass
