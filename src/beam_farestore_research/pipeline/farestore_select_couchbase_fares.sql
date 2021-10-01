SELECT
  STRUCT( eventMetadata.UniqueIdentifier AS unique_identifier,
    eventMetadata.SessionId AS session_id,
    eventMetadata.CacheKey AS cache_key ) AS event_metadata,
  UtcTimeStamp AS utc_time_stamp,
  STRUCT( ARRAY((
      SELECT
        AS STRUCT Fares.BrandName AS brand_name,
        Fares.Consolidator AS consolidator,
        Fares.CorporateCode AS corporate_code,
        Fares.DispatchConsolidator AS dispatch_consolidator,
        Fares.FareType AS fare_type,
        Fares.Id AS id,
        Fares.IsBookable AS is_bookable,
        Fares.Key AS key,
        Fares.LastTicketingDay AS last_ticketing_day,
        Fares.MarketingCarrier AS marketing_carrier,
        Fares.PointOfSale AS point_of_sale,
        Fares.Provider AS provider,
        Fares.ProviderAccount AS provider_account,
        Fares.ValidatingCarrier AS validating_carrier,
        Fares.TotalPassengers AS total_passengers,
        Fares.AverageSegments AS average_segments,
        Fares.HaulType AS haul_type,
        Fares.SecretCarrier AS secret_carrier,
        Fares.PurchaseCurrency AS purchase_currency,
        Fares.Filter AS filter,
        Fares.TicketingMethod AS ticketing_method,
        ARRAY((
          SELECT
            AS STRUCT FareAttributes.ChargeIndicator AS charge_indicator,
            FareAttributes.Code AS code
          FROM
            UNNEST(Fares.FareAttributes) AS FareAttributes) ) AS fare_attributes,
        ARRAY((
          SELECT
            AS STRUCT Legs.ArrivalCode AS arrival_code,
            Legs.ArrivalDateTime AS arrival_date_time,
            Legs.DepartureCode AS departure_code,
            Legs.DepartureDateTime AS departure_date_time,
            Legs.DistanceKms AS distance_kms,
            Legs.DurationMins AS duration_mins,
            Legs.Id AS id,
            Legs.LegRef AS leg_ref,
            Legs.Key AS key,
            Legs.MarketingCarrier AS marketing_carrier,
            ARRAY((
              SELECT
                AS STRUCT Segments.AirlineLocator AS airline_locator,
                Segments.ArrivalCode AS arrival_code,
                Segments.ArrivalDateTime AS arrival_date_time,
                Segments.ArrivalTerminal AS arrival_terminal,
                Segments.DepartureCode AS departure_code,
                Segments.DepartureDateTime AS departure_date_time,
                Segments.DepartureTerminal AS departure_terminal,
                Segments.AvailabilitySource AS availability_source,
                Segments.BookingClass AS booking_class,
                Segments.CabinClassType AS cabin_class_type,
                Segments.CodeShareDetail AS code_share_detail,
                Segments.Connection AS connection,
                Segments.DistanceKms AS distance_kms,
                Segments.DurationMins AS duration_mins,
                Segments.Equipment AS equipment,
                Segments.FareBasisCode AS fare_basis_code,
                Segments.FlightNumber AS flight_number,
                Segments.Id AS id,
                Segments.IsFlown AS is_flown,
                Segments.MarketingCarrier AS marketing_carrier,
                Segments.OperatingCarrier AS operating_carrier,
                Segments.SeatsAvailable AS seats_available,
                Segments.StatusCode AS status_code,
                Segments.Stops AS stops,
                Segments.TechnicalStopCode AS technical_stop_code,
                Segments.IsTrainSegment AS is_train_segment,
                Segments.SecretCarrierFlightNumber AS secret_carrier_flight_number,
                STRUCT( Segments.TechnicalStop.Airport AS airport,
                  Segments.TechnicalStop.DepartureDateTime AS departure_date_time,
                  Segments.TechnicalStop.ArrivalDateTime AS arrival_date_time,
                  Segments.TechnicalStop.DurationMins AS duration_mins ) AS technical_stop
              FROM
                UNNEST(Legs.Segments) AS Segments) ) AS segments,
            Legs.SecretCarrierDisplayCode AS secret_carrier_display_code
          FROM
            UNNEST(Fares.Legs) AS Legs) ) AS legs,
        ARRAY((
          SELECT
            AS STRUCT PassengerFares.FareCalculation AS fare_calculation,
            ARRAY((
              SELECT
                AS STRUCT FareInfoLegs.LegRef AS leg_ref,
                ARRAY((
                  SELECT
                    AS STRUCT STRUCT( PaxSegmentDataList.Baggage.Unit AS unit,
                      PaxSegmentDataList.Baggage.Value AS value ) AS baggage,
                    PaxSegmentDataList.BaggageAllowance AS baggage_allowance,
                    PaxSegmentDataList.FareBasisCode AS fare_basis_code,
                    PaxSegmentDataList.FareRuleKey AS fare_rule_key,
                    PaxSegmentDataList.SegmentId AS segment_id
                  FROM
                    UNNEST(FareInfoLegs.PaxSegmentDataList) AS PaxSegmentDataList) ) AS pax_segment_data_list,
                ARRAY((
                  SELECT
                    AS STRUCT ServiceOptions.Code AS code,
                    ServiceOptions.Quantity AS quantity,
                    ServiceOptions.Weight AS weight,
                    ServiceOptions.Amount AS amount,
                    ServiceOptions.Purchase AS purchase,
                    ServiceOptions.DefaultOptIn AS default_opt_in,
                    ServiceOptions.ApplyPer AS apply_per,
                    ServiceOptions.ProductCode AS product_code,
                    ServiceOptions.Unit AS unit
                  FROM
                    UNNEST(FareInfoLegs.ServiceOptions) AS ServiceOptions) ) AS service_options
              FROM
                UNNEST(PassengerFares.FareInfoLegs) AS FareInfoLegs) ) AS fare_info_legs,
            STRUCT( PassengerFares.FarePrice.BaseFare AS base_fare,
              PassengerFares.FarePrice.Tax AS tax,
              ARRAY((
                SELECT
                  AS STRUCT TaxElements.Code AS code,
                  TaxElements.Amount AS amount
                FROM
                  UNNEST(PassengerFares.FarePrice.TaxElements) AS TaxElements) ) AS tax_elements ) AS fare_price,
            PassengerFares.Id AS id,
            PassengerFares.NumberOfPassengers AS number_of_passengers,
            PassengerFares.PassengerType AS passenger_type,
            PassengerFares.PassengerTypeCode AS passenger_type_code
          FROM
            UNNEST(Fares.PassengerFares) AS PassengerFares) ) AS passenger_fares,
        ARRAY((
          SELECT
            AS STRUCT FareDetails.SequenceIndex AS sequence_index,
            FareDetails.Provider AS provider,
            FareDetails.PointOfSale AS point_of_sale,
            FareDetails.Consolidator AS consolidator,
            FareDetails.CorporateCode AS corporate_code,
            FareDetails.DispatchConsolidator AS dispatch_consolidator,
            FareDetails.Key AS key,
            FareDetails.LastTicketingDay AS last_ticketing_day,
            FareDetails.MarketingCarrier AS marketing_carrier,
            FareDetails.FareType AS fare_type,
            FareDetails.ValidatingCarrier AS validating_carrier,
            FareDetails.CreditCardFee AS credit_card_fee,
            FareDetails.TourCode AS tour_code,
            FareDetails.SegmentIds AS segment_ids,
            ARRAY((
              SELECT
                AS STRUCT PassengerPrices.Id AS id,
                PassengerPrices.PassengerType AS passenger_type,
                STRUCT( PassengerPrices.FarePrice.BaseFare AS base_fare,
                  PassengerPrices.FarePrice.Tax AS tax,
                  ARRAY((
                    SELECT
                      AS STRUCT TaxElements.Code AS code,
                      TaxElements.Amount AS amount
                    FROM
                      UNNEST(PassengerPrices.FarePrice.TaxElements) AS TaxElements) ) AS tax_elements ) AS fare_price,
                PassengerPrices.NumberOfPassengers AS number_of_passengers,
                ARRAY((
                  SELECT
                    AS STRUCT PricingItems.Code AS code,
                    PricingItems.Amount AS amount,
                    PricingItems.ApplyAs AS apply_as,
                    PricingItems.ApplyAt AS apply_at,
                    PricingItems.Id AS id,
                    PricingItems.Text AS text
                  FROM
                    UNNEST(PassengerPrices.PricingItems) AS PricingItems) ) AS pricing_items
              FROM
                UNNEST(FareDetails.PassengerPrices) AS PassengerPrices) ) AS passenger_prices,
            ARRAY((
              SELECT
                AS STRUCT FarePricingItems.Code AS code,
                FarePricingItems.Amount AS amount,
                FarePricingItems.ApplyAs AS apply_as,
                FarePricingItems.ApplyAt AS apply_at,
                FarePricingItems.Id AS id,
                FarePricingItems.Text AS text
              FROM
                UNNEST(FareDetails.FarePricingItems) AS FarePricingItems) ) AS fare_pricing_items,
            ARRAY((
              SELECT
                AS STRUCT MarginItems.Code AS code,
                MarginItems.Amount AS amount
              FROM
                UNNEST(FareDetails.MarginItems) AS MarginItems) ) AS margin_items,
            FareDetails.SupplierSource AS supplier_source,
            FareDetails.ProviderAccount AS provider_account,
            ARRAY((
              SELECT
                AS STRUCT ServiceOptions.Code AS code,
                ServiceOptions.Quantity AS quantity,
                ServiceOptions.Weight AS weight,
                ServiceOptions.Amount AS amount,
                ServiceOptions.Purchase AS purchase,
                ServiceOptions.DefaultOptIn AS default_opt_in,
                ServiceOptions.ApplyPer AS apply_per,
                ServiceOptions.ProductCode AS product_code,
                ServiceOptions.Unit AS unit
              FROM
                UNNEST(FareDetails.ServiceOptions) AS ServiceOptions) ) AS service_options,
            FareDetails.SearchId AS search_id,
            STRUCT( FareDetails.NonMorConstraints.MaxAllowance AS max_allowance,
              FareDetails.NonMorConstraints.SplitAllowed AS split_allowed ) AS non_mor_constraints,
            FareDetails.UniqueId AS unique_id,
            ARRAY((
              SELECT
                AS STRUCT FareNotesForConditions.Code AS code,
                FareNotesForConditions.Text AS text,
                ARRAY((
                  SELECT
                    AS STRUCT PlaceHolders.Name AS name,
                    PlaceHolders.Value AS value
                  FROM
                    UNNEST(FareNotesForConditions.PlaceHolders) AS PlaceHolders) ) AS place_holders
              FROM
                UNNEST(FareDetails.FareNotesForConditions) AS FareNotesForConditions) ) AS fare_notes_for_conditions,
            ARRAY((
              SELECT
                AS STRUCT BaggageOptions.Code AS code,
                BaggageOptions.SupplierCode AS supplier_code,
                BaggageOptions.Unit AS unit,
                BaggageOptions.Weight AS weight,
                BaggageOptions.Quantity AS quantity,
                BaggageOptions.OriginalPrice AS original_price,
                BaggageOptions.MarkupAmount AS markup_amount,
                BaggageOptions.TotalPrice AS total_price,
                BaggageOptions.PassengerTypes AS passenger_types
              FROM
                UNNEST(FareDetails.BaggageOptions) AS BaggageOptions) ) AS baggage_options,
            FareDetails.SeatMapAvailable AS seat_map_available
          FROM
            UNNEST(Fares.FareDetails) AS FareDetails) ) AS fare_details,
        ARRAY((
          SELECT
            AS STRUCT FareNotes.Code AS code,
            FareNotes.Text AS text,
            ARRAY((
              SELECT
                AS STRUCT PlaceHolders.Name AS name,
                PlaceHolders.Value AS value
              FROM
                UNNEST(FareNotes.PlaceHolders) AS PlaceHolders) ) AS place_holders
          FROM
            UNNEST(Fares.FareNotes) AS FareNotes) ) AS fare_notes,
        ARRAY((
          SELECT
            AS STRUCT ServiceOptions.Code AS code,
            ServiceOptions.Quantity AS quantity,
            ServiceOptions.Weight AS weight,
            ServiceOptions.Amount AS amount,
            ServiceOptions.Purchase AS purchase,
            ServiceOptions.DefaultOptIn AS default_opt_in,
            ServiceOptions.ApplyPer AS apply_per,
            ServiceOptions.ProductCode AS product_code,
            ServiceOptions.Unit AS unit
          FROM
            UNNEST(Fares.ServiceOptions) AS ServiceOptions) ) AS service_options,
        Fares.SupplierSource AS supplier_source,
        Fares.CallToBook AS call_to_book,
        Fares.Subset AS subset
      FROM
        UNNEST(Response.Fares) AS Fares) ) AS fares,
    Response.Ref AS ref,
    Response.HasDeduping AS has_deduping ) AS response
FROM
  `travix-bi.staging.farestore_couchbase`
WHERE
  DATE(UtcTimeStamp) = "2019-08-24"
--   AND eventMetadata.UniqueIdentifier = '951e3772-3d0a-4f4b-8b46-c99bc6ced3f7'
LIMIT
  10