import pycurl
import io
import curl

SERVER_URL = 'https://etamis.accelya.com/axis2/services/DataServiceApi?wsdl='
HTTP_HEADER = ['Authorization: Basic dHhBUEl1c2U6dHJhdml4YXBp', 'Cache-Control: no-cache', 'Content-Type: text/xml']
TIMEOUT = 30000
CONNECT_TIMEOUT = 300

XML ="""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:axis="http://axisapi.tamis.adpcl.com" xmlns:xsd="http://axisapi.tamis.adpcl.com/xsd">
<soapenv:Body>
 <axis:getData>
        <axis:request>
                         <xsd:ODTypeDesc>Ticket</xsd:ODTypeDesc>
                 <xsd:agencyLevelDesc>Group</xsd:agencyLevelDesc>
                 <xsd:fieldChoiceDesc>Agency id, Agency name, Issuing id, Issuing name, Issuing nation, Issuing type, One/Bothways, Area, Average cpn rate, Basic Agent, Baid issue, Booking agent, Booking area, Booking branch, Booking departmt, Booking ag. id, Booking ag. type, Branch, Marketing id, Marketing name, Marketing nat, Marketing type, Class category, Client Id, Eff Com, Std Com, Suppl Com, Rate Com, Cabin Class FB, Cabin Class RBD, Coupon airp dest, Coupon city dest, Coupon ctry dest, Coupon zone dest, Coupon airp orig, Coupon city orig, Coupon ctry orig, Coupon zone orig, Client ID creator, Department, CCurrency, Distance km, Distance miles, Dom./Int. sale, Fare, Fare basis, Booking class, Fcmi, Frequent flyer, Flight date, Flight day, Flight month, Flight number, Form of payment, Means of payment, Gds, Reporting date, Reporting day, Reporting month, Issue date, Issue day, Issue month, Country of issue, Nb air cpn, Num of tickets, Coupons nights, Ticket id, Orig. Ticket id, Princ. Ticket id, Related ticket id, Coupon id, Transaction count, In/Outbound, Operate id, Operate name, Operate nation, Operate type, Operates, Op. flight nb, Passenger, Pnr, Passenger type, Dom./Int. route, Reason code, Reason sub code, Rel. tickets, EMD Remarks, Route, Service type, Stpid, Stpo, Stp type, Client source Id, Total Tax, Trans. code, Ticket airp dest, Ticket city dest, Ticket ctry dest, Ticket zone dest, Ticket airp orig, Ticket city orig, Ticket ctry orig, Ticket zone orig, VAT on Com, Tourcode, Tourcode type, Travel airp dest, Travel city dest, Travel ctry dest, Travel zone dest, Travel airp orig, Travel city orig, Travel ctry orig, Travel zone orig, Trans type, Ucc, Week/Weekend, Flight week day, Issue week day</xsd:fieldChoiceDesc>
                 <xsd:comparisonOnDesc>No</xsd:comparisonOnDesc>
                 <xsd:currency>EUR</xsd:currency>
                 <xsd:dateTypeDesc>Issue</xsd:dateTypeDesc>
                 <xsd:destLevelDesc>World</xsd:destLevelDesc>
                <xsd:format>csv</xsd:format>
                <xsd:from>2017-12-01</xsd:from>
                <xsd:issueLevelDesc>All</xsd:issueLevelDesc>
                <xsd:marketLevelDesc>All</xsd:marketLevelDesc>
                <xsd:name>bi-test</xsd:name>
                <xsd:operateLevelDesc>All</xsd:operateLevelDesc>
                <xsd:origLevelDesc>World</xsd:origLevelDesc>
                <xsd:subTotalDesc>No sub total</xsd:subTotalDesc>
                <xsd:to>2017-12-31</xsd:to>
                <xsd:transactionCode>0,1,2,3,4,5,6,7,8,9</xsd:transactionCode>
             </axis:request>
 </axis:getData>
</soapenv:Body>
</soapenv:Envelope>"""

with open('response.csv', 'wb') as f:
    c = pycurl.Curl()
    c.setopt(pycurl.URL, SERVER_URL)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.HTTPHEADER, HTTP_HEADER)
    c.setopt(pycurl.TCP_KEEPALIVE, 1)
    c.setopt(pycurl.TIMEOUT, TIMEOUT)
    c.setopt(pycurl.CONNECTTIMEOUT, CONNECT_TIMEOUT)
    # c.setopt(pycurl.NOSIGNAL, 1) # disable signals, curl will be using other means besides signals to timeout.
    c.setopt(pycurl.POSTFIELDS, XML)
    c.setopt(pycurl.WRITEDATA, f)
    c.perform()
    c.close()
