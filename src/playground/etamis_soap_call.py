import requests
import logging
import sys
import socket
from requests import adapters
from requests_toolbelt.adapters.socket_options import SocketOptionsAdapter

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a stream handler
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

print(sys.platform)

class TCPKeepAliveAdapter(SocketOptionsAdapter):
    """An adapter for requests that turns on TCP Keep-Alive by default.

    The adapter sets 4 socket options:

    - ``SOL_SOCKET`` ``SO_KEEPALIVE`` - This turns on TCP Keep-Alive
    - ``IPPROTO_TCP`` ``TCP_KEEPINTVL`` 20 - Sets the keep alive interval
    - ``IPPROTO_TCP`` ``TCP_KEEPCNT`` 5 - Sets the number of keep alive probes
    - ``IPPROTO_TCP`` ``TCP_KEEPIDLE`` 60 - Sets the keep alive time if the
      socket library has the ``TCP_KEEPIDLE`` constant

    The latter three can be overridden by keyword arguments (respectively):

    - ``idle``
    - ``interval``
    - ``count``

    You can use this adapter like so::

       >>> from requests_toolbelt.adapters import socket_options
       >>> tcp = socket_options.TCPKeepAliveAdapter(idle=120, interval=10)
       >>> s = requests.Session()
       >>> s.mount('http://', tcp)

    """

    def __init__(self, **kwargs):
        socket_options = kwargs.pop('socket_options',
                                    SocketOptionsAdapter.default_options)
        idle = kwargs.pop('idle', 60)
        interval = kwargs.pop('interval', 20)
        count = kwargs.pop('count', 5)
        socket_options = socket_options + [
            (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        ]

        # NOTE(Ian): Apparently OSX does not have this constant defined, so we
        # set it conditionally.
        if getattr(socket, 'TCP_KEEPIDLE', None) is not None:
            socket_options += [(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, idle)]

        # socket_options += [(socket.IPPROTO_TCP, 0x10, interval)]

        if getattr(socket, 'TCP_KEEPINTVL', None) is not None:
            socket_options += [(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval)]
        else:
            # For OSX:
            # scraped from /usr/include, not exported by python's socket module
            # TCP_KEEPALIVE = 0x10
            socket_options += [(socket.IPPROTO_TCP, 0x10, interval)]

        if getattr(socket, 'TCP_KEEPCNT', None) is not None:
            socket_options += [(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, count)]

        super(TCPKeepAliveAdapter, self).__init__(
            socket_options=socket_options, **kwargs
        )



url = "https://etamis.accelya.com/axis2/services/DataServiceApi"

querystring = {"wsdl": ""}

payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:axis=\"http://axisapi.tamis.adpcl.com\" xmlns:xsd=\"http://axisapi.tamis.adpcl.com/xsd\">\n<soapenv:Body>\n <axis:getData>\n\t<axis:request>\n\t\t \t <xsd:ODTypeDesc>Ticket</xsd:ODTypeDesc>\n              \t <xsd:agencyLevelDesc>Group</xsd:agencyLevelDesc>\n              \t <xsd:fieldChoiceDesc>Agency id, Agency name, Issuing id, Issuing name, Issuing nation, Issuing type, One/Bothways, Area, Average cpn rate, Basic Agent, Baid issue, Booking agent, Booking area, Booking branch, Booking departmt, Booking ag. id, Booking ag. type, Branch, Marketing id, Marketing name, Marketing nat, Marketing type, Class category, Client Id, Eff Com, Std Com, Suppl Com, Rate Com, Cabin Class FB, Cabin Class RBD, Coupon airp dest, Coupon city dest, Coupon ctry dest, Coupon zone dest, Coupon airp orig, Coupon city orig, Coupon ctry orig, Coupon zone orig, Client ID creator, Department, CCurrency, Distance km, Distance miles, Dom./Int. sale, Fare, Fare basis, Booking class, Fcmi, Frequent flyer, Flight date, Flight day, Flight month, Flight number, Form of payment, Means of payment, Gds, Reporting date, Reporting day, Reporting month, Issue date, Issue day, Issue month, Country of issue, Nb air cpn, Num of tickets, Coupons nights, Ticket id, Orig. Ticket id, Princ. Ticket id, Related ticket id, Coupon id, Transaction count, In/Outbound, Operate id, Operate name, Operate nation, Operate type, Operates, Op. flight nb, Passenger, Pnr, Passenger type, Dom./Int. route, Reason code, Reason sub code, Rel. tickets, EMD Remarks, Route, Service type, Stpid, Stpo, Stp type, Client source Id, Total Tax, Trans. code, Ticket airp dest, Ticket city dest, Ticket ctry dest, Ticket zone dest, Ticket airp orig, Ticket city orig, Ticket ctry orig, Ticket zone orig, VAT on Com, Tourcode, Tourcode type, Travel airp dest, Travel city dest, Travel ctry dest, Travel zone dest, Travel airp orig, Travel city orig, Travel ctry orig, Travel zone orig, Trans type, Ucc, Week/Weekend, Flight week day, Issue week day</xsd:fieldChoiceDesc>\n              \t <xsd:comparisonOnDesc>No</xsd:comparisonOnDesc>\n              \t <xsd:currency>EUR</xsd:currency>\n              \t <xsd:dateTypeDesc>Issue</xsd:dateTypeDesc>\n              \t <xsd:destLevelDesc>World</xsd:destLevelDesc>\n               \t<xsd:format>csv</xsd:format>\n               \t<xsd:from>2017-12-01</xsd:from>\n               \t<xsd:issueLevelDesc>All</xsd:issueLevelDesc>\n               \t<xsd:marketLevelDesc>All</xsd:marketLevelDesc>\n               \t<xsd:name>bi-test</xsd:name>\n               \t<xsd:operateLevelDesc>All</xsd:operateLevelDesc>\n               \t<xsd:origLevelDesc>World</xsd:origLevelDesc>\n               \t<xsd:subTotalDesc>No sub total</xsd:subTotalDesc>\n               \t<xsd:to>2017-12-31</xsd:to>\n               \t<xsd:transactionCode>0,1,2,3,4,5,6,7,8,9</xsd:transactionCode>\n             </axis:request>\n </axis:getData>\n</soapenv:Body>\n</soapenv:Envelope>"
headers = {
    'Content-Type': "text/xml",
    'Authorization': "Basic dHhBUEl1c2U6dHJhdml4YXBp",
    'Cache-Control': "no-cache",
    'Postman-Token': "7b5a0a2a-cf93-3fd4-b685-978ee3017af7"
}

logger.info("starting download...")

session = requests.Session()
keep_alive = TCPKeepAliveAdapter(idle=10, count=2, interval=5)
# requests.adapters.DEFAULT_RETRIES = 50
# adapter = requests.adapters.HTTPAdapter(max_retries=50)
session.mount('https://', keep_alive)


try:
    response = session.post(url, data=payload, headers=headers, params=querystring)
    # response = session.request("POST", url, data=payload, headers=headers, params=querystring,
    #                            timeout=6000)
except:
    e = sys.exc_info()[0]
    logger.error("An exception occured: {}".format(e))


logger.info("finished download...")
# print(response.text)

session.close()