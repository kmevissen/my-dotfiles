from deepmerge import conservative_merger, always_merger, Merger

# shop_service_amadeus
bigquery_schema_1 = {
  "fields": [
    {
      "name": "loggername",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "level",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "SchemaVersion",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "metaData",
      "type": "RECORD",
      "mode": "NULLABLE",
      "fields": [
        {
          "name": "utcTimeStamp",
          "type": "DATETIME",
          "mode": "NULLABLE"
        },
        {
          "name": "businessProcess",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "environment",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "messageType",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "journeyType",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "requestId",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "sessionId",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "uniqueId",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "affiliateCode",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "channelCode",
          "type": "STRING",
          "mode": "NULLABLE"
        }
      ]
    },
    {
      "name": "payload",
      "type": "RECORD",
      "mode": "NULLABLE",
      "fields": [
        {
          "name": "request",
          "type": "RECORD",
          "mode": "NULLABLE",
          "fields": [
            {
              "name": "debug",
              "type": "BOOLEAN",
              "mode": "NULLABLE"
            },
            {
              "name": "provider",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "affiliate",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "channel",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "app",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "searchType",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "legs",
              "type": "RECORD",
              "mode": "REPEATED",
              "fields": [
                {
                  "name": "ref",
                  "type": "NUMERIC",
                  "mode": "NULLABLE"
                },
                {
                  "name": "departureCode",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "departureCountry",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "departureRegion",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "arrivalCode",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "arrivalCountry",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "arrivalRegion",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "departureDateTime",
                  "type": "DATETIME",
                  "mode": "NULLABLE"
                }
              ]
            },
            {
              "name": "cabinClass",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "nonStopDirect",
              "type": "BOOLEAN",
              "mode": "NULLABLE"
            },
            {
              "name": "adults",
              "type": "NUMERIC",
              "mode": "NULLABLE"
            },
            {
              "name": "children",
              "type": "NUMERIC",
              "mode": "NULLABLE"
            },
            {
              "name": "infants",
              "type": "NUMERIC",
              "mode": "NULLABLE"
            },
            {
              "name": "currency",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "requestModifiers",
              "type": "RECORD",
              "mode": "NULLABLE",
              "fields": [
                {
                  "name": "TaxBreakdown",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                },
                {
                  "name": "CorporateCodes",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "NumberOfResults",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "FareType",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "CabinClass",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "PointOfSale",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "ConsolidatorCode",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "GdsAccountCode",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "DisallowedAirlines",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "CombinedOneWay",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                },
                {
                  "name": "DirectFlight",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                },
                {
                  "name": "CombinedOneWaySplitPercentage",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "PreferredAirlines",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "OriginRadius",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "OriginMultiCities",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "DestinationRadius",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "CalendarSearch",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                },
                {
                  "name": "DestinationMultiCities",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "InstantSearch",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                },
                {
                  "name": "FreeBaggageAllowance",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                },
                {
                  "name": "ConnectionPoints",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "CurrencyConversion",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                },
                {
                  "name": "AlternatePointOfSale",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "NdcSearch",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "MetaSearch",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                }
              ]
            },
            {
              "name": "language",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "traffic",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "bypassInruleSfd",
              "type": "BOOLEAN",
              "mode": "NULLABLE"
            }
          ]
        },
        {
          "name": "response",
          "type": "RECORD",
          "mode": "NULLABLE",
          "fields": [
            {
              "name": "httpStatus",
              "type": "NUMERIC",
              "mode": "NULLABLE"
            },
            {
              "name": "httpStatusName",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "duration",
              "type": "NUMERIC",
              "mode": "NULLABLE"
            },
            {
              "name": "attributes",
              "type": "RECORD",
              "mode": "NULLABLE",
              "fields": [
                {
                  "name": "groupedFaresCount",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "flattenFaresCount",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "fareCount",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "supplierSessionId",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "shopSource",
                  "type": "STRING",
                  "mode": "NULLABLE"
                }
              ]
            },
            {
              "name": "error",
              "type": "RECORD",
              "mode": "NULLABLE",
              "fields": [
                {
                  "name": "source",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "httpStatus",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "logLevel",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "errorCode",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "stackTrace",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "sourceCause",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "details",
                  "type": "RECORD",
                  "mode": "NULLABLE",
                  "fields": [
                    {
                      "name": "FromCurrency",
                      "type": "STRING",
                      "mode": "NULLABLE"
                    },
                    {
                      "name": "ToCurrency",
                      "type": "STRING",
                      "mode": "NULLABLE"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "name": "sessionid",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "correlationid",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "requestid",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "uniqueId",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "applicationgroup",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "applicationname",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "hostname",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "type",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "stream",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "docker",
      "type": "RECORD",
      "mode": "NULLABLE",
      "fields": [
        {
          "name": "container_id",
          "type": "STRING",
          "mode": "NULLABLE"
        }
      ]
    },
    {
      "name": "kubernetes",
      "type": "RECORD",
      "mode": "NULLABLE",
      "fields": [
        {
          "name": "container_name",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "namespace_name",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "pod_name",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "pod_id",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "labels",
          "type": "RECORD",
          "mode": "NULLABLE",
          "fields": [
            {
              "name": "app",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "pod_template_hash",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "team",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "version",
              "type": "STRING",
              "mode": "NULLABLE"
            }
          ]
        },
        {
          "name": "host",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "master_url",
          "type": "STRING",
          "mode": "NULLABLE"
        }
      ]
    },
    {
      "name": "topic",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "fluent_timestamp",
      "type": "NUMERIC",
      "mode": "NULLABLE"
    },
    {
      "name": "UtcTimeStamp",
      "type": "TIMESTAMP",
      "mode": "NULLABLE"
    },
    {
      "name": "PubSubTimeStamp",
      "type": "TIMESTAMP",
      "mode": "NULLABLE"
    }
  ]
}

# shop_service_travelport
bigquery_schema_2 = {
  "fields": [
    {
      "name": "loggername",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "level",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "SchemaVersion",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "metaData",
      "type": "RECORD",
      "mode": "NULLABLE",
      "fields": [
        {
          "name": "utcTimeStamp",
          "type": "DATETIME",
          "mode": "NULLABLE"
        },
        {
          "name": "businessProcess",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "environment",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "messageType",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "journeyType",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "requestId",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "sessionId",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "uniqueId",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "affiliateCode",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "channelCode",
          "type": "STRING",
          "mode": "NULLABLE"
        }
      ]
    },
    {
      "name": "payload",
      "type": "RECORD",
      "mode": "NULLABLE",
      "fields": [
        {
          "name": "request",
          "type": "RECORD",
          "mode": "NULLABLE",
          "fields": [
            {
              "name": "debug",
              "type": "BOOLEAN",
              "mode": "NULLABLE"
            },
            {
              "name": "provider",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "affiliate",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "channel",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "app",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "searchType",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "legs",
              "type": "RECORD",
              "mode": "REPEATED",
              "fields": [
                {
                  "name": "ref",
                  "type": "NUMERIC",
                  "mode": "NULLABLE"
                },
                {
                  "name": "departureCode",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "departureCountry",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "departureRegion",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "arrivalCode",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "arrivalCountry",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "arrivalRegion",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "departureDateTime",
                  "type": "DATETIME",
                  "mode": "NULLABLE"
                }
              ]
            },
            {
              "name": "cabinClass",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "nonStopDirect",
              "type": "BOOLEAN",
              "mode": "NULLABLE"
            },
            {
              "name": "adults",
              "type": "NUMERIC",
              "mode": "NULLABLE"
            },
            {
              "name": "children",
              "type": "NUMERIC",
              "mode": "NULLABLE"
            },
            {
              "name": "infants",
              "type": "NUMERIC",
              "mode": "NULLABLE"
            },
            {
              "name": "currency",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "requestModifiers",
              "type": "RECORD",
              "mode": "NULLABLE",
              "fields": [
                {
                  "name": "NumberOfResults",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "DisallowedAirlines",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "CabinClass",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "FareType",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "ConsolidatorCode",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "PointOfSale",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "MetaSearch",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                },
                {
                  "name": "CorporateCodes",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "GdsAccountCode",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "CombinedOneWaySplitPercentage",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "CombinedOneWay",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                },
                {
                  "name": "PreferredAirlines",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "SupplierChannelId",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "DirectFlight",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                },
                {
                  "name": "ConnectionPoints",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "FreeBaggageAllowance",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                },
                {
                  "name": "CalendarSearch",
                  "type": "BOOLEAN",
                  "mode": "NULLABLE"
                }
              ]
            },
            {
              "name": "language",
              "type": "STRING",
              "mode": "NULLABLE"
            }
          ]
        },
        {
          "name": "response",
          "type": "RECORD",
          "mode": "NULLABLE",
          "fields": [
            {
              "name": "httpStatus",
              "type": "NUMERIC",
              "mode": "NULLABLE"
            },
            {
              "name": "httpStatusName",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "duration",
              "type": "NUMERIC",
              "mode": "NULLABLE"
            },
            {
              "name": "error",
              "type": "RECORD",
              "mode": "NULLABLE",
              "fields": [
                {
                  "name": "source",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "sourceCause",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "httpStatus",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "logLevel",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "errorCode",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "stackTrace",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "details",
                  "type": "RECORD",
                  "mode": "NULLABLE",
                  "fields": [
                    {
                      "name": "SoapResponse",
                      "type": "STRING",
                      "mode": "NULLABLE"
                    }
                  ]
                }
              ]
            },
            {
              "name": "attributes",
              "type": "RECORD",
              "mode": "NULLABLE",
              "fields": [
                {
                  "name": "groupedFaresCount",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "flattenFaresCount",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "fareCount",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "supplierSessionId",
                  "type": "STRING",
                  "mode": "NULLABLE"
                },
                {
                  "name": "shopSource",
                  "type": "STRING",
                  "mode": "NULLABLE"
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "name": "sessionid",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "correlationid",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "requestid",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "uniqueId",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "applicationgroup",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "applicationname",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "hostname",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "type",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "stream",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "docker",
      "type": "RECORD",
      "mode": "NULLABLE",
      "fields": [
        {
          "name": "container_id",
          "type": "STRING",
          "mode": "NULLABLE"
        }
      ]
    },
    {
      "name": "kubernetes",
      "type": "RECORD",
      "mode": "NULLABLE",
      "fields": [
        {
          "name": "container_name",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "namespace_name",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "pod_name",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "pod_id",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "labels",
          "type": "RECORD",
          "mode": "NULLABLE",
          "fields": [
            {
              "name": "app",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "pod_template_hash",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "team",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "version",
              "type": "STRING",
              "mode": "NULLABLE"
            }
          ]
        },
        {
          "name": "host",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "master_url",
          "type": "STRING",
          "mode": "NULLABLE"
        }
      ]
    },
    {
      "name": "topic",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "fluent_timestamp",
      "type": "NUMERIC",
      "mode": "NULLABLE"
    },
    {
      "name": "UtcTimeStamp",
      "type": "TIMESTAMP",
      "mode": "NULLABLE"
    },
    {
      "name": "PubSubTimeStamp",
      "type": "TIMESTAMP",
      "mode": "NULLABLE"
    }
  ]
}

print(conservative_merger.merge(bigquery_schema_1, bigquery_schema_2))

schema_1 = {'a': 1, 'b': [{'c': 2}]}
schema_2 = {'a': 1, 'b': [{'d': 3}], 'e': 5}

new_schema = {**schema_1, **schema_2}
z = conservative_merger.merge(schema_1, schema_2)

print(new_schema)
print(z)

bq_schema_1 = {
  "fields": [
    {
      "name": "loggername",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "level",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "SchemaVersion",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "metaData",
      "type": "RECORD",
      "mode": "NULLABLE",
      "fields": [
        {
          "name": "utcTimeStamp",
          "type": "DATETIME",
          "mode": "NULLABLE"
        },
        {
          "name": "businessProcess",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "environment",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "messageType",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "journeyType",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "requestId",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "sessionId",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "uniqueId",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "affiliateCode",
          "type": "STRING",
          "mode": "NULLABLE"
        }
      ]
    }]}
bq_schema_2 = {
  "fields": [
    {
      "name": "loggername",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "metaData",
      "type": "RECORD",
      "mode": "NULLABLE",
      "fields": [
        {
          "name": "affiliateCode",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "channelCode",
          "type": "STRING",
          "mode": "NULLABLE"
        }
      ]
    }]}

# this yields an incorrect schema
print(conservative_merger.merge(dict(bq_schema_1), dict(bq_schema_2)))