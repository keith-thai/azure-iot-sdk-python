# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class X509Attestation(Model):
    """Attestation via X509.

    :param client_certificates:
    :type client_certificates: ~protocol.models.X509Certificates
    :param signing_certificates:
    :type signing_certificates: ~protocol.models.X509Certificates
    :param ca_references:
    :type ca_references: ~protocol.models.X509CAReferences
    """

    _attribute_map = {
        "client_certificates": {"key": "clientCertificates", "type": "X509Certificates"},
        "signing_certificates": {"key": "signingCertificates", "type": "X509Certificates"},
        "ca_references": {"key": "caReferences", "type": "X509CAReferences"},
    }

    def __init__(self, **kwargs):
        super(X509Attestation, self).__init__(**kwargs)
        self.client_certificates = kwargs.get("client_certificates", None)
        self.signing_certificates = kwargs.get("signing_certificates", None)
        self.ca_references = kwargs.get("ca_references", None)
