def create_clientes_expectations(validator):
    validator.expect_column_values_to_not_be_null("id_cliente")
    validator.expect_column_values_to_be_unique("id_cliente")
    validator.expect_column_values_to_match_regex("email", r"^[\w\.-]+@[\w\.-]+\.\w+$")
    validator.expect_column_values_to_match_regex("telefone", r"^\d{11}$")
    return validator