BASE_SCHEMA = {
    "format": {
        "type": "json_schema",
        "name": "get_proposal_info",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                # Payment Info
                "total_premium": {
                    "type": ["string", "null"],
                    "description": "Total policy premium as numeric string",
                },
                "down_payment": {
                    "type": ["string", "null"],
                    "description": "Down payment / initial payment required",
                },
                "monthly_payment": {
                    "type": ["string", "null"],
                    "description": "Monthly installment amount",
                },
                "number_of_payments": {
                    "type": ["integer", "null"],
                    "description": "Number of monthly payments (excluding down payment)",
                },
                # Coverages
                "auto_liability": {
                    "type": ["string", "null"],
                    "description": "Bodily Injury and Property Damage Liability CSL",
                },
                "cargo_limit": {
                    "type": ["string", "null"],
                    "description": "Motor Truck Cargo limit",
                },
                "cargo_deductible": {
                    "type": ["string", "null"],
                    "description": "Motor Truck Cargo deductible",
                },
                "general_liability_per_occurrence": {
                    "type": ["string", "null"],
                    "description": "GL per occurrence limit",
                },
                "general_liability_aggregate": {
                    "type": ["string", "null"],
                    "description": "GL aggregate limit",
                },
                "physical_damage_limit": {
                    "type": ["string", "null"],
                    "description": "Highest stated amount from auto coverage schedule",
                },
                "physical_damage_deductible": {
                    "type": ["string", "null"],
                    "description": "Comp/Collision deductible",
                },
                "non_owned_trailer_pd_limit": {
                    "type": ["string", "null"],
                    "description": "Non-Owned Trailer PD limit",
                },
                "non_owned_trailer_pd_deductible": {
                    "type": ["string", "null"],
                    "description": "Non-Owned Trailer PD deductible",
                },
                "trailer_interchange_limit": {
                    "type": ["string", "null"],
                    "description": "Trailer Interchange limit",
                },
                "trailer_interchange_deductible": {
                    "type": ["string", "null"],
                    "description": "Trailer Interchange deductible",
                },
                "on_hook_limit": {
                    "type": ["string", "null"],
                    "description": "On-Hook limit",
                },
                "on_hook_deductible": {
                    "type": ["string", "null"],
                    "description": "On-Hook deductible",
                },
                "non_trucking_liability": {
                    "type": ["string", "null"],
                    "description": "Non-Trucking Liability CSL",
                },
                "vehicles": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "vin": {"type": ["string", "null"]},
                            "year": {"type": ["string", "null"]},
                            "make": {"type": ["string", "null"]},
                            "model": {"type": ["string", "null"]},
                            "stated_amount": {"type": ["string", "null"]},
                        },
                        "required": ["vin", "year", "make", "model", "stated_amount"],
                        "additionalProperties": False,
                    },
                },
            },
            "additionalProperties": False,
            "required": [
                "total_premium",
                "down_payment",
                "monthly_payment",
                "number_of_payments",
                "auto_liability",
                "cargo_limit",
                "cargo_deductible",
                "general_liability_per_occurrence",
                "general_liability_aggregate",
                "physical_damage_limit",
                "physical_damage_deductible",
                "non_owned_trailer_pd_limit",
                "non_owned_trailer_pd_deductible",
                "trailer_interchange_limit",
                "trailer_interchange_deductible",
                "on_hook_limit",
                "on_hook_deductible",
                "non_trucking_liability",
                "vehicles",
            ],
        },
    }
}
