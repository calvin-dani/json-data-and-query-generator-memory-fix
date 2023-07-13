FEASIBILITY_MATRIX = {
    "SUM(:1)": {
        "array": "FAIL",
        "boolean": "FAIL",
        "null": "FAIL",
        "number": "SUCCESS",
        "object": "FAIL",
        "string": "FAIL",
    },
    "COUNT(:1)": {
        "array": "FAIL",
        "boolean": "FAIL",
        "null": "FAIL",
        "number": "SUCCESS",
        "object": "FAIL",
        "string": "FAIL",
    },
    "AVG(:1)": {
        "array": "FAIL",
        "boolean": "FAIL",
        "null": "FAIL",
        "number": "SUCCESS",
        "object": "FAIL",
        "string": "FAIL",
    },
    "MIN(:1)": {
        "array": "FAIL",
        "boolean": "FAIL",
        "null": "FAIL",
        "number": "SUCCESS",
        "object": "FAIL",
        "string": "FAIL",
    },
    "MAX(:1)": {
        "array": "FAIL",
        "boolean": "FAIL",
        "null": "FAIL",
        "number": "SUCCESS",
        "object": "FAIL",
        "string": "FAIL",
    },
    "TO_DOUBLE(:1)": {
        "string": "FAIL",
        "object": "FAIL",
        "number": "SUCCESS",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "TAN(:1)": {
        "string": "FAIL",
        "object": "FAIL",
        "number": "SUCCESS",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "TO_BIGINT(:1)": {
        "string": "FAIL",
        "object": "FAIL",
        "number": "SUCCESS",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "ASIN(:1)": {
        "string": "FAIL",
        "object": "FAIL",
        "number": "SUCCESS",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "CONCAT(:1, :2)": {
        "string": {
            "string": "SUCCESS",
            "object": "SUCCESS",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "object": {
            "string": "SUCCESS",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "number": {
            "string": "SUCCESS",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "boolean": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "array": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "null": {
            "string": "SUCCESS",
            "object": "SUCCESS",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
    },
    "ABS(:1)": {
        "string": "FAIL",
        "object": "FAIL",
        "number": "SUCCESS",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "LOWER(:1)": {
        "string": "SUCCESS",
        "object": "FAIL",
        "number": "FAIL",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "LN(:1)": {
        "string": "FAIL",
        "object": "FAIL",
        "number": "SUCCESS",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "(:1)+(:2)": {
        "string": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "object": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "number": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "boolean": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "array": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "null": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
    },
    "LOG(:1, :2)": {
        "string": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "object": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "number": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "boolean": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "array": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "null": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
    },
    "SIN(:1)": {
        "string": "FAIL",
        "object": "FAIL",
        "number": "SUCCESS",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "(:1)*(:2)": {
        "string": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "object": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "number": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "boolean": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "array": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "null": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
    },
    "ATAN2(:1, :2)": {
        "string": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "object": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "number": {
            "string": "SUCCESS",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "boolean": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "array": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "null": {
            "string": "SUCCESS",
            "object": "SUCCESS",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
    },
    "ATAN(:1)": {
        "string": "FAIL",
        "object": "FAIL",
        "number": "SUCCESS",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "(:1)/(:2)": {
        "string": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "object": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "number": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "boolean": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "array": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "null": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
    },
    "UPPER(:1)": {
        "string": "SUCCESS",
        "object": "FAIL",
        "number": "FAIL",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "TO_VARCHAR(:1)": {
        "string": "SUCCESS",
        "object": "SUCCESS",
        "number": "SUCCESS",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "(:1)-(:2)": {
        "string": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "object": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "number": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "boolean": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "array": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "null": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
    },
    "ACOS(:1)": {
        "string": "FAIL",
        "object": "FAIL",
        "number": "SUCCESS",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "LENGTH(:1)": {
        "string": "SUCCESS",
        "object": "FAIL",
        "number": "FAIL",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "COS(:1)": {
        "string": "FAIL",
        "object": "FAIL",
        "number": "SUCCESS",
        "boolean": "FAIL",
        "array": "FAIL",
        "null": "SUCCESS",
    },
    "MOD(:1, :2)": {
        "string": {
            "string": "FAIL",
            "object": "SUCCESS",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "object": {
            "string": "SUCCESS",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "number": {
            "string": "SUCCESS",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "boolean": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "array": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "null": {
            "string": "SUCCESS",
            "object": "SUCCESS",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
    },
    "POWER(:1, :2)": {
        "string": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "object": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "number": {
            "string": "SUCCESS",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "boolean": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "array": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "null": {
            "string": "SUCCESS",
            "object": "SUCCESS",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
    },
    "ROUND(:1, :2)": {
        "string": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "object": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "number": {
            "string": "SUCCESS",
            "object": "FAIL",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
        "boolean": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "array": {
            "string": "FAIL",
            "object": "FAIL",
            "number": "FAIL",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "FAIL",
        },
        "null": {
            "string": "SUCCESS",
            "object": "SUCCESS",
            "number": "SUCCESS",
            "boolean": "FAIL",
            "array": "FAIL",
            "null": "SUCCESS",
        },
    },
}
